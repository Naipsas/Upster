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

import tkinter as tk

from Classes.Controller import Controller

if __name__ == "__main__":

  try:

    parent = tk.Tk()
    # parent.withdraw()

    app = Controller(parent)

    parent.mainloop()

  except Exception as e:

    print(str(e))