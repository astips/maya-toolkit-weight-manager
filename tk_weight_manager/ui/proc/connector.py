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
import maya.OpenMayaUI as OpenMayaUI
import maya.OpenMaya as OpenMaya


def connect():
    try:
        from QtSide import QtWidgets, ui_wrapper
    except Exception as e:
        OpenMaya.MGlobal.displayError(e)
        return None
    return ui_wrapper.wrapinstance(
        long(OpenMayaUI.MQtUtil.mainWindow()),
        QtWidgets.QMainWindow
    )
