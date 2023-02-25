# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remoteControlHIUuUh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources_rc


class Ui_remoteControl(object):
    def setupUi(self, remoteControl):
        if not remoteControl.objectName():
            remoteControl.setObjectName(u"remoteControl")
        remoteControl.resize(335, 351)
        remoteControl.setStyleSheet(u"#frame QLabel\n"
                                    "{\n"
                                    "	font: 28pt \"Times New Roman\";\n"
                                    "\n"
                                    "}")
        self.verticalLayout = QVBoxLayout(remoteControl)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(remoteControl)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(169, 208, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.roomNameLabel = QLabel(self.frame_4)
        self.roomNameLabel.setObjectName(u"roomNameLabel")

        self.horizontalLayout_2.addWidget(self.roomNameLabel, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.OnOffLabel = QLabel(self.frame_3)
        self.OnOffLabel.setObjectName(u"OnOffLabel")
        self.OnOffLabel.setPixmap(QPixmap(u":/images/OFF.png"))

        self.verticalLayout_2.addWidget(self.OnOffLabel)

        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignRight | Qt.AlignBottom)

        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.line = QFrame(remoteControl)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.functionsFrame = QFrame(remoteControl)
        self.functionsFrame.setObjectName(u"functionsFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.functionsFrame.sizePolicy().hasHeightForWidth())
        self.functionsFrame.setSizePolicy(sizePolicy1)
        self.functionsFrame.setStyleSheet(u"#functionsFrame{\n"
                                          "	background-color: rgb(224, 237, 255);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton\n"
                                          "{\n"
                                          "	font: 15pt \"Times New Roman\";\n"
                                          "	font-color: black;\n"
                                          "	background: rgb(183, 230, 255);\n"
                                          "	border-radius: 10px;\n"
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
        self.functionsFrame.setFrameShape(QFrame.StyledPanel)
        self.functionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.functionsFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.functionsFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/images/WARM.png"))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.tempStateSlider = QSlider(self.frame_6)
        self.tempStateSlider.setObjectName(u"tempStateSlider")
        self.tempStateSlider.setMaximum(1)
        self.tempStateSlider.setPageStep(1)
        self.tempStateSlider.setOrientation(Qt.Horizontal)
        self.tempStateSlider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_4.addWidget(self.tempStateSlider)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/images/COLD.png"))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.functionsFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.decreaseTempPushBtn = QPushButton(self.frame_5)
        self.decreaseTempPushBtn.setObjectName(u"decreaseTempPushBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.decreaseTempPushBtn.sizePolicy().hasHeightForWidth())
        self.decreaseTempPushBtn.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/icons/icons8-subtract-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.decreaseTempPushBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.decreaseTempPushBtn)

        self.wantedTempLCDDisp = QLCDNumber(self.frame_5)
        self.wantedTempLCDDisp.setObjectName(u"wantedTempLCDDisp")

        self.horizontalLayout_3.addWidget(self.wantedTempLCDDisp)

        self.increaseTempPushBtn = QPushButton(self.frame_5)
        self.increaseTempPushBtn.setObjectName(u"increaseTempPushBtn")
        sizePolicy2.setHeightForWidth(self.increaseTempPushBtn.sizePolicy().hasHeightForWidth())
        self.increaseTempPushBtn.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-plus-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.increaseTempPushBtn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.increaseTempPushBtn)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.functionsFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 14pt \"Times New Roman\";")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.roomTempLCDDisp = QLCDNumber(self.frame_7)
        self.roomTempLCDDisp.setObjectName(u"roomTempLCDDisp")

        self.horizontalLayout_5.addWidget(self.roomTempLCDDisp)

        self.verticalLayout_3.addWidget(self.frame_7)

        self.verticalLayout.addWidget(self.functionsFrame)

        self.retranslateUi(remoteControl)

        QMetaObject.connectSlotsByName(remoteControl)

    # setupUi

    def retranslateUi(self, remoteControl):
        remoteControl.setWindowTitle(QCoreApplication.translate("remoteControl", u"Dialog", None))
        self.roomNameLabel.setText(QCoreApplication.translate("remoteControl", u"Room", None))
        self.OnOffLabel.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.decreaseTempPushBtn.setText("")
        self.increaseTempPushBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("remoteControl", u"Real Time Room Temp. [\u2103]", None))
    # retranslateUi
