#!/usr/bin/python3.5
# -*- coding: iso-8859-1 -*-
#
# Naipsas (Btc Sources)
#
# Upster Project - GitHub
#

from tkinter import ttk
import tkinter as tk

# from Module import function
# from Classes.File import Class
from .Model import Model
from .Model import Download_Status

class View:

  def __init__(self, parent_tk):

    # Configuramos la venana principal
    self.createMainWindow(parent_tk)

  ### Funciones invocadas por el controlador ###

  def libraryChanged(self, library):

    for item in self.downloadView.get_children():
      self.deleteDownload(item)

    for item in library.getApps():
      self.insertNewDownload(item[0], str(item[1]), str(item[2]))

  ### Creacion de la interfaz ###
  def createMainWindow(self, parent_tk):

    # Creamos cada tab con su contenido
    tab = []

    # Tab 1: Store View
    tab.append(self.__createTab(parent_tk))
    # Elementos


    # Tab 2: Library View
    tab.append(self.__createTab(parent_tk))
    # Elementos


    # Tab 3: Download View
    tab.append(self.__createTab(parent_tk))
    # Elementos
    self.downloadView = self.__createDownloadTreeview(tab[2])


  def insertNewDownload(self, name, status, size):

    # Podemos cambiar 0 por "end" para insertarlo al final de la lista
    self.downloadView.insert("", "end", text=name, values=(str(status), str(size) + "MB"))

  def deleteDownload(self, download):

    for item in self.downloadView.get_children():

      if item.text == download:

        self.downloadView.delete(item)

  ### Funciones privadas - anteriores ###

  # Parent debe de ser una ventana
  def __createTab(self, parent):
  
    tab = tk.Frame(parent)
    tab.pack()

    return tab

  # Parent debe de ser un frame/tab
  def __createDownloadTreeview(self, parent):

    tree = ttk.Treeview(parent)

    tree["columns"] = ("One", "Two")
    tree.column("One", width=100)
    tree.column("Two", width=100)

    tree.heading("One", text="Estado")
    tree.heading("Two", text="Tamaño")

    tree.pack()

    return tree