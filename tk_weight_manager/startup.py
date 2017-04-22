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
from .ui import gui, toolkits
from .ui.proc.connector import connect
from .core import machine


def show_manager() :
    ui = gui.MainDialog(parent=connect('PyQt4'), 
                        machine=machine.SkinClusterMachine()
                        )
    ui.show()
    ui.exec_()


def show_toolkits() :
    ui = toolkits.ToolKitsDialog(parent=connect('PyQt4'), 
                                 machine=machine.SkinClusterMachine()
                                 )
    ui.show()
    ui.exec_()
