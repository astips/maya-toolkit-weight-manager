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
import json
import fnmatch
import shutil
import pymel.core as pm
from PyQt4 import QtCore, QtGui
from .proc.utils import __icon__, __pixmap__
from .resource import manager_qt
from . import toolkits


TOOLKIT_NAME = 'skin-cluster-manager'
CONFIG_DIR = 'astips/config/toolkits/{0}'.format(TOOLKIT_NAME)
CONFIG_FILE = 'config.json'


class MainDialog(QtGui.QDialog, manager_qt.Ui_skinClusterManager_Dialog) :
    def __init__(self, parent=None, machine=None) :
        super(MainDialog,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.config = {}
        self.pathing = None

        # -- Read Config File -- #
        self.__config_loading()
        self.machine = machine

        self.__style()
        self.__connect_cmd()
       
    def __style(self) :
        self.skinClusterManager_progressBar.hide()
        self.skinClusterManager_two_listWidget.setEnabled(False)
        self.skinClusterManager_one_groupBox.setEnabled(False)
        self.skinClusterManager_path_LineEdit_cmd()
        self.skinClusterManager_refresh_pushButton_cmd()
        
        self.skinClusterManager_home_pushButton.setIcon(__icon__('icon_home'))
        self.skinClusterManager_folder_pushButton.setIcon(__icon__('icon_folder'))
        self.skinClusterManager_refresh_pushButton.setIcon(__icon__('icon_refresh'))
        self.skinClusterManager_vis_pushButton.setIcon(__icon__('icon_visible'))
        self.skinClusterManager_tool_pushButton.setIcon(__icon__('icon_tool'))
        self.skinClusterManager_path_pushButton.setIcon(__icon__('icon_path'))
        self.skinClusterManager_export_pushButton.setIcon(__icon__('icon_batchExport'))
        self.skinClusterManager_exportComponents_pushButton.setIcon(__icon__('icon_export'))
        self.skinClusterManager_import_pushButton.setIcon(__icon__('icon_import'))
        self.skinClusterManager_batchImport_pushButton.setIcon(__icon__('icon_batchImport'))
        self.skinClusterManager_getInfluenceFromWeightData_pushButton.setIcon(__icon__('icon_influence'))
        self.skinClusterManager_trash_pushButton.setIcon(__icon__('icon_trash'))
        self.skinClusterManager_reload_pushButton.setIcon(__icon__('icon_refresh'))
        self.skinClusterManager_getInfluence_pushButton.setIcon(__icon__('icon_link'))
        self.skinClusterManager_holdInfluence_pushButton.setIcon(__icon__('icon_lock'))
        self.skinClusterManager_unHoldSelectedInfluence_pushButton.setIcon(__icon__('icon_key'))
        self.skinClusterManager_resetBindPose_pushButton.setIcon(__icon__('icon_reBind'))
        self.skinClusterManager_removeUnusedInfluence_pushButton.setIcon(__icon__('icon_cleanInf'))

    def __connect_cmd(self) :
        self.skinClusterManager_home_pushButton.clicked.connect(self.skinClusterManager_home_pushButton_cmd)
        self.skinClusterManager_folder_pushButton.clicked.connect(self.skinClusterManager_folder_pushButton_cmd)
        self.skinClusterManager_refresh_pushButton.clicked.connect(self.skinClusterManager_refresh_pushButton_cmd)
        self.skinClusterManager_vis_pushButton.clicked.connect(self.skinClusterManager_vis_pushButton_cmd)
        self.skinClusterManager_tool_pushButton.clicked.connect(self.skinClusterManager_tool_pushButton_cmd)
        self.skinClusterManager_path_pushButton.clicked.connect(self.skinClusterManager_path_pushButton_cmd)
        self.skinClusterManager_one_listWidget.itemClicked.connect(self.skinClusterManager_one_listWidget_itemClicked_cmd)
        self.skinClusterManager_one_listWidget.itemDoubleClicked.connect(self.skinClusterManager_one_listWidget_itemDoubleClicked_cmd)
        self.skinClusterManager_two_listWidget.itemClicked.connect(self.skinClusterManager_two_listWidget_itemClicked_cmd)
        self.skinClusterManager_two_listWidget.itemDoubleClicked.connect(self.skinClusterManager_two_listWidget_itemDoubleClicked_cmd)
        self.skinClusterManager_export_pushButton.clicked.connect(self.skinClusterManager_export_pushButton_cmd)
        self.skinClusterManager_exportComponents_pushButton.clicked.connect(self.skinClusterManager_exportComponents_pushButton_cmd)
        self.skinClusterManager_import_pushButton.clicked.connect(self.skinClusterManager_import_pushButton_cmd)
        self.skinClusterManager_batchImport_pushButton.clicked.connect(self.skinClusterManager_batchImport_pushButton_cmd)
        self.skinClusterManager_getInfluenceFromWeightData_pushButton.clicked.connect(self.skinClusterManager_getInfluenceFromWeightData_pushButton_cmd)
        self.skinClusterManager_trash_pushButton.clicked.connect(self.skinClusterManager_trash_pushButton_cmd)
        self.skinClusterManager_reload_pushButton.clicked.connect(self.skinClusterManager_reload_pushButton_cmd)
        self.skinClusterManager_getInfluence_pushButton.clicked.connect(self.skinClusterManager_getInfluence_pushButton_cmd)
        self.skinClusterManager_resetBindPose_pushButton.clicked.connect(self.skinClusterManager_resetBindPose_pushButton_cmd)
        self.skinClusterManager_holdInfluence_pushButton.clicked.connect(self.skinClusterManager_holdInfluence_pushButton_cmd)
        self.skinClusterManager_unHoldSelectedInfluence_pushButton.clicked.connect(self.skinClusterManager_unHoldSelectedInfluence_pushButton_cmd)
        self.skinClusterManager_removeUnusedInfluence_pushButton.clicked.connect(self.skinClusterManager_removeUnusedInfluence_pushButton_cmd)

    def skinClusterManager_home_pushButton_cmd(self) :
        dialog = pm.fileDialog2(ds=2, fileMode=3, caption='Set Root Path To :', 
                                dir='d:/', okc='Set Path', cc='Cancle')
        if dialog :
            self.config['root'] = str(dialog[0])
            self.pathing = self.config['root']
            self.skinClusterManager_path_LineEdit_cmd()
            self.skinClusterManager_refresh_pushButton_cmd()
            self.__config_dumping()

    def skinClusterManager_folder_pushButton_cmd(self) :
        dialog = QtGui.QInputDialog()
        value = str(dialog.getText(None, 'Create New Folder', 'Enter Folder Name')[0])
        if value :
            if os.path.exists(os.path.join(self.config['root'], value)) :
                raise NameError ('Folder Already Exist !' ) 
            else :
                os.mkdir(os.path.join(self.config['root'], value))
                newItem = QtGui.QListWidgetItem(self.skinClusterManager_one_listWidget)
                newItem.linkType = 'folder'
                newItem.linkPath = os.path.join(self.config['root'], value)
                newItem.linkName = value
                newItem.setText(value)
                newItem.setIcon(__icon__('icon_folder'))

    def skinClusterManager_refresh_pushButton_cmd(self) :
        self.skinClusterManager_one_listWidget.clear()
        self.skinClusterManager_two_listWidget.clear()
        self.skinClusterManager_one_groupBox.setEnabled(False)
        self.skinClusterManager_two_listWidget.setEnabled(False)
        try:
            for item in os.listdir(self.config['root']) :
                subPath = os.path.normpath(os.path.join(self.config['root'], item))
                if os.path.isdir(subPath) :
                    newItem = QtGui.QListWidgetItem(self.skinClusterManager_one_listWidget)
                    newItem.linkType = 'folder'
                    newItem.linkPath = subPath
                    newItem.linkName = item
                    newItem.setText(item)

                    newItem.setIcon(__icon__('icon_folder'))
        except :
            pass

    def skinClusterManager_vis_pushButton_cmd(self) :
        if self.skinClusterManager_one_listWidget.isVisible() :
            self.skinClusterManager_one_listWidget.hide()
        else :
            self.skinClusterManager_one_listWidget.show()

    def skinClusterManager_tool_pushButton_cmd(self) :
        ui = toolkits.ToolKitsDialog(self.parent, self.machine)
        ui.show()
        ui.exec_()

    def skinClusterManager_path_LineEdit_cmd(self) :
        try :
            self.skinClusterManager_path_LineEdit.setText(QtCore.QString(self.pathing))
            self.skinClusterManager_path_LineEdit.setCursorPosition(0)
        except :
            pass

    def skinClusterManager_path_pushButton_cmd(self) :
        try :
            os.startfile(self.pathing)
        except :
            pass

    def skinClusterManager_one_listWidget_itemClicked_cmd(self) :
        self.skinClusterManager_listWidget_cmd(listWidget=self.skinClusterManager_one_listWidget, method='single')

    def skinClusterManager_one_listWidget_itemDoubleClicked_cmd(self) :
        self.skinClusterManager_listWidget_cmd(listWidget=self.skinClusterManager_one_listWidget, method='double')

    def skinClusterManager_two_listWidget_itemClicked_cmd(self) :
        self.skinClusterManager_listWidget_cmd(listWidget=self.skinClusterManager_two_listWidget, method='single')

    def skinClusterManager_two_listWidget_itemDoubleClicked_cmd(self) :
        self.skinClusterManager_listWidget_cmd(listWidget=self.skinClusterManager_two_listWidget, method='double')

    def skinClusterManager_listWidget_cmd(self,listWidget=None, method=None) :       
        if listWidget.currentItem().linkType == 'folder' :       
            if method == 'single' :
                self.skinClusterManager_two_listWidget.clear()
                self.skinClusterManager_one_groupBox.setEnabled(True)
                self.skinClusterManager_two_listWidget.setEnabled(True)
                self.pathing = listWidget.currentItem().linkPath
                self.skinClusterManager_path_LineEdit_cmd()

                for item in os.listdir(self.pathing) :
                    subPath = os.path.normpath(os.path.join(self.pathing, item))
                    if os.path.isfile(subPath) and fnmatch.fnmatch(item, '*.xml') :
                        newItem = QtGui.QListWidgetItem(self.skinClusterManager_two_listWidget)
                        newItem.linkType = 'weight'
                        newItem.linkPath = subPath
                        newItem.linkName = item
                        newItem.setText(item.split('[')[0].replace('#','|'))

                        icon = QtGui.QIcon()
                        if item.split('[')[1].split(']')[0] == 'mesh' :
                            icon.addPixmap(__pixmap__('icon_mesh'))
                        elif item.split('[')[1].split(']')[0] == 'nurbsSurface' :
                            icon.addPixmap(__pixmap__('icon_surface'))
                        elif item.split('[')[1].split(']')[0] == 'nurbsCurve' :
                            icon.addPixmap(__pixmap__('icon_curve'))
                        elif item.split('[')[1].split(']')[0] == 'lattice' :
                            icon.addPixmap(__pixmap__('icon_lattice'))
                        newItem.setIcon(icon)

            elif method == 'double' :
                confirmDialog = pm.confirmDialog(title='Delete', 
                                                 message='Delete?', 
                                                 button=['Delete Flder','Cancle'], 
                                                 cancelButton='Cancle', 
                                                 dismissString='Cancle', 
                                                 icon='question'
                                                 )
                if confirmDialog == 'Delete Flder' :
                    try :
                        os.rmdir(self.pathing) ## os.rmdir : delete empty dir
                        listWidget.currentItem().setHidden(True)
                        self.skinClusterManager_one_groupBox.setEnabled(False)
                        self.skinClusterManager_two_listWidget.setEnabled(False)
                    except :
                        confirmDialog = pm.confirmDialog(title='Delete', 
                                                         message='File in Folder ' + ', Sure To Delete ?', 
                                                         button=['Yes','No'], 
                                                         defaultButton='Yes', 
                                                         cancelButton='No', 
                                                         dismissString='No', 
                                                         icon='warning'
                                                         )
                        if confirmDialog == 'Yes' :
                            try :
                                shutil.rmtree(self.pathing) # shutil.rmtree : delete dir
                                listWidget.currentItem().setHidden(True)
                            except : pass
                            self.skinClusterManager_two_listWidget.clear()
                            self.skinClusterManager_one_groupBox.setEnabled(False)
                            self.skinClusterManager_two_listWidget.setEnabled(False)
                            self.pathing = self.config['root']
                            self.skinClusterManager_path_LineEdit_cmd()
            else :
                pass
        elif listWidget.currentItem().linkType == 'weight' : 
            if method == 'single' :
                pass
            elif method == 'double' :
                self.machine.getInfluenceFromWeightData(listWidget.currentItem().linkPath)

    def skinClusterManager_export_pushButton_cmd(self) :
        self.skinClusterManager_progressBar.show()
        self.machine.exportSkinWeight(exportPath=self.pathing, 
                                      QWidget=[self.skinClusterManager_progressBar, 
                                      self.skinClusterManager_two_listWidget])
        self.skinClusterManager_progressBar.setValue(0)
        self.skinClusterManager_progressBar.hide()

    def skinClusterManager_exportComponents_pushButton_cmd(self) :
        self.skinClusterManager_progressBar.show()
        self.machine.exportComponentsSkinWeight(exportPath=self.pathing, 
                                                QWidget=[self.skinClusterManager_progressBar, self.skinClusterManager_two_listWidget])
        self.skinClusterManager_progressBar.setValue(0)
        self.skinClusterManager_progressBar.hide()

    def skinClusterManager_import_pushButton_cmd(self) :
        items = self.skinClusterManager_two_listWidget.selectedItems()
        if len(items) == 1 :
            dataPath = items[0].linkPath
            self.skinClusterManager_progressBar.show()
            self.machine.importSkinWeight(method='single', 
                                          weightFilePath=dataPath, 
                                          QWidget=[self.skinClusterManager_progressBar]
                                          )
            self.skinClusterManager_progressBar.setValue(0)
            self.skinClusterManager_progressBar.hide()
        else :
            pm.displayWarning('must select only one item ! try again...')

    def skinClusterManager_batchImport_pushButton_cmd(self) :
        items = self.skinClusterManager_two_listWidget.selectedItems()
        if len(items) != 0 :
            self.skinClusterManager_progressBar.show()
            for item in items :
                dataPath = item.linkPath
                self.machine.importSkinWeight(method='batch', 
                                              weightFilePath=dataPath, 
                                              QWidget=[self.skinClusterManager_progressBar]
                                              )
            self.skinClusterManager_progressBar.setValue(0)
            self.skinClusterManager_progressBar.hide()
        else :
            pm.displayWarning('must select item ! try again...')

    def skinClusterManager_getInfluenceFromWeightData_pushButton_cmd(self) :
        items = self.skinClusterManager_two_listWidget.selectedItems()
        if len(items) == 1 :
            self.machine.getInfluenceFromWeightData(self.skinClusterManager_two_listWidget.currentItem().linkPath)
        else :
            pm.displayWarning('must select only one item ! try again...')

    def skinClusterManager_trash_pushButton_cmd(self) :
        items = self.skinClusterManager_two_listWidget.selectedItems()
        if len(items) :
            confirmDialog = pm.confirmDialog(title='Delete', 
                                             message=' Sure To Delete ?', 
                                             button=['Yes','No'], 
                                             defaultButton='Yes', 
                                             cancelButton='No', 
                                             dismissString='No', 
                                             icon='warning'
                                             )
            if confirmDialog == 'Yes' :
                for item in items :              
                    dataPath = item.linkPath
                    if os.path.isfile(dataPath) :
                        try :
                            os.remove(dataPath) ## os.remove : delete file
                            item.setHidden(True)
                        except :
                            pass
            else :
                pass
        else :
            pass

    def skinClusterManager_reload_pushButton_cmd(self) :
        self.skinClusterManager_two_listWidget.clear()
        try :
            self.skinClusterManager_one_listWidget_itemClicked_cmd()
        except :
            pass

    def skinClusterManager_getInfluence_pushButton_cmd(self) :
        self.machine.getInfluence(node=None,select=1)

    def skinClusterManager_holdInfluence_pushButton_cmd(self) :
        self.machine.holdInfluence(v=1)

    def skinClusterManager_unHoldSelectedInfluence_pushButton_cmd(self) :
        self.machine.unholdSelectInfluence(v=0)

    def skinClusterManager_resetBindPose_pushButton_cmd(self) :
        self.machine.resetBindPose(node=None)

    def skinClusterManager_removeUnusedInfluence_pushButton_cmd(self) :
        skinClusterNodes = self.machine.getSkinCluster(node=None)
        if skinClusterNodes :
            for skinClusterNode in skinClusterNodes :
                self.machine.removeUnusedInfluence(skinClusterNode)

    def __config_dumping(self) :
        userPrefPath = pm.internalVar(upd=True)
        configDir = os.path.join(userPrefPath, CONFIG_DIR)
        configFile = os.path.join(configDir, CONFIG_FILE)
        if not os.path.exists(configDir):
            os.makedirs(configDir)

        # -- Write 2 File -- #
        with open(configFile.replace('\\', '/'), 'wb') as f :
            f.write(json.dumps(self.config, ensure_ascii=True, indent=4))

    def __config_loading(self) :
        userPrefPath = pm.internalVar(upd=True)
        configFile = os.path.join(userPrefPath, CONFIG_DIR, CONFIG_FILE)
        if not os.path.exists(configFile) :
            self.config.setdefault('root', '')
            return

        with open(configFile.replace('\\', '/'), 'rb') as f :
            self.config = json.load(f) or {}
            if self.config :
                self.pathing = self.config['root']
