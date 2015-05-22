# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.decorators import task
from fabric.contrib import files
from fabric.colors import red, green
from cuisine import run
import cuisine

env.hosts = ['vagrant@192.168.56.101']
#env.key_filename = ['~/.ssh/id_rsa']
#env.port = 2222

env.user = 'vagrant'
env.password = 'vagrant'
env.forward_agent = True

@task
def update_packages():
    puts(green('update packages'))
    sudo("apt-get update")

# 使いそうなツール
@task
def setup_devtools():
    puts(green('Installing Devtools'))
    packages = '''
        vim curl wget build-essential tmux screen zsh make sqlite3 tig tree locate git-core python-software-properties unzip
        '''.split()

    for pkg in packages:
        cuisine.package_ensure(pkg)

# アプリケーション
@task
def setup_packages():
    puts(green('Installing Packages'))

    packages = '''
        libssl-dev libreadline-dev libsqlite3-dev python-pip
        '''.split()

    for pkg in packages:
        cuisine.package_ensure(pkg)

    # python 3.4 install
    run('wget https://www.python.org/ftp/python/3.4.1/Python-3.4.1.tar.xz')
    run('tar xvf Python-3.4.1.tar.xz && rm -f Python-3.4.1.tar.xz')
    run('mkdir -p $HOME/local')
    with cd('Python-3.4.1'):
        run('./configure --prefix=$HOME/local/python-3.4')
        run('make')
        run('make install')

    sudo('rm -rf Python-3.4.1')

    sudo('pip install virtualenv')
    sudo('virtualenv $HOME/local/python3')
    run('source $HOME/local/python3/bin/activate')
    sudo('pip install ipython')

    run('echo "export PATH=$HOME/local/python-3.4/bin:$PATH" >> $HOME/.bashrc')

    # other
    cuisine.package_ensure('mysql-server-5.5')

    # pythonを動かすためにいろいろ
    packages = '''
        uwsgi uwsgi-plugin-python nginx
        '''.split()

    for pkg in packages:
        cuisine.package_ensure(pkg)

@task
def restart_application():
    puts(green('Restarting application'))

@task
def main():
    update_packages()
    setup_devtools()
    setup_packages()
    restart_application()

    puts(green('finish script'))
