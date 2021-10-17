#!/usr/bin/env python

from PyQt4 import QtCore, QtGui, QtSql

import connection


class TableEditor(QtGui.QDialog):
    def __init__(self, tableName, parent=None):
        super(TableEditor, self).__init__(parent)
        hdr = ["NAME","EMAIL ADDRESS","PHONE NUMBER","BIRTHDAY","ADDRESS","PARTICIPATION"]
        if tableName=="att":
          hdr = [ "NAME","PARTICIPATION","FELLDATE","SNO" ]
        if tableName=="prog":
          hdr = ["CONDUCTOR","DATE","TOPIC","SPEAKER","FOCUS","PASSAGE","ADDRESS1","ADDRESS2"]
        if tableName=="ict":
          hdr = ["QNO","INSTRUCTION","QUESTION","CANSWER","ANS","OPT A","OPT_B","OPT_C","OPT_D","OPT_E","DIAG","SYALLBUS","EXAMDATE","LEVEL"]
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable(tableName)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()
        i=0
        for x in hdr:
          self.model.setHeaderData(i, QtCore.Qt.Horizontal, x)
          i+=1

        view = QtGui.QTableView()
        view.setModel(self.model)

        submitButton = QtGui.QPushButton("Submit")
        submitButton.setDefault(True)
        revertButton = QtGui.QPushButton("&Revert")
        quitButton = QtGui.QPushButton("Quit")

        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
        buttonBox.addButton(submitButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(revertButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QtGui.QDialogButtonBox.RejectRole)

        submitButton.clicked.connect(self.submit)
        revertButton.clicked.connect(self.model.revertAll)
        quitButton.clicked.connect(self.close)

        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(view)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("CCYA")

    def submit(self):
        self.model.database().transaction()
        if self.model.submitAll():
            self.model.database().commit()
        else:
            self.model.database().rollback()
            QtGui.QMessageBox.warning(self, "Cached Table",
                        "The database reported an error: %s" % self.model.lastError().text())


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
#    if not connection.createConnection():
#        sys.exit(1)

    editor = TableEditor('names')
    sys.exit(editor.exec_())
