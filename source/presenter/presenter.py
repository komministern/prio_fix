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

import logging
# from re import escape
import sys
import os

from PySide6 import QtCore, QtGui, QtWidgets

from ..view.aboutwidget import AboutWidget
from ..view.helpwidget import HelpWidget

logger = logging.getLogger(__name__)

class MyPresenter(QtCore.QObject):

    def __init__(self, model, view, app):
        super(MyPresenter, self).__init__()

        # Store view, model and app.
        self.model = model
        self.view = view
        self.app = app

        self.connectSignals()

        # The following hack decides the current working directory. If the app is run as a bundled
        # PyInstaller executable, the cwd is given by the _MEIPASS attribute at runtime.
        if hasattr(sys, '_MEIPASS'):
            cwd = sys._MEIPASS
        else:
            cwd = os.path.abspath('.')

        self.resources_path = os.path.join(cwd, 'resources')
        self.template_path = os.path.join(self.resources_path, 'Mall Användarregistrering-1.98')

        from os.path import expanduser
        self.user_path = expanduser("~")

        icon_path = os.path.join(self.resources_path, 'uffe2square.ico')
        icon = QtGui.QIcon(icon_path)
        self.view.setWindowIcon(icon)

        pixmap_path = os.path.join(self.resources_path, 'uffe2.png')
        pixmap = QtGui.QPixmap()
        pixmap.load(pixmap_path)
        self.view.label.setPixmap(pixmap)

        self.aboutwidget = AboutWidget(icon)
        self.helpwidget = HelpWidget(icon)


    def connectSignals(self):
        """
            Here we connect the signals from both Model and View to methods in the
            Presenter object.
        """
        # The quit signal is emitted when the user closes the window.
        self.view.myQuitSignal.connect(self.quit)

        self.view.label.click.connect(self.dostuff)

        self.view.aboutAction.triggered.connect(self.about)
        self.view.helpAction.triggered.connect(self.help)


    def quit(self):
        """
            This method should always be called when exiting the app. If data needs
            to be saved, or the user needs to be asked for some action prior to exiting,
            here is where it should happen.
        """

        # Fix things that need to be done from Presenter here (such as interactions with
        # the user regarding saving data before quitting for example).

        # Then we call the Model objects quit function, in case the Model needs to do some
        # cleanup before quitting.
        self.model.quit()

        # This line exits the application.
        QtWidgets.QApplication.quit()


    def dostuff(self):

        ok = True

        path_to_file, _ = QtWidgets.QFileDialog.getOpenFileName(self.view, "Ladda PRIO-export", self.user_path, "Exceldokument (*.xlsx)")

        if path_to_file:

            try:
            
                self.model.collect_data_from_rows(path_to_file)
                self.model.process_row_data()
            
            except Exception as e:
                
                ok = False
                print(e)

                tmpMsg = QtWidgets.QMessageBox(self.view) # for simple msg that no need for translation
                tmpMsg.setIcon(QtWidgets.QMessageBox.Critical)
                tmpMsg.setWindowTitle("Fel")
                tmpMsg.setText('Något gick fel med den valda filen.')
                tmpMsg.addButton("OK",QtWidgets.QMessageBox.YesRole)
                tmpMsg.exec_()

        if ok and path_to_file:

            path_to_file, _ = QtWidgets.QFileDialog.getSaveFileName(self.view, "Spara Användarregistrering (v1.98)", self.user_path, "Exceldokument (*.xlsx)")

            if path_to_file:

                try:
                    
                    nbr_of_posts, suspect_posts, nbr_of_files = self.model.create_registration_from_template(path_to_file)

                    if nbr_of_files > 1:
                        msg = 'Resultatet blev %d filer med totalt %d elevposter. Osäkra konverteringar: %d' % (nbr_of_files, nbr_of_posts, suspect_posts)
                    else:
                        msg = 'Resultatet blev en fil med totalt %d elevposter. Osäkra konverteringar: %d' % (nbr_of_posts, suspect_posts)
                    
                    tmpMsg = QtWidgets.QMessageBox(self.view) # for simple msg that no need for translation
                    tmpMsg.setIcon(QtWidgets.QMessageBox.Information)
                    tmpMsg.setWindowTitle("Information")
                    tmpMsg.setText(msg)
                    tmpMsg.addButton("OK",QtWidgets.QMessageBox.YesRole)
                    tmpMsg.exec_()

                except Exception as e:
                
                    print(e)

                    tmpMsg = QtWidgets.QMessageBox(self.view) # for simple msg that no need for translation
                    tmpMsg.setIcon(QtWidgets.QMessageBox.Critical)
                    tmpMsg.setWindowTitle("Fel")
                    tmpMsg.setText('Något gick fel när filen skulle sparas.')
                    tmpMsg.addButton("OK",QtWidgets.QMessageBox.YesRole)
                    tmpMsg.exec_()


    def about(self):
        self.aboutwidget.show()

    def help(self):
        self.helpwidget.show()
        