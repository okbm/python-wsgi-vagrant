vagrant fabric
====
vagrantをfabricでセットアップしてみる

## Description

| インストール | version |
|:-----------|:------------|
| mysql      |5.5.41|
| python     |3.4.0|

## Requirement

以下をインストール(macのみでしか検証してません！！)

- virualbox
  - [Downloads – Oracle VM VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- vagrant
  - [Download Vagrant - Vagrant](https://www.vagrantup.com/downloads.html)
- fabric

```
$ easy_install pip
$ pip install fabric cuisine
$ pip install paramiko==1.10
```

## Install

```
$ vagrant up
$ fab main
```

