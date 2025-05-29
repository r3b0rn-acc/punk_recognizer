import joblib
import tensorflow as tf

from pathlib import Path
from typing import List, Dict, Tuple


from classifier.classes import Dataset, ModelsManager


class ImageSearcher:
    def __init__(
        self,
        dataset_path: str,
        index_path: Path,
        weights_path: Path,
        image_size: Tuple[int, int] = (512, 512),
        batch_size: int = 32,
        embedding_dim: int = 128,
    ):
        self.image_size = image_size
        self.dataset = Dataset(dataset_path, batch_size, image_size)
        self.dataset.prepare(train_ratio=0.8, shuffle=True)

        models_manager = ModelsManager(image_size, embedding_dim, self.dataset.num_classes)
        self.classifier = models_manager.classifier
        self.embedding_model = models_manager.embedding_model
        self.classifier.load_weights(weights_path)

        data = joblib.load(index_path)
        self.nn_index = data['nn_index']
        self.image_paths: List[str] = data['image_paths']

    def preprocess(self, image_path: str) -> tf.Tensor:
        img = tf.io.read_file(image_path)
        img = tf.image.decode_jpeg(img, channels=3)
        img = tf.image.resize(img, self.image_size)
        img = tf.keras.applications.resnet50.preprocess_input(img)
        return tf.expand_dims(img, axis=0)

    def query(self, query_path: str, top_k: int = 3) -> List[Tuple[str, float, str]]:
        tensor = self.preprocess(query_path)
        emb = self.embedding_model(tensor, training=False).numpy()
        dists, inds = self.nn_index.kneighbors(emb, n_neighbors=top_k + 1)

        results = []
        for dist, idx in zip(dists[0][1:], inds[0][1:]):
            label = self.dataset.label_encoder.inverse_transform(
                [self.dataset.labels[idx]]
            )[0]
            results.append((self.image_paths[idx], float(dist), label))
        return results

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        top_k_found = []

        for path, dist, label in self.query(query, top_k=top_k):
            top_k_found.append({'image_path': str(path), 'dist': dist, 'label': label})

        return top_k_found
