============
project-base
============

project-base is a source tree which I use for new Django sites. 

It uses pip and virtualenv to install `Django`_, `IPython`_, `flup`_, `MySQL-python`_ and `ipdb`_.

Included is a Django project, which includes `jQuery`_ and `960.gs`_. The settings.py file has been modified to suit my own conventions, and there are some default templates.

Requirements
============

#. bash - I've not tried the shell scripts with any other shell, so if you're not using bash, proceed at your own risk. 

#. virtualenv - The bootstrap script requires virtualenv to complete.

#. pip - The bootstrap script uses pip to install the project dependencies.

Usage
=====

#. Checkout the repository

	git@github.com:jonatkinson/project-base.git

#. Rename the top level folder as appropriate for the name of your project.

#. Run the ./bootstrap.sh script. This will install all the dependencies from the requirements.txt file.

#. Change the git origin as appropriate.

Other Stuff
===========

#. You can run ./requirements.sh at any time to install all the packages in ./requirements.txt.

#. There is a very basic Fabfile for really simple deployments. It's designed to work with a Debian Lighttpd installation.

.. _Django: http://www.djangoproject.com/
.. _IPython: http://ipython.scipy.org/moin/
.. _flup: http://trac.saddi.com/flup
.. _MySQL-python: http://sourceforge.net/projects/mysql-python/
.. _ipdb: http://trac.gotcha.python-hosting.com/file/bubblenet/pythoncode/ipdb/README.txt?format=txt
.. _jQuery: http://jquery.com/
.. _960.gs: http://960.gs/
