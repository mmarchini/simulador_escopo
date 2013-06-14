#!/usr/bin/env python
#encoding=utf-8

'''
    DONT TOUCH THIS FILE, UNLESS YOU KNOW WHAT YOU ARE DOING !!!
'''
import os

try:
    from gi.repository import Gtk
except:
    print u"Não é possível instalar o PyGtk utilizando setuptools no Linux. \nPor favor, instale o pagote 'gobject-introspection' utilizando o gerênciador de pacotes da sua distribuição para poder continuar."
    exit()

from setuptools import setup
setup(name="simesc",install_requires=["functional>0"])

