# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buddyWindow.ui'
#
# Created: Thu Jan  6 00:23:46 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_BuddyWindow(object):
    def setupUi(self, BuddyWindow):
        BuddyWindow.setObjectName("BuddyWindow")
        BuddyWindow.resize(396, 573)
        self.verticalLayout_2 = QtGui.QVBoxLayout(BuddyWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.errorLabel = QtGui.QLabel(BuddyWindow)
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout_2.addWidget(self.errorLabel)
        self.drawingareaWidget = QtGui.QWidget(BuddyWindow)
        self.drawingareaWidget.setObjectName("drawingareaWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.drawingareaWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(13, 237, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QGraphicsView(self.drawingareaWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(320, 240))
        self.frame.setMaximumSize(QtCore.QSize(320, 240))
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.colorShowLabel = QtGui.QLabel(self.drawingareaWidget)
        self.colorShowLabel.setMinimumSize(QtCore.QSize(20, 20))
        self.colorShowLabel.setMaximumSize(QtCore.QSize(20, 16777215))
        self.colorShowLabel.setToolTip("")
        self.colorShowLabel.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.colorShowLabel.setText("")
        self.colorShowLabel.setObjectName("colorShowLabel")
        self.horizontalLayout_2.addWidget(self.colorShowLabel)
        self.strokeShowLabel = QtGui.QLabel(self.drawingareaWidget)
        self.strokeShowLabel.setStyleSheet("font: 75 10pt \"Arial Black\";")
        self.strokeShowLabel.setObjectName("strokeShowLabel")
        self.horizontalLayout_2.addWidget(self.strokeShowLabel)
        self.strokeSlider = QtGui.QSlider(self.drawingareaWidget)
        self.strokeSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.strokeSlider.setMinimum(0)
        self.strokeSlider.setMaximum(5)
        self.strokeSlider.setSingleStep(1)
        self.strokeSlider.setSliderPosition(1)
        self.strokeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.strokeSlider.setObjectName("strokeSlider")
        self.horizontalLayout_2.addWidget(self.strokeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.colorButton = QtGui.QPushButton(self.drawingareaWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton.sizePolicy().hasHeightForWidth())
        self.colorButton.setSizePolicy(sizePolicy)
        self.colorButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.colorButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.colorButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorButton.setIcon(icon)
        self.colorButton.setObjectName("colorButton")
        self.horizontalLayout.addWidget(self.colorButton)
        self.strokeButton = QtGui.QPushButton(self.drawingareaWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strokeButton.sizePolicy().hasHeightForWidth())
        self.strokeButton.setSizePolicy(sizePolicy)
        self.strokeButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.strokeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.strokeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.strokeButton.setIcon(icon1)
        self.strokeButton.setCheckable(True)
        self.strokeButton.setChecked(True)
        self.strokeButton.setObjectName("strokeButton")
        self.horizontalLayout.addWidget(self.strokeButton)
        self.eraseButton = QtGui.QPushButton(self.drawingareaWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eraseButton.sizePolicy().hasHeightForWidth())
        self.eraseButton.setSizePolicy(sizePolicy)
        self.eraseButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.eraseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.eraseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eraseButton.setIcon(icon2)
        self.eraseButton.setCheckable(True)
        self.eraseButton.setObjectName("eraseButton")
        self.horizontalLayout.addWidget(self.eraseButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.clearButton = QtGui.QPushButton(self.drawingareaWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clearButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clearButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon3)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.saveButton = QtGui.QPushButton(self.drawingareaWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.saveButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.saveButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon4)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(12, 237, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.drawingareaWidget)
        self.chatBrowser = QtGui.QTextBrowser(BuddyWindow)
        self.chatBrowser.setStyleSheet("font: 9pt \"Arial\";")
        self.chatBrowser.setObjectName("chatBrowser")
        self.verticalLayout_2.addWidget(self.chatBrowser)
        self.chatEdit = QtGui.QLineEdit(BuddyWindow)
        self.chatEdit.setObjectName("chatEdit")
        self.verticalLayout_2.addWidget(self.chatEdit)

        self.retranslateUi(BuddyWindow)
        QtCore.QMetaObject.connectSlotsByName(BuddyWindow)

    def retranslateUi(self, BuddyWindow):
        BuddyWindow.setWindowTitle(QtGui.QApplication.translate("BuddyWindow", "Scribble n Chat", None, QtGui.QApplication.UnicodeUTF8))
        self.errorLabel.setText(QtGui.QApplication.translate("BuddyWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#aa0000;\">Drawing is disabled!</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Your buddy is not using xScribble</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.strokeShowLabel.setToolTip(QtGui.QApplication.translate("BuddyWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:10pt; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stroke thickness</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.strokeShowLabel.setText(QtGui.QApplication.translate("BuddyWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.colorButton.setToolTip(QtGui.QApplication.translate("BuddyWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Colour Chooser</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the colour you want to scribble in</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.strokeButton.setToolTip(QtGui.QApplication.translate("BuddyWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Pencil</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Scribble on the canvas</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.eraseButton.setToolTip(QtGui.QApplication.translate("BuddyWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Eraser</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Erase the mistakes</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setToolTip(QtGui.QApplication.translate("BuddyWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Clear</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Deletes everything on the canvas</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setToolTip(QtGui.QApplication.translate("BuddyWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Save</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Save your scribbles to disk</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chatBrowser.setHtml(QtGui.QApplication.translate("BuddyWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import xscribble_rc
