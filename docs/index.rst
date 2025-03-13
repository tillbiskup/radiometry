==========
radiometry
==========

*Reproducible and automated processing and analysis of (synchrotron) radiometry data based on the ASpecD framework.*

Welcome! This is the documentation for radiometry, a Python package for **processing and analysing (synchrotron) radiometry data** in a **reproducible** and mostly **automated** fashion. Currently, it focusses on data obtained at one of the beamlines at **BESSY-II or MLS in Berlin**, mostly operated by the German National Metrology Institute, the `Physikalisch-Technische Bundesanstalt (PTB) <https://www.ptb.de/>`_.

Due to inheriting from the `ASpecD framework <https://www.aspecd.de/>`_, all data generated with the radiometry package are **completely reproducible** and have a complete history.


Features
========

A list of (planned) features:

* Generalised data model for (synchrotron) radiometry data

* A growing list of general-purpose processing and analysis steps


And to make it even more convenient for users and future-proof:

* Open source project written in Python (>= 3.9)

* Developed fully test-driven

* Extensive user and API documentation



.. warning::
    radiometry is currently under active development and still considered in Beta development state. Therefore, expect frequent changes in features and public APIs that may break your own code. Nevertheless, feedback as well as feature requests are highly welcome.


Installation
============

To install the radiometry package on your computer (sensibly within a Python virtual environment), open a terminal (activate your virtual environment), and type in the following:

.. code-block:: bash

    pip install radiometry


Related projects
================

There is a number of related packages users of the radiometry package may well be interested in, as they have a similar scope, focussing on scientific data analysis and reproducible research.

* `ASpecD <https://docs.aspecd.de/>`_

  A Python framework for the analysis of spectroscopic data focussing on reproducibility and good scientific practice. The framework the radiometry package is based on, developed by T. Biskup.

* evedataviewer

  A Python package for **graphically inspecting data** contained in EVE files, *i.e.* data **obtained at one of the beamlines at BESSY-II or MLS in Berlin**, mostly operated by the German National Metrology Institute, the `Physikalisch-Technische Bundesanstalt (PTB) <https://www.ptb.de/>`_.

* evedata

  A Python package for **importing (synchrotron) radiometry data** obtained at one of the beamlines at **BESSY-II or MLS in Berlin**, mostly operated by the German National Metrology Institute, the `Physikalisch-Technische Bundesanstalt (PTB) <https://www.ptb.de/>`_.

Finally, don't forget to check out the website on `reproducible research <https://www.reproducible-research.de/>`_ covering in more general terms aspects of reproducible research and good scientific practice.


License
=======

This program is free software: you can redistribute it and/or modify it under the terms of the **GPLv3 License**.


A note on the logo
==================

The logo depicts a synchrotron emitting radiation, with the Python logo in its centre. While the synchrotron part is inspired by the logo used for the `Metrology with Synchrotron Radiation section of the PTB <https://www.ptb.de/cms/en/ptb/fachabteilungen/abt7/ptb-sr.html>`_ and the rights of the Python logo belong to the Python Software Foundation (PSF), the entire logo is copyright T. Biskup.



.. toctree::
   :maxdepth: 2
   :caption: User Manual:
   :hidden:

   audience
   concepts
   usecases
   dataset-structure
   installing

.. toctree::
   :maxdepth: 2
   :caption: Developers:
   :hidden:

   people
   developers
   changelog
   roadmap
   api/index

