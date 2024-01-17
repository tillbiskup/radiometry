import datetime
import unittest

from radiometry import metadata


class TestEveDatasetMetadata(unittest.TestCase):
    def setUp(self):
        self.metadata = metadata.EveDatasetMetadata()

    def test_instantiate_class(self):
        pass

    def test_has_measurement_metadata(self):
        self.assertTrue(
            isinstance(
                self.metadata.measurement,
                metadata.Measurement,
            )
        )


class TestMeasurement(unittest.TestCase):
    def setUp(self):
        self.measurement = metadata.Measurement()

    def test_instantiate_class(self):
        pass

    def test_has_additional_attributes(self):
        attributes = ["duration", "location"]
        for attribute in attributes:
            with self.subTest(attribute=attribute):
                self.assertTrue(hasattr(self.measurement, attribute))

    def test_start_is_datetime_object(self):
        self.assertIsInstance(self.measurement.start, datetime.datetime)

    def test_end_is_datetime_object(self):
        self.assertIsInstance(self.measurement.end, datetime.datetime)

    def test_instantiate_properties_from_dict(self):
        dict_ = {
            "purpose": "Kill time",
            "operator": "John Doe",
            "labbook_entry": "loi:42.1001/foo/bar",
        }
        measurement = metadata.Measurement(dict_)
        for key in dict_:
            self.assertEqual(getattr(measurement, key), dict_[key])

    def test_set_properties_from_dict(self):
        dict_ = {
            "purpose": "Kill time",
            "operator": "John Doe",
            "labbook_entry": "loi:42.1001/foo/bar",
        }
        self.measurement.from_dict(dict_)
        for key in dict_:
            self.assertEqual(getattr(self.measurement, key), dict_[key])


class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device = metadata.Device()

    def test_instantiate_class(self):
        pass

    def test_set_properties_from_dict(self):
        dict_ = {"label": "foo"}
        self.device.from_dict(dict_)
        for key in dict_:
            self.assertEqual(getattr(self.device, key), dict_[key])

    def test_has_additional_attributes(self):
        attributes = ["name", "type", "xmlid", "access"]
        for attribute in attributes:
            with self.subTest(attribute=attribute):
                self.assertTrue(hasattr(self.device, attribute))
