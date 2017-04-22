# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\animator.well\github-repertories\maya-toolkit-weight-manager\tk_weight_manager\ui\resource\designer\toolkits_qt.ui'
#
# Created: Sun Apr 23 02:49:03 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_skinClusterToolKit_Dialog(object):
    def setupUi(self, skinClusterToolKit_Dialog):
        skinClusterToolKit_Dialog.setObjectName(_fromUtf8("skinClusterToolKit_Dialog"))
        skinClusterToolKit_Dialog.resize(211, 35)
        self.skinClusterToolKit_Dialog_verticalLayout = QtGui.QVBoxLayout(skinClusterToolKit_Dialog)
        self.skinClusterToolKit_Dialog_verticalLayout.setSpacing(2)
        self.skinClusterToolKit_Dialog_verticalLayout.setMargin(3)
        self.skinClusterToolKit_Dialog_verticalLayout.setObjectName(_fromUtf8("skinClusterToolKit_Dialog_verticalLayout"))
        self.skinClusterToolKit_groupBox = QtGui.QGroupBox(skinClusterToolKit_Dialog)
        self.skinClusterToolKit_groupBox.setTitle(_fromUtf8(""))
        self.skinClusterToolKit_groupBox.setObjectName(_fromUtf8("skinClusterToolKit_groupBox"))
        self.skinClusterToolKit_groupBox_horizontalLayout = QtGui.QHBoxLayout(self.skinClusterToolKit_groupBox)
        self.skinClusterToolKit_groupBox_horizontalLayout.setSpacing(2)
        self.skinClusterToolKit_groupBox_horizontalLayout.setMargin(2)
        self.skinClusterToolKit_groupBox_horizontalLayout.setObjectName(_fromUtf8("skinClusterToolKit_groupBox_horizontalLayout"))
        self.skinClusterToolKit_getInfluence_pushButton = QtGui.QPushButton(self.skinClusterToolKit_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skinClusterToolKit_getInfluence_pushButton.sizePolicy().hasHeightForWidth())
        self.skinClusterToolKit_getInfluence_pushButton.setSizePolicy(sizePolicy)
        self.skinClusterToolKit_getInfluence_pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.skinClusterToolKit_getInfluence_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.skinClusterToolKit_getInfluence_pushButton.setFlat(True)
        self.skinClusterToolKit_getInfluence_pushButton.setObjectName(_fromUtf8("skinClusterToolKit_getInfluence_pushButton"))
        self.skinClusterToolKit_groupBox_horizontalLayout.addWidget(self.skinClusterToolKit_getInfluence_pushButton)
        self.skinClusterToolKit_holdInfluence_pushButton = QtGui.QPushButton(self.skinClusterToolKit_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skinClusterToolKit_holdInfluence_pushButton.sizePolicy().hasHeightForWidth())
        self.skinClusterToolKit_holdInfluence_pushButton.setSizePolicy(sizePolicy)
        self.skinClusterToolKit_holdInfluence_pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.skinClusterToolKit_holdInfluence_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.skinClusterToolKit_holdInfluence_pushButton.setFlat(True)
        self.skinClusterToolKit_holdInfluence_pushButton.setObjectName(_fromUtf8("skinClusterToolKit_holdInfluence_pushButton"))
        self.skinClusterToolKit_groupBox_horizontalLayout.addWidget(self.skinClusterToolKit_holdInfluence_pushButton)
        self.skinClusterToolKit_unHoldSelectedInfluence_pushButton = QtGui.QPushButton(self.skinClusterToolKit_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skinClusterToolKit_unHoldSelectedInfluence_pushButton.sizePolicy().hasHeightForWidth())
        self.skinClusterToolKit_unHoldSelectedInfluence_pushButton.setSizePolicy(sizePolicy)
        self.skinClusterToolKit_unHoldSelectedInfluence_pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.skinClusterToolKit_unHoldSelectedInfluence_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.skinClusterToolKit_unHoldSelectedInfluence_pushButton.setFlat(True)
        self.skinClusterToolKit_unHoldSelectedInfluence_pushButton.setObjectName(_fromUtf8("skinClusterToolKit_unHoldSelectedInfluence_pushButton"))
        self.skinClusterToolKit_groupBox_horizontalLayout.addWidget(self.skinClusterToolKit_unHoldSelectedInfluence_pushButton)
        self.line = QtGui.QFrame(self.skinClusterToolKit_groupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.skinClusterToolKit_groupBox_horizontalLayout.addWidget(self.line)
        self.skinClusterToolKit_copyComponentWeight_pushButton = QtGui.QPushButton(self.skinClusterToolKit_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skinClusterToolKit_copyComponentWeight_pushButton.sizePolicy().hasHeightForWidth())
        self.skinClusterToolKit_copyComponentWeight_pushButton.setSizePolicy(sizePolicy)
        self.skinClusterToolKit_copyComponentWeight_pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.skinClusterToolKit_copyComponentWeight_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.skinClusterToolKit_copyComponentWeight_pushButton.setFlat(True)
        self.skinClusterToolKit_copyComponentWeight_pushButton.setObjectName(_fromUtf8("skinClusterToolKit_copyComponentWeight_pushButton"))
        self.skinClusterToolKit_groupBox_horizontalLayout.addWidget(self.skinClusterToolKit_copyComponentWeight_pushButton)
        self.skinClusterToolKit_pasteComponentWeight_pushButton = QtGui.QPushButton(self.skinClusterToolKit_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skinClusterToolKit_pasteComponentWeight_pushButton.sizePolicy().hasHeightForWidth())
        self.skinClusterToolKit_pasteComponentWeight_pushButton.setSizePolicy(sizePolicy)
        self.skinClusterToolKit_pasteComponentWeight_pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.skinClusterToolKit_pasteComponentWeight_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.skinClusterToolKit_pasteComponentWeight_pushButton.setFlat(True)
        self.skinClusterToolKit_pasteComponentWeight_pushButton.setObjectName(_fromUtf8("skinClusterToolKit_pasteComponentWeight_pushButton"))
        self.skinClusterToolKit_groupBox_horizontalLayout.addWidget(self.skinClusterToolKit_pasteComponentWeight_pushButton)
        self.line_2 = QtGui.QFrame(self.skinClusterToolKit_groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.skinClusterToolKit_groupBox_horizontalLayout.addWidget(self.line_2)
        self.skinClusterToolKit_resetBindPose_pushButton = QtGui.QPushButton(self.skinClusterToolKit_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skinClusterToolKit_resetBindPose_pushButton.sizePolicy().hasHeightForWidth())
        self.skinClusterToolKit_resetBindPose_pushButton.setSizePolicy(sizePolicy)
        self.skinClusterToolKit_resetBindPose_pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.skinClusterToolKit_resetBindPose_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.skinClusterToolKit_resetBindPose_pushButton.setFlat(True)
        self.skinClusterToolKit_resetBindPose_pushButton.setObjectName(_fromUtf8("skinClusterToolKit_resetBindPose_pushButton"))
        self.skinClusterToolKit_groupBox_horizontalLayout.addWidget(self.skinClusterToolKit_resetBindPose_pushButton)
        self.skinClusterToolKit_removeUnusedInfluence_pushButton = QtGui.QPushButton(self.skinClusterToolKit_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skinClusterToolKit_removeUnusedInfluence_pushButton.sizePolicy().hasHeightForWidth())
        self.skinClusterToolKit_removeUnusedInfluence_pushButton.setSizePolicy(sizePolicy)
        self.skinClusterToolKit_removeUnusedInfluence_pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.skinClusterToolKit_removeUnusedInfluence_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.skinClusterToolKit_removeUnusedInfluence_pushButton.setFlat(True)
        self.skinClusterToolKit_removeUnusedInfluence_pushButton.setObjectName(_fromUtf8("skinClusterToolKit_removeUnusedInfluence_pushButton"))
        self.skinClusterToolKit_groupBox_horizontalLayout.addWidget(self.skinClusterToolKit_removeUnusedInfluence_pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.skinClusterToolKit_groupBox_horizontalLayout.addItem(spacerItem)
        self.skinClusterToolKit_Dialog_verticalLayout.addWidget(self.skinClusterToolKit_groupBox)

        self.retranslateUi(skinClusterToolKit_Dialog)
        QtCore.QMetaObject.connectSlotsByName(skinClusterToolKit_Dialog)

    def retranslateUi(self, skinClusterToolKit_Dialog):
        skinClusterToolKit_Dialog.setWindowTitle(_translate("skinClusterToolKit_Dialog", "SkinCluster - ToolKits", None))
        self.skinClusterToolKit_getInfluence_pushButton.setToolTip(_translate("skinClusterToolKit_Dialog", "get influences", None))
        self.skinClusterToolKit_holdInfluence_pushButton.setToolTip(_translate("skinClusterToolKit_Dialog", "hold influence", None))
        self.skinClusterToolKit_unHoldSelectedInfluence_pushButton.setToolTip(_translate("skinClusterToolKit_Dialog", "unhold selected influences", None))
        self.skinClusterToolKit_copyComponentWeight_pushButton.setToolTip(_translate("skinClusterToolKit_Dialog", "copy component weight", None))
        self.skinClusterToolKit_pasteComponentWeight_pushButton.setToolTip(_translate("skinClusterToolKit_Dialog", "paste component weight", None))
        self.skinClusterToolKit_resetBindPose_pushButton.setToolTip(_translate("skinClusterToolKit_Dialog", "reset bind pose", None))
        self.skinClusterToolKit_removeUnusedInfluence_pushButton.setToolTip(_translate("skinClusterToolKit_Dialog", "remove unused influences", None))

