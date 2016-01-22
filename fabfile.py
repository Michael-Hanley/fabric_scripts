from __future__ import with_statement
from fabric.api import local, execute
from contextlib import contextmanager as _contextmanager
from fabric.context_managers import lcd

"""
This File is meant to be run in two parts. The first is to install the tools necessary to get a virtual environment ready. 

An intermediary step is necessary in that the user needs to manually enter the mkvitualenv command with the
name of the virtual env in order to create and start the virtualenv.

On step two, within the virtual env we will be installing the necessary packages for our python/django environment.
"""

def install_0():
    execute(update)
    execute(git)
    execute(python)
    execute(setup_tools)
    execute(pip)
    execute(edit_vimrc)
    execute(create_virtual)
    execute(messages)

def update():
	local("sudo apt-get update")

def git():
	local("sudo apt-get install git")
	local("git config --global user.name 'Pasquali'")
	local("git config --global user.email 'pasaquali@gmail.com'")

def python():
    local("sudo apt-get install python")

def setup_tools():
    local("sudo apt-get install python-setuptools")

def pip():
    local("sudo apt-get install python-pip python-dev build-essential -y")

def create_virtual():
    local("sudo pip install virtualenv virtualenvwrapper")
    bashrc_dir = '..'
    with lcd(bashrc_dir):
    	local("echo 'export WORKON_HOME=~/.virtualenvs' >> .bashrc")
	local("echo '. /usr/local/bin/virtualenvwrapper.sh' >> .bashrc")
    
def edit_vimrc():
    vimrc_file = '..'
    with lcd(vimrc_file):
        local("git clone https://github.com/amix/vimrc.git ~/.vim_runtime")
        local("sh ~/.vim_runtime/install_awesome_vimrc.sh")

def messages():
    local("echo '. ~/.bashrc'")
    local("")
    local("echo do not forget to begin a virtualenv before starting part 2")
    local("")
    local("echo do not forget to edit vim.rc")


"""
Step two

Packages to be install inside the virtual env.

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


