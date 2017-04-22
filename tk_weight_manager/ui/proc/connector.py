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

def connect(_type='PyQt4') :
    if _type == 'PyQt4' :
        try :
            from PyQt4 import QtCore, QtGui
            from sip import wrapinstance
        except :
            OpenMaya.MGlobal.displayError('Faild Loading PyQt4...')
            return 
    elif _type == 'PySide' :
        try :
            from PySide import QtGui, QtCore
            from shiboken import wrapInstance as wrapinstance
        except :
            OpenMaya.MGlobal.displayError('Faild Loading PySide...')
            return
    
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapinstance(long(ptr), QtGui.QMainWindow)
