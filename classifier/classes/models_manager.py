import tensorflow as tf
from tensorflow.keras import layers, models, optimizers, losses, metrics
from tensorflow.keras.applications.resnet50 import ResNet50


class ModelsManager:
    """
    Утилити класс для удобства работы с моделями tf + кеширует модели
    """
    def __init__(self, img_size: tuple, embedding_dim: int, num_classes: int):
        self._cache = dict.fromkeys(['classifier', 'embedding_model'])

        self.img_size = img_size
        self.embedding_dim = embedding_dim
        self.num_classes = num_classes

    def build(self):
        base = ResNet50(
            include_top=False,
            weights='imagenet',
            input_shape=self.img_size + (3,)
        )
        base.trainable = False

        inputs = layers.Input(shape=self.img_size + (3,))
        x = base(inputs, training=False)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dropout(0.3)(x)

        emb = layers.Dense(self.embedding_dim, name='embedding_dense')(x)
        emb = layers.Lambda(lambda t: tf.math.l2_normalize(t, axis=1), name='embedding')(emb)

        logits = layers.Dense(
            self.num_classes,
            activation='softmax',
            name='classifier'
        )(emb)

        classifier = models.Model(
            inputs=inputs,
            outputs=logits,
            name='classifier_model'
        )
        classifier.compile(
            optimizer=optimizers.Adam(1e-4),
            loss=losses.SparseCategoricalCrossentropy(),
            metrics=[metrics.SparseCategoricalAccuracy()]
        )

        embedding_model = models.Model(
            inputs=inputs,
            outputs=emb,
            name='embedding_model'
        )

        self._cache['classifier'] = classifier
        self._cache['embedding_model'] = embedding_model

    @property
    def classifier(self):
        if not self._cache.get('classifier'):
            self.build()

        return self._cache.get('classifier')

    @property
    def embedding_model(self):
        if not self._cache.get('embedding_model'):
            self.build()

        return self._cache.get('embedding_model')
