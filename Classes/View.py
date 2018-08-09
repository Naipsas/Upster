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

class View:

  def __init__(self):
    pass


  ### Funciones generales - Invocadas fuera ###
  def createMainWindow(self):

    self.top = self.__createWindow()

    # Creamos cada tab con su contenido
    self.tab = []
    # Cada tabla tiene asociado una lista de elementos a emplear
    self.elements = []

    # Tab 1: Store View
    self.tab.append(self.__createTab(self.top))

    # Tab 2: Library View
    self.tab.append(self.__createTab(self.top))

    # Tab 3: Download View
    self.tab.append(self.__createTab(self.top))
    self.tab3_elem = []
    self.tab3_elem.append(self.__createDownloadTreeview(self.tab[2]))

  def insertNewDownload(self, name, category, size):

    

    # Podemos cambiar 0 por "end" para insertarlo al final de la lista
    tree.insert("", "end", text="Upster", values=("Programa", "5MB"))

  def startWindowWorking(self):

    return self.top.mainloop()


  ### Funciones privadas - invocadas por las generales ###
  def __createWindow(self):

    return tk.Tk()

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

    tree.heading("One", text="Categoría")
    tree.heading("Two", text="Tamaño")

    tree.pack()

    return tree

  
