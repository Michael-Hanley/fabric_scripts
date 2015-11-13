from __future__ import with_statement
from fabric.api import local, execute
from contextlib import contextmanager as _contextmanager
from fabric.context_managers import lcd

def install():
    execute(python)
    execute(pip)
    execute(django)
    execute(virt_env)
    execute(apache)
    execute(setup_tools)
    execute(create_virtual)
    execute(start_django_proj)

def python():
    local("sudo apt-get install python")

def pip():
    local("sudo apt-get install python-pip python-dev build-essential ")

def django():
    local("sudo pip install Django")

def virt_env():
    local("sudo pip install virtualenv")

def apache():
    local("sudo apt-get install apache2")

def setup_tools():
    local("sudo apt-get install python-setuptools")

def create_virtual():
    local("virtualenv --no-site-packages project")

def start_django_proj():
    code_dir = 'project'
    with lcd(code_dir):
        local("django-admin.py startproject myproject")
