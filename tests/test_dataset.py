import unittest

from radiometry import dataset, metadata


class TestEveDataset(unittest.TestCase):
    def setUp(self):
        self.dataset = dataset.EveDataset()

    def test_instantiate_class(self):
        pass

    def test_metadata_is_EveDatasetMetadata(self):
        self.assertTrue(
            isinstance(
                self.dataset.metadata,
                metadata.EveDatasetMetadata,
            )
        )
