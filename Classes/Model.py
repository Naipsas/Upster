#!/usr/bin/python3.5
# -*- coding: iso-8859-1 -*-
#
# Naipsas (Btc Sources)
#
# Upster Project - GitHub
#
# Observable class comes from ToyMVC example 
#

import os
import sys
import shutil
import pathlib
import subprocess

from enum import Enum

import numpy as np

## Clases auxiliares -  Enum

class Store_Status(Enum):

  Non = 0
  Trial = 1
  Bought = 2
  Revoked = 3
  Error = 4

class Local_Status(Enum):

  Non = 0
  Downloading = 1
  Installed = 2
  NeedUpdate = 3
  Error = 4

class Observable():

  def __init__(self, initialValue=None):
    self.data = initialValue
    self.callbacks = {}

  def addCallback(self, func):
    self.callbacks[func] = 1

  def delCallback(self, func):
    del self.callbacks[func]

  def __doCallbacks(self):
    for func in self.callbacks:
      func(self.data)

  def set(self, data):
    self.data = data
    self.__doCallbacks()

  def get(self):
    return self.data

  def unset(self):
    self.data = None


# Esta clase no reconoce información nueva, trabaja con la que tiene
class Application():

  def __init__(self, name, size, categories, store_status, local_status):

    # Python script name
    self.__name = name
    # Tamaño en MB
    self.__size = size
    # Categorías
    self.__categories = categories
    # Estado de la aplicación en al tienda
    self.__store_status = store_status
    # Estado de la aplicación en local
    self.__local_status = local_status

  def getName(self):
    return self.__name

  # Devuelve el tamaño en MB
  def getSize(self):
    return self.__size

  # Devuelve las categorías a las que pertenece la app
  def getCategories(self):
    return self.__categories

  # Devuelve el estado en la tienda
  def getStoreStatus(self):
    return self.__store_status

  # Devuelve el estado en el equipo local
  def getLocalStatus(self):
    return self.__local_status

  ## Funciones de ejecución ##

  # Ejecuta la aplicación
  def run(self, path, args):

    if self.__local_status == Local_Status.Installed:
      os.system(path + "/" + name + " " + path)

  # Elimina la aplicación en local
  def uninstall(self, path):

    if self.__local_status != Local_Status.Non:
      shutil.rmtree(path)
      res = True
    else:
      res = False
      
    return res


class Store():

  __applications = []


class Library():

  __applications = []


  def __init__(self, root_path):

    # Reconocemos las aplicaciones instaladas en la carpeta
    apps = self.getApps(root_path)

    # Las añadimos
    for item in apps:
      __applications.append(item)

  # Trunca a 2 decimales el número que se le proporciona
  def __truncateSize(self, target):
    decade = 10 ** 2
    return np.trunc(target * decade) / decade

  # Tamaño de una app en MB
  def __calculateAppSize(self, folder = "."):

    total_size = 0

    for dirpath, dirnames, filenames in os.walk(folder):

      for f in filenames:

        fp = os.path.join(dirpath, f)
        total_size += os.path.getsize(fp)

    total_size = float(total_size)
    total_size /= (1024 ** 2)
    total_size = self.__truncateSize(total_size)

    return total_size


  # Identifica el estado de una app instalada
  def __IdentifyLocalAppStatus(self, path, name):

    result = subprocess.run([path + "/" + name + ".py", "-status"], stdout=subprocess.PIPE)
    result = result.stdout.decode("iso-8859-1")

    if result == "NeedUpdate":
      res = Local_Status.NeedUpdate
    elif result == "Installed":
      res = Local_Status.Installed
    else:
      res = Error

    return res


  # Identifica el estado de una app en la tienda/servidor
  def __askStoreStatus(self, name):

    pass


  # Identifica las categorías de una app en la tienda/servidor
  def __askStoreCategories(self, name):

    pass


  # Lista todas las aplicaciones encontradas con sus características
  def getApps(self, root_path):

    paths = os.listdir(root_path)
    result = []

    for item in paths:

      path = os.path.join(root_path, item)
      app = []

      if os.path.isdir(path):

        # name, size, categories, store_status, local_status
        app.append(item)
        app.append(self.__calculateAppSize(path))
        print("App " + item + " size: " + str(app[1]) + " MB")
        app.append(self.__askStoreCategories(item))
        # app.append(self.__askStoreStatus(item))
        # app.append(self.__IdentifyLocalAppStatus(root_path, item))
        
    return result


class Model():

  def __init__(self):

    root_path = os.path.realpath(sys.argv[0]).replace(sys.argv[0], "")
    library_path = root_path + "library"

    pathlib.Path(library_path).mkdir(exist_ok=True)

    # Inicializa la tienda y la biblioteca
    self.__library = Library(library_path)
    self.__store = Store()
