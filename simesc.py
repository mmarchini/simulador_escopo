#!/usr/bin/env python
#encoding=UTF-8

from simesc.interface import MainWindow
import os
filename = ""

if "-f" in os.sys.argv and len(os.sys.argv) >= (os.sys.argv.index("-f")+1):
    filename = os.sys.argv[os.sys.argv.index("-f")+1]

app = MainWindow(filename = filename)
app.start_main_loop()

