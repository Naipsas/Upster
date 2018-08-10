#!/usr/bin/python3.5
# -*- coding: iso-8859-1 -*-
#
# Naipsas (Btc Sources)
#
# Upster Project - GitHub
#

import os
import sys
import pathlib

from .View import View
from .Model import Model
from .Model import Store
from .Model import Library

class Controller():

  def __init__(self, parent_tk):

    root_path = os.path.realpath(sys.argv[0]).replace(sys.argv[0], "")
    library_path = root_path + "library"

    pathlib.Path(library_path).mkdir(exist_ok=True)

    # Creamos el modelo
    self.model = Model()

    # Añadimos los callbacks: cuando cambian qué valores del modelo se llama a la vista
    self.model.library.addCallback(self.libraryChanged)
    self.model.store.addCallback(self.storeChanged)

    # Creamos la vista
    self.view = View(parent_tk)

    # Añadimos las funciones de la vista, que provocan cambios en el modelo
    

    # Inicializamos. Hay que hacerlo aqui porque en Model todavia no estan los callbacks
    self.model.libraryChanged(Library(library_path))
    # self.model.storeChanged(Store())


  ## Definimos las funciones de control necesarias sobre objetos controlados
  ## con Observable en el modelo

  def libraryChanged(self, library):
    self.view.libraryChanged(library)

  def storeChanged(self, store):
    self.view.storeChanged(store)