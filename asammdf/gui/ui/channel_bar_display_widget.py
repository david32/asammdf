# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'channel_bar_display_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChannelBarDisplay(object):
    def setupUi(self, ChannelBarDisplay):
        ChannelBarDisplay.setObjectName("ChannelBarDisplay")
        ChannelBarDisplay.resize(154, 46)
        ChannelBarDisplay.setMinimumSize(QtCore.QSize(40, 46))
        ChannelBarDisplay.setMaximumSize(QtCore.QSize(16777215, 46))
        self.verticalLayout = QtWidgets.QVBoxLayout(ChannelBarDisplay)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setObjectName("layout")
        self.color_btn = QtWidgets.QPushButton(ChannelBarDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_btn.sizePolicy().hasHeightForWidth())
        self.color_btn.setSizePolicy(sizePolicy)
        self.color_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.color_btn.setMaximumSize(QtCore.QSize(16, 16))
        self.color_btn.setAutoFillBackground(False)
        self.color_btn.setText("")
        self.color_btn.setFlat(False)
        self.color_btn.setObjectName("color_btn")
        self.layout.addWidget(self.color_btn)
        self.name = QtWidgets.QLabel(ChannelBarDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setMinimumSize(QtCore.QSize(130, 40))
        self.name.setMaximumSize(QtCore.QSize(16777215, 40))
        self.name.setMouseTracking(False)
        self.name.setTextFormat(QtCore.Qt.PlainText)
        self.name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.name.setObjectName("name")
        self.layout.addWidget(self.name)
        self.verticalLayout.addLayout(self.layout)

        self.retranslateUi(ChannelBarDisplay)
        QtCore.QMetaObject.connectSlotsByName(ChannelBarDisplay)

    def retranslateUi(self, ChannelBarDisplay):
        _translate = QtCore.QCoreApplication.translate
        ChannelBarDisplay.setWindowTitle(_translate("ChannelBarDisplay", "Form"))
        self.name.setText(_translate("ChannelBarDisplay", "MAIN CLOCK"))