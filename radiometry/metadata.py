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
    attr : :class:`None`
        Short description

    """
