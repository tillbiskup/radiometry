=================
Dataset structure
=================

The dataset is an essential :doc:`concept <concepts>` of the ASpecD framework and in turn the radiometry package, as it abstracts the different vendor formats and combines both, numerical data and metadata, in an easily accessible way. Even more, the general structure of a dataset allows to compare data of entirely different origin (read: spectroscopic method), as long as their axes are compatible.

Developers of the radiometry package frequently need to get an overview of the structure of the dataset and its different subclasses. Whereas the API documentation of each class provides a lot of information, a simple and accessible presentation of the dataset structure is often what is needed.

Therefore, the structure of each of the dataset classes is provided below in YAML format, automatically generated from the actual source code.


eve dataset
===========

Entity containing both, numerical data as well as the corresponding metadata that represent all possible contents of an eve HDF5 file. For implementation details, see the API documentation of :class:`radiometry.dataset.EveDataset` and :class:`radiometry.metadata.EveDatasetMetadata`.

.. literalinclude:: EveDataset.yaml
   :language: yaml


DeviceData
----------

Device data are a subclass of :class:`aspecd.dataset.Data` containing additional metadata. Device data are stored as a dictionary in the dataset structure, where the keys refer to the "name" of the respective device, and the values are instances of the :class:`radiometry.dataset.DeviceData` class. Therefore, the structure of the :class:`radiometry.dataset.DeviceData` class is not visible in the dataset structure shown above, but documented below:

.. literalinclude:: DeviceData.yaml
   :language: yaml
