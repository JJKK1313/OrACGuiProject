# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'removeACDialogBoxiTIcOc.ui'
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
        Dialog.resize(279, 196)
        Dialog.setStyleSheet(u"#frame_3 QPushButton\n"
                             "{\n"
                             "	font: 12pt \"Times New Roman\";\n"
                             "}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
                                 "	background-color: rgb(169, 208, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "	font: 16pt \"Times New Roman\";\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.frame)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"#frame_2{\n"
                                   "	background-color: rgb(224, 237, 255);\n"
                                   "}\n"
                                   "QCheckBox{\n"
                                   "	font: 16pt \"Times New Roman\";\n"
                                   "}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ac4ChkBx = QCheckBox(self.frame_2)
        self.ac4ChkBx.setObjectName(u"ac4ChkBx")

        self.gridLayout.addWidget(self.ac4ChkBx, 1, 1, 1, 1)

        self.ac1ChkBx = QCheckBox(self.frame_2)
        self.ac1ChkBx.setObjectName(u"ac1ChkBx")

        self.gridLayout.addWidget(self.ac1ChkBx, 0, 0, 1, 1)

        self.ac2ChkBx = QCheckBox(self.frame_2)
        self.ac2ChkBx.setObjectName(u"ac2ChkBx")

        self.gridLayout.addWidget(self.ac2ChkBx, 0, 1, 1, 1)

        self.ac3ChkBx = QCheckBox(self.frame_2)
        self.ac3ChkBx.setObjectName(u"ac3ChkBx")

        self.gridLayout.addWidget(self.ac3ChkBx, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3{\n"
                                   "	background-color: rgb(206, 231, 255);\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "#frame_3 QPushButton\n"
                                   "{\n"
                                   "	font: 15pt \"Times New Roman\";\n"
                                   "	font-color: black;\n"
                                   "	background: rgb(183, 230, 255);\n"
                                   "	border-radius: 10px;\n"
                                   "	border: 1px solid;\n"
                                   "}\n"
                                   "\n"
                                   "#frame_3 QPushButton::hover\n"
                                   "{\n"
                                   "	background: rgb(183, 230, 0);\n"
                                   "}\n"
                                   "\n"
                                   "#frame_3 QPushButton::pressed\n"
                                   "{\n"
                                   "	background: rgb(100, 150, 0);\n"
                                   "}\n"
                                   "")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cancelPushBtn = QPushButton(self.frame_3)
        self.cancelPushBtn.setObjectName(u"cancelPushBtn")

        self.horizontalLayout_2.addWidget(self.cancelPushBtn)

        self.okPushBtn = QPushButton(self.frame_3)
        self.okPushBtn.setObjectName(u"okPushBtn")

        self.horizontalLayout_2.addWidget(self.okPushBtn)

        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignBottom)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Choose Which AC to Remove?", None))
        self.ac4ChkBx.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.ac1ChkBx.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.ac2ChkBx.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.ac3ChkBx.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.cancelPushBtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.okPushBtn.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi
