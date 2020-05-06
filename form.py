# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custom_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_Dialog(object):
    # TODO implement more complex GUI so that no additional XML modifications are required after creation 
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 149)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rbColor = QtWidgets.QRadioButton(Dialog)
        self.rbColor.setChecked(True)
        self.rbColor.setObjectName("rbColor")
        self.horizontalLayout_3.addWidget(self.rbColor)
        self.rbImage = QtWidgets.QRadioButton(Dialog)
        self.rbImage.setObjectName("rbImage")
        self.horizontalLayout_3.addWidget(self.rbImage)
        self.rbText = QtWidgets.QRadioButton(Dialog)
        self.rbText.setObjectName("rbText")
        self.horizontalLayout_3.addWidget(self.rbText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbLog = QtWidgets.QCheckBox(Dialog)
        self.cbLog.setObjectName("cbLog")
        self.horizontalLayout_2.addWidget(self.cbLog)
        self.cbPub = QtWidgets.QCheckBox(Dialog)
        self.cbPub.setObjectName("cbPub")
        self.horizontalLayout_2.addWidget(self.cbPub)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.rbColor.setText(_translate("Dialog", "Color"))
        self.rbImage.setText(_translate("Dialog", "Image"))
        self.rbText.setText(_translate("Dialog", "Text"))
        self.label.setText(_translate("Dialog", "ID"))
        self.cbLog.setText(_translate("Dialog", "Logging"))
        self.cbPub.setText(_translate("Dialog", "Publish via API"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

class InputDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

    def getAnalyzer(self, dimension):
        if(self.ui.rbColor.isChecked()):
            analyzerType = "colorAnalyser"
        if(self.ui.rbImage.isChecked()):
            analyzerType = "imageAnalyser"
        if(self.ui.rbText.isChecked()):
            analyzerType = "textAnalyser"
        analyzerId = self.ui.lineEdit.text()
        log = self.ui.cbLog.isChecked()
        pub = self.ui.cbPub.isChecked()
        return Analyzer(analyzerType, analyzerId, dimension, log, pub)

class Analyzer():
    def __init__(self, analyzerType, analyzerId, dimension, log=False, pub=False):
        self.analyzerType = analyzerType
        self.analyzerId = analyzerId
        self.dimension = dimension
        self.log = log
        self.pub = pub

    def __str__(self):
        return """Analyzer Type: {o.analyzerType}
        Analyzer Id: {o.analyzerId}
        Dimension: {o.dimension}
        Log: {o.log}
        Pub: {o.pub}""".format(o=self)