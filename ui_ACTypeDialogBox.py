# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ACTypeDialogBoxtnZoQJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(318, 122)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"background-color: rgb(169, 208, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"	font: 20pt \"Times New Roman\";\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_2)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame\n"
"{\n"
"	background-color:rgb(224, 237, 255);\n"
"}\n"
"\n"
"#frame QComboBox\n"
"{\n"
"	font: 16pt \"Times New Roman\";\n"
"	font-color: black;\n"
"	background: rgb(183, 230, 255);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"#frame QPushButton\n"
"{\n"
"	font: 16pt \"Times New Roman\";\n"
"	font-color: black;\n"
"	background: rgb(183, 230, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"#frame QPushButton::hover\n"
"{\n"
"	background: rgb(183, 230, 0);\n"
"}\n"
"\n"
"#frame QPushButton::pressed\n"
"{\n"
"	background: rgb(100, 150, 0);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.AcTypesComboBox = QComboBox(self.frame)
        self.AcTypesComboBox.addItem("")
        self.AcTypesComboBox.addItem("")
        self.AcTypesComboBox.addItem("")
        self.AcTypesComboBox.setObjectName(u"AcTypesComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AcTypesComboBox.sizePolicy().hasHeightForWidth())
        self.AcTypesComboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.AcTypesComboBox)

        self.DonePushButton = QPushButton(self.frame)
        self.DonePushButton.setObjectName(u"DonePushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DonePushButton.sizePolicy().hasHeightForWidth())
        self.DonePushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.DonePushButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Choose AC Protocol", None))
        self.AcTypesComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Electra", None))
        self.AcTypesComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Samsung", None))
        self.AcTypesComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Customize...", None))

        self.DonePushButton.setText(QCoreApplication.translate("Dialog", u"Done", None))
    # retranslateUi

