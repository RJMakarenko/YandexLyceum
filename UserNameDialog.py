# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UserNameDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_input_dialog(object):
    def setupUi(self, user_input_dialog):
        user_input_dialog.setObjectName("user_input_dialog")
        user_input_dialog.setWindowModality(QtCore.Qt.WindowModal)
        user_input_dialog.resize(399, 134)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(user_input_dialog.sizePolicy().hasHeightForWidth())
        user_input_dialog.setSizePolicy(sizePolicy)
        user_input_dialog.setMinimumSize(QtCore.QSize(399, 134))
        user_input_dialog.setMaximumSize(QtCore.QSize(399, 134))
        self.buttonBox = QtWidgets.QDialogButtonBox(user_input_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(user_input_dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.user_name_edit = QtWidgets.QLineEdit(user_input_dialog)
        self.user_name_edit.setGeometry(QtCore.QRect(20, 50, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user_name_edit.setFont(font)
        self.user_name_edit.setObjectName("user_name_edit")

        self.retranslateUi(user_input_dialog)
        self.buttonBox.accepted.connect(user_input_dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(user_input_dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(user_input_dialog)

    def retranslateUi(self, user_input_dialog):
        _translate = QtCore.QCoreApplication.translate
        user_input_dialog.setWindowTitle(_translate("user_input_dialog", "Представьтесь, пожалуйста"))
        self.label.setText(_translate("user_input_dialog", "Введите Ваше имя:"))
