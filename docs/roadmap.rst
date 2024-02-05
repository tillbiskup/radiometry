=======
Roadmap
=======

A few ideas how to develop the project further, currently a list as a reminder for the main developers themselves, in no particular order, though with a tendency to list more important aspects first:


For version 0.1
===============

* Dataset structure for general :class:`radiometry.dataset.EveDataset`

  * Idea: Get access to all information possibly contained in the eve HDF5 files, so that eve users know better what would be available to them. Ideally, this will positively influence further eve development.

  * As a next step after the dataset structure has been created, the evedataviewer GUI needs to be able to display all this information in a somewhat sensible way.

* Importer for eve HDF5 files

  * For the time being based on ``evefile``?

    * How to deal with Windows/macOS compatibility?

  * Consolidate fill modes for data: which ones are actually useful?

    * In a data model that does both, importing the actual data and filling only on demand afterwards, the information which data are actually contained in the eveH5 file would be preserved.

* Minimum functionality required for evedataviewer

  * dataset
  * importer
  * plotter
