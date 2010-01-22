============
project-base
============

project-base is a source tree which I use for new Django sites. It includes a few scripts which makes setup easier, and some commonly-used components, such as JQuery and 960.gs. The settings.py file has been modified to suit my own conventions.

Usage
=====

#. Checkout the repository

	git@github.com:jonatkinson/project-base.git

#. Rename the top level folder as appropriate for the name of your project.

#. Run the ./bootstrap.sh script. This will install all the files from the requirements.txt file.

#. Change the git origin as appropriate.

Other Stuff
===========

#. You can run ./requirements.sh at any time to install all the packages in ./requirements.txt.

#. There is a very basic Fabfile for really simple deployments. It's designed to work with a Debian Lighttpd installation.