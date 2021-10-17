"""
Copyright (C) 2021 Oscar Franzén <oscarfranzen@protonmail.com>

This file is part of PRIO-fix Användarregistrering.

PRIO-fix Användarregistrering is free software: you can redistribute 
it and/or modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.

PRIO-fix Användarregistrering is distributed in the hope that it will 
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with GCA Simulator.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import sys
import logging

from PySide6 import QtCore, QtGui, QtWidgets
from .ui_mainwindow import Ui_MainWindow

logger = logging.getLogger(__name__)

class MyView(QtWidgets.QMainWindow, Ui_MainWindow):
    """
        The View object is just a subclassed QMainWindow which contains the all the
        applications widgets. The main window and its contents is created with the 
        Qt Designer application. The ui file is found in the resources directory. 
    """

    myQuitSignal = QtCore.Signal()

    

    def __init__(self):
        super(MyView, self).__init__()

        # The setupUi method sets up the main window as we have laid it out in the Qt Designer.
        self.setupUi(self)

        self.setupMenu()

    def closeEvent(self, event):
        """
            This method overrides the mainwindows closeEvent method, which gets called when 
            the user tries to close the mainwindow. 
        """

        # Ignore the close event. We need to take care of some business before we allow the
        # app to close. (If we had not ignored this event, the window would close immediately.)
        event.ignore()

        # Now we emit our own signal quit. This will be caught by the Presenter which will
        # call its own quit method. There we have full control of what shall happen before
        # exiting the application.
        self.myQuitSignal.emit() 

    def setupMenu(self):
        self.helpAction = QtGui.QAction('PRIO-fix Användarregistrering Hjälp', self)
        self.aboutAction = QtGui.QAction('Om PRIO-fix Användarregistrering', self)
        menubar = self.menuBar()
        about_menu = menubar.addMenu('Hjälp')
        about_menu.addAction(self.helpAction)
        about_menu.addSeparator()
        about_menu.addAction(self.aboutAction)