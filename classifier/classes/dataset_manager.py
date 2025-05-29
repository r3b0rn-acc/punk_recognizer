from typing import List, Optional, Tuple

import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from classifier.utils import load_image


class DatasetManager:
    """
    Управляет данными: чтение CSV, кодирование меток и построение tf.data.Dataset для обучения, валидации и инференса.
    """
    def __init__(
        self,
        csv_path: str,
        random_state: int = 42,
    ) -> None:
        self.csv_path = csv_path
        self.random_state = random_state

        df = pd.read_csv(self.csv_path)
        if not {'path', 'label'}.issubset(df.columns):
            raise ValueError("CSV должен содержать столбцы 'path' и 'label'")

        self.all_image_paths: List[str] = df['path'].tolist()
        raw_labels = df['label'].tolist()

        self._encoder = LabelEncoder()
        self.labels: List[int] = self._encoder.fit_transform(raw_labels).tolist()
        self.num_classes: int = len(self._encoder.classes_)

        self.train_set: Optional[tf.data.Dataset] = None
        self.val_set: Optional[tf.data.Dataset] = None

    def split(self, train_ratio) -> Tuple[List[str], List[str], List[int], List[int]]:
        """
        Разбивает на train/val по train_ratio.

        Returns:
            train_paths, val_paths, train_labels, val_labels
        """
        return train_test_split(
            self.all_image_paths,
            self.labels,
            test_size=1 - train_ratio,
            stratify=self.labels,
            random_state=self.random_state,
        )

    def build(self, batch_size: int = 32, train_ratio: float = 0.8, shuffle: bool = True) -> None:
        """
        Создает train_set и val_set.

        Args:
            batch_size: Размер батча.
            train_ratio: Соотношение.
            shuffle: Перемешивать ли при создании.
        """
        train_p, val_p, train_l, val_l = self.split(train_ratio=train_ratio)
        self.train_set = self._make_dataset(train_p, train_l, batch_size, shuffle)
        self.val_set = self._make_dataset(val_p, val_l, batch_size, shuffle)

    def _make_dataset(
        self,
        paths: List[str],
        labels: Optional[List[int]],
        batch_size: int,
        shuffle: bool,
    ) -> tf.data.Dataset:
        """
        Генерирует tf.data.Dataset из путей и опциональных меток.

        Args:
            paths: Список путей к изображениям.
            labels: Список меток или None для инференса.
            shuffle: Флаг перемешивания.
        Returns:
            tf.data.Dataset
        """
        if labels is not None:
            ds = tf.data.Dataset.from_tensor_slices((paths, labels))
            if shuffle:
                ds = ds.shuffle(buffer_size=len(paths), reshuffle_each_iteration=True)
            ds = ds.map(
                lambda p, l: load_image(p, l),
                num_parallel_calls=tf.data.AUTOTUNE,
            )
        else:
            ds = tf.data.Dataset.from_tensor_slices(paths)
            if shuffle:
                ds = ds.shuffle(buffer_size=len(paths), reshuffle_each_iteration=True)
            ds = ds.map(
                lambda p: load_image(p),
                num_parallel_calls=tf.data.AUTOTUNE,
            )

        return ds.batch(batch_size).prefetch(tf.data.AUTOTUNE)

    def inference_dataset(self, batch_size: int = 32, shuffle: bool = False) -> tf.data.Dataset:
        """
        Создает датасет для инференса без меток.

        Args:
            paths: Пути к изображениям.
            batch_size: Размер батча
            shuffle: Перемешивание.
        """
        return self._make_dataset(self.all_image_paths, labels=None, batch_size=batch_size, shuffle=shuffle)

    def get_label_encoder(self) -> LabelEncoder:
        """
        Возвращает LabelEncoder для обратного преобразования.
        """
        return self._encoder

    def get_class_names(self) -> List[str]:
        """
        Оригинальные названия классов.
        """
        return list(self._encoder.classes_)
