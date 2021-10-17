
import os
import shutil

os.system('pyside6-uic ui_mainwindow.ui -o ui_mainwindow.py')
shutil.copyfile('./ui_mainwindow.py', '../source/view/ui_mainwindow.py')

os.system('pyside6-uic about.ui -o ui_about.py')
shutil.copyfile('./ui_about.py', '../source/view/ui_about.py')

os.system('pyside6-uic help.ui -o ui_help.py')
shutil.copyfile('./ui_help.py', '../source/view/ui_help.py')