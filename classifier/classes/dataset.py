from classifier.classes import DatasetManager


class Dataset:
    """
    Handles dataset loading, splitting, and encoding.
    """
    def __init__(self, csv_path: str, batch_size: int, img_size: tuple):
        self.csv_path = csv_path
        self.batch_size = batch_size
        self.img_size = img_size

        self._dataset_former = DatasetManager(self.csv_path)
        self.train_set = None
        self.val_set = None
        self.all_image_paths = None
        self.labels = None
        self.label_encoder = None
        self.num_classes = None

    def prepare(self, train_ratio: float = 0.8, shuffle: bool = True):
        self._dataset_former.build(
            train_ratio=train_ratio,
            batch_size=self.batch_size,
            shuffle=shuffle
        )
        self.train_set = self._dataset_former.train_set
        self.val_set = self._dataset_former.val_set

        self.all_image_paths = self._dataset_former.all_image_paths
        self.labels = self._dataset_former.labels
        self.label_encoder = self._dataset_former.get_label_encoder()
        self.num_classes = self._dataset_former.num_classes

    def inference_dataset(self, shuffle: bool = False):
        return self._dataset_former.inference_dataset(shuffle=shuffle)