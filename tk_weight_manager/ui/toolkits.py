# -*- coding: utf-8 -*-

###########################################################################################
#
# Author: astips - (animator.well)
#
# Date: 2014.11
#
# Url: https://github.com/astips
#
# Description: skinCluster weight machine
#
###########################################################################################
from QtSide import QtWidgets
from .resource import toolkits_qt
from .proc.utils import __icon__


class ToolKitsDialog(QtWidgets.QDialog, toolkits_qt.Ui_skinClusterToolKit_Dialog):
    def __init__(self, parent=None, machine=None):
        super(ToolKitsDialog, self).__init__(parent)
        self.setupUi(self)

        self.machine = machine

        self.skinClusterToolKit_getInfluence_pushButton.clicked.connect(self.__getInfluence)
        self.skinClusterToolKit_holdInfluence_pushButton.clicked.connect(self.__holdInfluence)
        self.skinClusterToolKit_unHoldSelectedInfluence_pushButton.clicked.connect(self.__unHoldSelectedInfluence)
        self.skinClusterToolKit_copyComponentWeight_pushButton.clicked.connect(self.__copyComponentWeight)
        self.skinClusterToolKit_pasteComponentWeight_pushButton.clicked.connect(self._pasteComponentWeight)
        self.skinClusterToolKit_resetBindPose_pushButton.clicked.connect(self.__resetBindPose)
        self.skinClusterToolKit_removeUnusedInfluence_pushButton.clicked.connect(self.__removeUnusedInfluence)

        self.__style()

    def __style(self):
        self.skinClusterToolKit_getInfluence_pushButton.setIcon(__icon__('icon_link'))
        self.skinClusterToolKit_holdInfluence_pushButton.setIcon(__icon__('icon_lock'))
        self.skinClusterToolKit_unHoldSelectedInfluence_pushButton.setIcon(__icon__('icon_key'))
        self.skinClusterToolKit_copyComponentWeight_pushButton.setIcon(__icon__('icon_position'))
        self.skinClusterToolKit_pasteComponentWeight_pushButton.setIcon(__icon__('icon_pencil'))
        self.skinClusterToolKit_resetBindPose_pushButton.setIcon(__icon__('icon_reBind'))
        self.skinClusterToolKit_removeUnusedInfluence_pushButton.setIcon(__icon__('icon_cleanInf'))

    def __getInfluence(self):
        self.machine.getInfluence(node=None, select=1)

    def __holdInfluence(self):
        self.machine.holdInfluence(v=1)

    def __unHoldSelectedInfluence(self):
        self.machine.unholdSelectInfluence(v=0)

    def __copyComponentWeight(self):
        self.machine.takeComponentWeight()

    def _pasteComponentWeight(self):
        self.machine.pasteComponentWeight()

    def __resetBindPose(self):
        self.machine.resetBindPose(node=None)

    def __removeUnusedInfluence(self):
        skinClusterNodes = self.machine.getSkinCluster(node=None)
        if skinClusterNodes:
            for skinClusterNode in skinClusterNodes:
                self.machine.removeUnusedInfluence(skinClusterNode)
