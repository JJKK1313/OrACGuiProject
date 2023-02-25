# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomACDialogBoxvctqcn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_CustomACDialogBox(object):
    def setupUi(self, CustomACDialogBox):
        if not CustomACDialogBox.objectName():
            CustomACDialogBox.setObjectName(u"CustomACDialogBox")
        CustomACDialogBox.resize(746, 300)
        self.verticalLayout = QVBoxLayout(CustomACDialogBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(CustomACDialogBox)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"#frame{\n"
"background-color: rgb(169, 208, 255);\n"
"}\n"
"\n"
"\n"
"#frame QLabel#label\n"
"{\n"
"	font: 16pt \"Times New Roman\";\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.line = QFrame(CustomACDialogBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.frame_2 = QFrame(CustomACDialogBox)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"background-color: rgb(224, 237, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.nameFrame = QFrame(self.frame_2)
        self.nameFrame.setObjectName(u"nameFrame")
        self.nameFrame.setStyleSheet(u"QLabel#label_3\n"
"{\n"
"	font: 16pt \"Times New Roman\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#nameFrame QPushButton\n"
"{\n"
"	font: 15pt \"Times New Roman\";\n"
"	font-color: black;\n"
"	background: rgb(183, 230, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"#nameFrame QPushButton::hover\n"
"{\n"
"	background: rgb(183, 230, 0);\n"
"}\n"
"\n"
"#nameFrame QPushButton::pressed\n"
"{\n"
"	background: rgb(100, 150, 0);\n"
"}\n"
"")
        self.nameFrame.setFrameShape(QFrame.StyledPanel)
        self.nameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.nameFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.label_3 = QLabel(self.nameFrame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.CustomizeBrandNameLineEdit = QLineEdit(self.nameFrame)
        self.CustomizeBrandNameLineEdit.setObjectName(u"CustomizeBrandNameLineEdit")

        self.verticalLayout_3.addWidget(self.CustomizeBrandNameLineEdit, 0, Qt.AlignTop)

        self.DoneNameGivingPushButton = QPushButton(self.nameFrame)
        self.DoneNameGivingPushButton.setObjectName(u"DoneNameGivingPushButton")

        self.verticalLayout_3.addWidget(self.DoneNameGivingPushButton)


        self.horizontalLayout.addWidget(self.nameFrame, 0, Qt.AlignLeft)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line_2)

        self.recordingFrame = QFrame(self.frame_2)
        self.recordingFrame.setObjectName(u"recordingFrame")
        self.recordingFrame.setStyleSheet(u"QLabel#commandLabel\n"
"{\n"
"	font: 16pt \"Times New Roman\";\n"
"	color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QLabel#instructionsLabel\n"
"{\n"
"	font: 12pt \"Times New Roman\";\n"
"}")
        self.recordingFrame.setFrameShape(QFrame.StyledPanel)
        self.recordingFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.recordingFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.commandLabel = QLabel(self.recordingFrame)
        self.commandLabel.setObjectName(u"commandLabel")

        self.verticalLayout_5.addWidget(self.commandLabel, 0, Qt.AlignHCenter)

        self.instructionsLabel = QLabel(self.recordingFrame)
        self.instructionsLabel.setObjectName(u"instructionsLabel")
        self.instructionsLabel.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.instructionsLabel)


        self.horizontalLayout.addWidget(self.recordingFrame)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line_3)

        self.finishFrame = QFrame(self.frame_2)
        self.finishFrame.setObjectName(u"finishFrame")
        self.finishFrame.setStyleSheet(u"QLabel#label_4\n"
"{\n"
"	font: 20pt \"Times New Roman\";\n"
"}\n"
"")
        self.finishFrame.setFrameShape(QFrame.StyledPanel)
        self.finishFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.finishFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.label_4 = QLabel(self.finishFrame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.finishFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"#frame_6 QPushButton\n"
"{\n"
"	font: 15pt \"Times New Roman\";\n"
"	font-color: black;\n"
"	background: rgb(183, 230, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"#frame_6 QPushButton::hover\n"
"{\n"
"	background: rgb(183, 230, 0);\n"
"}\n"
"\n"
"#frame_6 QPushButton::pressed\n"
"{\n"
"	background: rgb(100, 150, 0);\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SavePushButton = QPushButton(self.frame_6)
        self.SavePushButton.setObjectName(u"SavePushButton")

        self.horizontalLayout_2.addWidget(self.SavePushButton)

        self.ExitPushButton = QPushButton(self.frame_6)
        self.ExitPushButton.setObjectName(u"ExitPushButton")

        self.horizontalLayout_2.addWidget(self.ExitPushButton)


        self.verticalLayout_4.addWidget(self.frame_6, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.finishFrame)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(CustomACDialogBox)

        QMetaObject.connectSlotsByName(CustomACDialogBox)
    # setupUi

    def retranslateUi(self, CustomACDialogBox):
        CustomACDialogBox.setWindowTitle(QCoreApplication.translate("CustomACDialogBox", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("CustomACDialogBox", u"Set New AC Device", None))
        self.label_3.setText(QCoreApplication.translate("CustomACDialogBox", u"Device Brand Name", None))
        self.DoneNameGivingPushButton.setText(QCoreApplication.translate("CustomACDialogBox", u"Done", None))
        self.commandLabel.setText(QCoreApplication.translate("CustomACDialogBox", u"ON", None))
        self.instructionsLabel.setText(QCoreApplication.translate("CustomACDialogBox", u"Please wait for the green light", None))
        self.label_4.setText(QCoreApplication.translate("CustomACDialogBox", u"Done!", None))
        self.SavePushButton.setText(QCoreApplication.translate("CustomACDialogBox", u"Save", None))
        self.ExitPushButton.setText(QCoreApplication.translate("CustomACDialogBox", u"Exit", None))
    # retranslateUi

