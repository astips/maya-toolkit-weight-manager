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
from QtSide import QtGui


ICON_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resource/icon').replace('\\', '/')


def __icon__(image, suffix='png'):
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap(os.path.join(ICON_PATH, '{0}.{1}'.format(image, suffix)))
    )
    return icon


def __pixmap__(image, suffix='png'):
    pixmap = QtGui.QPixmap(os.path.join(ICON_PATH, '{0}.{1}'.format(image, suffix)))
    return pixmap


def to_utf8(_input):
    if _input.__class__.__name__ == 'QString':
        _input = str(_input.toUtf8())
        _input = _input.decode('utf-8')
    elif _input.__class__.__name__ == 'str':
        _input = _input.decode('utf-8')
    else:
        pass
    return _input
