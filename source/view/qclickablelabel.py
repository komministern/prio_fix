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

from PySide6 import QtCore, QtGui, QtWidgets

class QClickableLabel(QtWidgets.QLabel):

    click = QtCore.Signal()

    def __init__(self, parent):
        super(QClickableLabel, self).__init__(parent)

    def mousePressEvent(self, event):
        event.ignore()
        self.click.emit()
        # print('KUK')