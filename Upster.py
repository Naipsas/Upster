#!/usr/bin/python3.5
# -*- coding: iso-8859-1 -*-
#
# Naipsas (Btc Sources)
#
# Upster Project - GitHub
#

# import pygame as pg
import os
import sys

# from Module import function
from Classes.View import View
from Classes.Model import Model

if __name__ == "__main__":

  try:

    GuiManager = View()
    ModelManager = Model()

    # Creamos la interfaz gráfica
    view = GuiManager.createMainWindow()

    # Adjuntamos la lógica

    # Ponemos la interfaz en funcionamiento
    GuiManager.startWindowWorking()

  except Exception as e:

    print(str(e))