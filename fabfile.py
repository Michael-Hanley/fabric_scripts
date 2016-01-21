from __future__ import with_statement
from fabric.api import local, execute
from contextlib import contextmanager as _contextmanager
from fabric.context_managers import lcd

"""
This File is meant to be run in two parts. The first is to install the tools necessary to get a virtual environment ready. 

An intermediary step is necessary in that the user needs to manually create a new terminal, enter the mkvitualenv command with the name of the virtual env inorder to create and start the virtualenv.

On step two, within the virtual env we will be installing the necessary packages for our python environment.
"""

def install_0():
    execute(update)
    execute(git)
    execute(python)
    execute(setup_tools)
    execute(pip)
    execute(create_virtual)

def update():
	local("apt-get update")

def git():
	local("apt-get install git")
	local("git config --global user.name 'Pasquali'")
	local("git config --global user.email 'pasaquali@gmail.com'")

def python():
    local("apt-get install python")

def setup_tools():
    local("apt-get install python-setuptools")

def pip():
    local("apt-get install python-pip python-dev build-essential ")

def create_virtual():
    local("pip install virtualenv virtualenvwrapper")
    bashrc_dir = '..'
    with lcd(bashrc_dir):
    	local("echo 'export WORKON_HOME=~/.virtualenvs' >> .bashrc")
	local("echo '. /usr/local/bin/virtualenvwrapper.sh' >> .bashrc")
    local("echo Please begin a new terminal window and type mkvirtualenv + the virtualenvs name to begin a virtual env and then run install_1")

"""
Step two
"""

def install_1():
    execute(req_security)
    execute(requests)
    execute(django)
    execute(rest_framework)

def requests():
    local("pip install requests")

def django():
    local("pip install Django")

def rest_framework():
    local("pip install djangorestframework markdown django-filter")

def req_security():
	local("sudo pip install requests[security]")


