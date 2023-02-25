# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orACGuiPpXZUm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(595, 224)
        MainWindow.setStyleSheet(u"#TopLabelFrame QLabel\n"
                                 "{\n"
                                 "padding:0;\n"
                                 "margin: 0;\n"
                                 "background:transparent;\n"
                                 "font: 36pt \"Times New Roman\";\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#TopLabelFrame\n"
                                 "{\n"
                                 "	\n"
                                 "	background-color: rgb(169, 208, 255);\n"
                                 "}\n"
                                 "\n"
                                 "#MainPartFrame\n"
                                 "{\n"
                                 "	background-color:rgb(224, 237, 255);\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopLabelFrame = QFrame(self.centralwidget)
        self.TopLabelFrame.setObjectName(u"TopLabelFrame")
        self.TopLabelFrame.setStyleSheet(u"")
        self.TopLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.TopLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.TopLabelFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.HeadlineLabel = QLabel(self.TopLabelFrame)
        self.HeadlineLabel.setObjectName(u"HeadlineLabel")

        self.horizontalLayout.addWidget(self.HeadlineLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addWidget(self.TopLabelFrame, 0, Qt.AlignTop)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.MainPartFrame = QFrame(self.centralwidget)
        self.MainPartFrame.setObjectName(u"MainPartFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainPartFrame.sizePolicy().hasHeightForWidth())
        self.MainPartFrame.setSizePolicy(sizePolicy)
        self.MainPartFrame.setStyleSheet(u"")
        self.MainPartFrame.setFrameShape(QFrame.StyledPanel)
        self.MainPartFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.MainPartFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.MainPartFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"#frame QPushButton\n"
                                 "{\n"
                                 "	font: 19pt \"Times New Roman\";\n"
                                 "	font-color: black;\n"
                                 "	background: rgb(183, 230, 255);\n"
                                 "	border-radius: 20px;\n"
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
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ac1PushBtn = QPushButton(self.frame)
        self.ac1PushBtn.setObjectName(u"ac1PushBtn")
        self.ac1PushBtn.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ac1PushBtn.sizePolicy().hasHeightForWidth())
        self.ac1PushBtn.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.ac1PushBtn, 0, 0, 1, 1)

        self.ac2PushBtn = QPushButton(self.frame)
        self.ac2PushBtn.setObjectName(u"ac2PushBtn")
        self.ac2PushBtn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.ac2PushBtn.sizePolicy().hasHeightForWidth())
        self.ac2PushBtn.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.ac2PushBtn, 0, 1, 1, 1)

        self.ac3PushBtn = QPushButton(self.frame)
        self.ac3PushBtn.setObjectName(u"ac3PushBtn")
        self.ac3PushBtn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.ac3PushBtn.sizePolicy().hasHeightForWidth())
        self.ac3PushBtn.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.ac3PushBtn, 1, 0, 1, 1)

        self.ac4PushBtn = QPushButton(self.frame)
        self.ac4PushBtn.setObjectName(u"ac4PushBtn")
        self.ac4PushBtn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.ac4PushBtn.sizePolicy().hasHeightForWidth())
        self.ac4PushBtn.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.ac4PushBtn, 1, 1, 1, 1)

        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.MainPartFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton\n"
                                   "{\n"
                                   "	font: 12pt \"Times New Roman\";\n"
                                   "	font-color: black;\n"
                                   "	background: rgb(183, 230, 255);\n"
                                   "	border-radius: 20px;\n"
                                   "	border: 1px solid;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::hover\n"
                                   "{\n"
                                   "	background: rgb(183, 230, 0);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::pressed\n"
                                   "{\n"
                                   "	background: rgb(100, 150, 0);\n"
                                   "}\n"
                                   "")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addAcPushBtn = QPushButton(self.frame_2)
        self.addAcPushBtn.setObjectName(u"addAcPushBtn")
        sizePolicy2.setHeightForWidth(self.addAcPushBtn.sizePolicy().hasHeightForWidth())
        self.addAcPushBtn.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.addAcPushBtn)

        self.removeAcPushBtn = QPushButton(self.frame_2)
        self.removeAcPushBtn.setObjectName(u"removeAcPushBtn")
        sizePolicy2.setHeightForWidth(self.removeAcPushBtn.sizePolicy().hasHeightForWidth())
        self.removeAcPushBtn.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.removeAcPushBtn)

        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignRight)

        self.verticalLayout.addWidget(self.MainPartFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.HeadlineLabel.setText(QCoreApplication.translate("MainWindow", u"Hello, Ready To Start!", None))
        self.ac1PushBtn.setText(QCoreApplication.translate("MainWindow", u"AC 1", None))
        self.ac2PushBtn.setText(QCoreApplication.translate("MainWindow", u"AC 2", None))
        self.ac3PushBtn.setText(QCoreApplication.translate("MainWindow", u"AC 3", None))
        self.ac4PushBtn.setText(QCoreApplication.translate("MainWindow", u"AC 4", None))
        self.addAcPushBtn.setText(QCoreApplication.translate("MainWindow", u"Add AC", None))
        self.removeAcPushBtn.setText(QCoreApplication.translate("MainWindow", u"Remove AC", None))
    # retranslateUi
