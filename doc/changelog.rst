Release Notes
=============

Release Version 1.3
-------------------

Re-running the same simulation with the same seed on the same python version should now be deterministic, 
at least for the most common options. 
As sets and dictionaries have arbitrary order, this was not the case previously.


Release Version 1.2
-------------------

Additional fixes. Tested with Python 3.11

Release Version 1.1
-------------------

Python3 Support. Tested with Python 3.10

Release Version 1.0
-------------------

The main script is now called `ernwin.py`

Release Version 0.1
-------------------

For this release, some non-core parts of the ernwin program have been restructured.
Therefore most files in fess/scripts are outdated and do not work.
The only tested script is `ernwin_new.py`

Changes from earlier versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*  Use ernwin_new.py instead of ernwin_go.py
