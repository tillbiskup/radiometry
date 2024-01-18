import aspecd.utils


class_names = ["EveDataset", "DeviceData"]

for class_name in class_names:
    yaml = aspecd.utils.Yaml()
    dataset = aspecd.utils.object_from_class_name(
        ".".join(["radiometry.dataset", class_name])
    )
    yaml.dict = dataset.to_dict()
    yaml.serialise_numpy_arrays()
    yaml.write_to(".".join([class_name, "yaml"]))
