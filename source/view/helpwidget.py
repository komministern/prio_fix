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
from PySide6 import QtCore, QtWidgets, QtGui

# from mycommonfunctions import path as mypath
# from mycommonfunctions import basicconfig as myconf

from .ui_help import Ui_Help

# globalvars = myconf.getGlobals()

class HelpWidget(QtWidgets.QWidget, Ui_Help):

    # my_close = QtCore.Signal()

    def __init__(self, icon):
        super(HelpWidget, self).__init__()

        self.setupUi(self)

        self.setWindowIcon(icon)

