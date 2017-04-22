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
import os
from PyQt4 import QtGui


ICON_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resource/icon').replace('\\', '/')


def __icon__(image, suffix='png') :
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(os.path.join(ICON_PATH, '{0}.{1}'.format(image, suffix))), QtGui.QIcon.Normal, QtGui.QIcon.On)
    return icon


def __pixmap__(image, suffix='png') :
    pixmap = QtGui.QPixmap(os.path.join(ICON_PATH, '{0}.{1}'.format(image, suffix)))
    return pixmap
