"""
Metadata: Information on numeric data stored in a structured way.

Metadata
========

In this module, the individual metadata classes are defined which contain the
metadata for the different types of datasets:

  * :class:`EveDatasetMetadata`

What may sound like a minor detail is one key aspect of the radiometry package:
The metadata and their structure provide a unified interface for all
functionality operating on datasets. Reproducible research
is only possible if all information necessary is always recorded, and this
starts with all the metadata accompanying a measurement. Defining what kind
of metadata is important and needs to be recorded, together with metadata
formats easily writable by the experimenters *during* recording the data
requires a thorough understanding of both, the method and the setup(s) used.
For an overview of the structures of the dataset classes and their
corresponding metadata, see the :doc:`dataset structure </dataset-structure>`
section.


Module documentation
====================
"""

import aspecd.metadata


class EveDatasetMetadata(aspecd.metadata.ExperimentalDatasetMetadata):
    """
    Set of all metadata for a dataset object representing an eve HDF5 file.

    Metadata as a unified structure of information coupled to the dataset are
    necessary for the understanding, analysis and processing of data.


    Attributes
    ----------
    measurement : :class:`Measurement`
        Metadata of measurement

    """

    def __init__(self):
        super().__init__()
        self.measurement = Measurement()


class Measurement(aspecd.metadata.Measurement):
    """
    General information available for each type of measurement.

    Attributes
    ----------
    location : :class:`str`
        Experimental station the data were obtained

    """

    def __init__(self, dict_=None):
        self.location = ""
        super().__init__(dict_=dict_)


class Device(aspecd.metadata.Device):
    """
    One sentence (on one line) describing the class.

    More description comes here...


    Attributes
    ----------
    name : :class:`str`
        Name of the device

        TODO: What is this name? And how does it differ from :attr:`label`?

    type : :class:`str`
        Device type

        Channel or Axis

        TODO: Needs to become an enum type

    xmlid : :class:`str`
        XML id

        Some more description is necessary.

    access : :class:`str`
        PV name for CA

        Some more description is necessary.

    """

    def __init__(self, dict_=None):
        self.name = ""
        self.type = ""
        self.xmlid = ""
        self.access = ""
        super().__init__(dict_=dict_)
