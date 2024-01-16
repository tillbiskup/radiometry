import unittest

from radiometry import metadata


class TestEveDatasetMetadata(unittest.TestCase):
    def setUp(self):
        self.eve_dataset_metadata = metadata.EveDatasetMetadata()

    def test_instantiate_class(self):
        pass
