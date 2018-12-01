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
import time
import getpass
from QtSide import QtWidgets, QtGui
from xml.etree.ElementTree import (ElementTree, 
                                   Element, 
                                   SubElement, 
                                   parse)
import pymel.core as pm
from ..ui.proc.utils import __pixmap__


class SkinClusterMachine(object):
    IGNORE_VALUE = 0.00001
    OBJ_TYPE = ['mesh', 'nurbsSurface', 'nurbsCurve', 'lattice']

    def __init__(self) :
        self.user = getpass.getuser()
        self.mayaVersion = pm.versions.installName()

        self.componentInfluenceList = None
        self.componentSkinWeightList = None

    def getTime(self) :
        return time.strftime('%Y/%m/%d', time.localtime(time.time()))

    def getSkinCluster(self, node=None) :
        whiteList = []
        if node == None :
            nodes = pm.selected()
            if nodes :
                node = nodes[0]
            else :
                pm.displayWarning('nothing selected')
        try :
            nodeShapes = node.getShapes()
            if nodeShapes :
                for nodeShape in nodeShapes :
                    historys = nodeShape.listHistory(pruneDagObjects=True, interestLevel=1)
                    for history in historys :
                        if history.type() == 'skinCluster' :
                            whiteList.append(history)
        except :
            pass

        skinClusterList = list(set(whiteList))
        skinClusterList.sort(key=whiteList.index)
        return skinClusterList

    def getInfluence(self, node=None, select=False) :
        if node == None :
            nodes = pm.selected()
            if nodes :
                node = nodes[0]
            else :
                pm.displayWarning('nothing selected')
                return
        skinClusterNodes = self.getSkinCluster(node=node)
        if len(skinClusterNodes) :
            skinClusterNode = skinClusterNodes[0]
            influence = pm.skinCluster(skinClusterNode, q=True, inf=True)
            if select :
                pm.select(influence, r=True)
            return influence
        else : 
            pm.displayWarning('no skin')

    def takeComponentWeight(self) :
        components = pm.selected(fl=True)
        if len(components) != 1 :
            pm.displayWarning('can only select one component')
            return
        component = components[0]
        if component.node().type() not in self.OBJ_TYPE :
            pm.displayWarning('wrong select, component needed')
            return

        node = component.node().getParent()
        skinClusterNodes = self.getSkinCluster(node=node)
        if skinClusterNodes :
            self.componentInfluenceList = pm.skinPercent(skinClusterNodes[0], 
                                                         component, 
                                                         ignoreBelow=self.IGNORE_VALUE, 
                                                         query=True, 
                                                         t=None)
            self.componentSkinWeightList = pm.skinPercent(skinClusterNodes[0], 
                                                          component, 
                                                          ignoreBelow=self.IGNORE_VALUE, 
                                                          query=True, 
                                                          v=True)

        else :
            pm.displayWarning('no skin')

    def pasteComponentWeight(self) :
        if self.componentInfluenceList == None or self.componentSkinWeightList == None :
            pm.displayWarning('no value to paste')
            return
            
        components = pm.selected(fl=True)
        for component in components :
            if component.node().type() not in self.OBJ_TYPE :
                pm.displayWarning('wrong select %s' %component)
                continue

            node = component.node().getParent()
            skinClusterNodes = self.getSkinCluster(node=node)
            if not skinClusterNodes :
                pm.displayWarning('no skin %s' %node)
                continue

            skinPercentList = []
            for i,each in enumerate(self.componentInfluenceList) :
                skinPercentList.append([each, self.componentSkinWeightList[i]])
            pm.skinPercent(skinClusterNodes[0], component, transformValue=skinPercentList)

    def lockWeightList(self, skinClusterNode, v=False) :
        skinClusterNode.weightList.set(lock=v)

    def holdInfluence(self, v=False) :
        nodes = pm.selected()
        if len(nodes) :
            influences = self.getInfluence(node=nodes[0], select=False)
            if influences :
                for influence in influences :
                    influence.liw.set(v)
        else :
            pm.displayWarning('nothing selected')

    def unholdSelectInfluence(self, v=0) :
        nodes = pm.selected()
        if len(nodes) >= 2:
            if nodes[0].getShape() != None :
                if nodes[0].getShape().type() in self.OBJ_TYPE :
                    node = nodes[0]
                    influences = self.getInfluence(node=node, select=False)
                    if influences :
                        for node in nodes :
                            if node in influences :
                                node.liw.set(v)
                else :
                    pm.displayWarning('wrong selected ,please select object first ,then select influences')
            else :
                pm.displayWarning('wrong selected ,please select object first ,then select influences')
        else :
            pm.displayWarning('wrong selected ,please select object first ,then select influences')

    def resetBindPose(self, node=None) :
        if node == None :
            nodes = pm.selected()
        for eachNode in nodes :
            skinClusterNodes = self.getSkinCluster(node=eachNode)
            if len(skinClusterNodes) :
                for skinClusterNode in skinClusterNodes :
                    matrixList = skinClusterNode.matrix.get(mi=True)
                    for index in matrixList :
                        inf = skinClusterNode.matrix[index].listConnections(s=True, d=False, scn=True)
                        if inf :
                            inverseMatrix = inf[0].worldInverseMatrix[0].get()
                            skinClusterNode.pm[index].set(inverseMatrix, type='matrix')

    def delBindPose(self) :
        bindPoseNodes = pm.ls(type='dagPose')
        for bindPoseNode in bindPoseNodes :
            bindPoseNode.set(lock=False)
            pm.delete(bindPoseNode)

    def renameSkinClusterName(self) :
        timeString = time.strftime("%Y%b%d%H%M", time.localtime())
        skinClusterNodes = pm.ls(type='skinCluster')
        for index,skinClusterNode in enumerate(skinClusterNodes) :
            skinClusterNode.rename("rig%s_%d_skinCluster" %(timeString, index))

    def removeUnusedInfluence(self, skinClusterNode) :
        allInfs = pm.skinCluster(skinClusterNode, q=True, inf=True)
        goodInfs = pm.skinCluster(skinClusterNode, q=True, wi=True)
        badInfs = list(set(allInfs).difference(set(goodInfs)))
        if len(badInfs) :
            pm.progressWindow(title='', progress=0, status='Remove Unused Influence...', 
                              isInterruptable=True, maxValue=len(badInfs))
            nodeState = skinClusterNode.nodeState.get()
            lockState = skinClusterNode.nodeState.get(lock=True)
            
            skinClusterNode.nodeState.set(1)
            skinClusterNode.nodeState.set(lock=False)

            amount = 0
            for badInf in badInfs :
                if pm.progressWindow(query=True, isCancelled=True) :
                    break
                skinClusterNode.removeInfluence(badInf)
                amount += 1
                pm.progressWindow(e=True, progress=amount)                
            pm.progressWindow(endProgress=1)
            skinClusterNode.nodeState.set(nodeState)
            skinClusterNode.nodeState.set(lock=lockState)

    def getShapeElement(self, shape=None, type=None) :
        if type == 'mesh' :
            countElement = shape.numVertices()
        elif type == 'nurbsSurface' :
            countElement = [shape.numCVsInU(), shape.numCVsInV()]            
        elif type == 'nurbsCurve' :
            countElement = shape.numCVs()
        elif type == 'lattice' :
            countElement = shape.getDivisions()
        else :
            pass
        return countElement

    def __exportSkinWeight(self, node=None, shape=None, type=None, 
                           skinClusterNode=None, exportPath=None, QWidget=None) :

        countElement = self.getShapeElement(shape=shape, type=type)

        mainInfluence = self.getInfluence(node=node, select=0)
        mainInfluenceList =[influence.name() for influence in mainInfluence]

        # - Mian Data Tree - #
        dataInfoTree = ElementTree()
        dataInfoMain = Element('dataInfoMain')
        dataInfoTree._setroot(dataInfoMain)

        # - Data Info - #
        dataInfoElement = Element('dataInfo')
        SubElement(dataInfoElement, 'Author', {'value': self.user})
        SubElement(dataInfoElement, 'Date', {'value': self.getTime()})
        SubElement(dataInfoElement, 'Maya', {'value': self.mayaVersion})
        dataInfoMain.append(dataInfoElement)

        # - Node Info - #
        nodeInfoElement = Element('nodeInfo')
        SubElement(nodeInfoElement, 'Node', {'value': str(node.name())})
        SubElement(nodeInfoElement, 'Type', {'value': str(type)})
        if type == 'mesh' or type == 'nurbsCurve':
            SubElement(nodeInfoElement, 'Element', {'value': str(countElement)})
        elif type == 'nurbsSurface' :
            SubElement(nodeInfoElement, 'Element', {'value': str(countElement[0]*countElement[1])})
        elif type == 'lattice' :
            SubElement(nodeInfoElement, 'Element', {'value': str(countElement[0]*countElement[1]*countElement[2])})
        else :
            pass
        SubElement(nodeInfoElement, 'Influence', {'value': str(mainInfluenceList)})
        dataInfoMain.append(nodeInfoElement)

        # - Data Vertex Weight - #
        dataElement = Element('dataElement')
        if type == 'mesh' :
            if QWidget != None :
                QWidget[0].setRange(0, countElement)
            for i in range(countElement) :
                influenceList = pm.skinPercent(skinClusterNode, 
                                               node.vtx[i], 
                                               ignoreBelow=self.IGNORE_VALUE, 
                                               query=True, 
                                               t=None)
                influenceIndexList = [mainInfluenceList.index(eachInfluence) for eachInfluence in influenceList]
                weightList = pm.skinPercent(skinClusterNode, 
                                            node.vtx[i], 
                                            ignoreBelow=self.IGNORE_VALUE, 
                                            query=True, 
                                            v=True)
                SubElement(dataElement, 'Vertex', {'index': str(i), 
                                                   'influence': str(influenceIndexList), 
                                                   'weight': str(weightList)})
                try :
                    QWidget[0].setValue(i+1)
                except : pass

        elif type == 'nurbsSurface' :
            if QWidget != None :
                QWidget[0].setRange(0, countElement[0]*countElement[1])
            i = 0
            for u in range(countElement[0]) :
                for v in range(countElement[1]) :
                    influenceList = pm.skinPercent(skinClusterNode, node.cv[u][v], ignoreBelow=self.IGNORE_VALUE, query=True, t=None)
                    influenceIndexList = [mainInfluenceList.index(eachInfluence) for eachInfluence in influenceList]
                    weightList = pm.skinPercent(skinClusterNode, node.cv[u][v], ignoreBelow=self.IGNORE_VALUE, query=True, v=True)
                    SubElement(dataElement, 'Vertex', {'index': str([u,v]), 'influence': str(influenceIndexList), 'weight': str(weightList)})
                    i += 1
                    try :
                        QWidget[0].setValue(i)
                    except :
                        pass
                      
        elif type == 'nurbsCurve' :
            if QWidget != None :
                QWidget[0].setRange(0, countElement)
            for i in range(countElement) :
                influenceList = pm.skinPercent(skinClusterNode, node.cv[i], ignoreBelow=self.IGNORE_VALUE, query=True, t=None)
                influenceIndexList = [mainInfluenceList.index(eachInfluence) for eachInfluence in influenceList]
                weightList = pm.skinPercent(skinClusterNode, node.cv[i], ignoreBelow=self.IGNORE_VALUE, query=True, v=True)
                SubElement(dataElement, 'Vertex', {'index': str(i), 'influence': str(influenceIndexList), 'weight': str(weightList)})

        elif type == 'lattice' :
            if QWidget != None :
                QWidget[0].setRange(0, countElement[0]*countElement[1]*countElement[2])
            i = 0
            for sd in range(countElement[0]) :
                for td in range(countElement[1]) :
                    for ud in range(countElement[2]) :
                       influenceList = pm.skinPercent(skinClusterNode, node.pt[sd][td][ud], ignoreBelow=self.IGNORE_VALUE, query=True, t=None)
                       influenceIndexList = [mainInfluenceList.index(eachInfluence) for eachInfluence in influenceList]
                       weightList = pm.skinPercent(skinClusterNode, node.pt[sd][td][ud], ignoreBelow=self.IGNORE_VALUE, query=True, v=True)
                       SubElement(dataElement, 'Vertex', {'index': str([sd,td,ud]), 'influence': str(influenceIndexList), 'weight': str(weightList)})
                       try :
                           QWidget[0].setValue(i+1)
                       except :
                        pass         
        else :
            pass
        dataInfoMain.append(dataElement)

        # - Write XML File - #
        exportPath = os.path.join(exportPath, (node.name().replace('|','#') + '[' + type + '].xml'))
        dataInfoTree.write(exportPath, 'utf-8')

    def exportSkinWeight(self, exportPath=None, QWidget=None) :
        if QWidget != None :
            QWidget[0].setValue(0)
        nodes = pm.selected(fl=True)
        if not len(nodes) :
            pm.displayWarning('nothing selected')
            return
        for node in nodes :
            nodeShape = node.getShape()
            if nodeShape != None :
                nodeShapeType = nodeShape.type()
                if nodeShapeType in self.OBJ_TYPE :
                    skinClusterNodes = self.getSkinCluster(node=node)
                    if len(skinClusterNodes) :
                        self.__exportSkinWeight(node=node, 
                                                shape=nodeShape, 
                                                type=nodeShapeType, 
                                                skinClusterNode=skinClusterNodes[0], 
                                                exportPath=exportPath, 
                                                QWidget=QWidget)
                        if QWidget != None :
                            QWidget[0].setValue(0)
                            newItem = QtWidgets.QListWidgetItem(QWidget[1])
                            newItem.linkType = 'weight'
                            newItem.linkPath = os.path.join(exportPath, (node.name().replace('|','#') + '[' + nodeShapeType + '].xml'))
                            newItem.linkName = node.name() + '[' + nodeShapeType + '].xml'
                            newItem.setText(node.name())
                            icon = QtGui.QIcon()
                            if nodeShapeType == 'mesh' :
                                icon.addPixmap(__pixmap__('icon_mesh'))
                            elif nodeShapeType == 'nurbsSurface' :
                                icon.addPixmap(__pixmap__('icon_surface'))
                            elif nodeShapeType == 'nurbsCurve' :
                                icon.addPixmap(__pixmap__('icon_curve'))
                            elif nodeShapeType == 'lattice' :
                                icon.addPixmap(__pixmap__('icon_lattice'))
                            newItem.setIcon(icon)
                    else :
                        pm.displayWarning('find no skinCluster on object %s'%node)
                else :
                    pm.displayWarning('object %s shape node not support'%node)
            else :
                pm.displayWarning('object %s has no shape'%node)

    def exportComponentsSkinWeight(self, exportPath=None, QWidget=None) :
        nodesTempList = []
        components = pm.selected(fl=True)
        if components :
            for component in components :
                nodeShape = component.node()
                if nodeShape not in nodesTempList :
                    nodesTempList.append(nodeShape)
        if len(nodesTempList) != 1 :
            pm.displayWarning('this method support only one obj components right now...')
            return

        if nodesTempList[0].type() not in self.OBJ_TYPE :
            pm.displayWarning('this method only support obj components...')
            return

        node = nodesTempList[0].getParent()
        type = nodesTempList[0].type()
        countElement = len(components)

        skinClusterNodes = self.getSkinCluster(node=node)
        if skinClusterNodes :
            if QWidget != None :
                QWidget[0].setRange(0, countElement)

            mainInfluence = self.getInfluence(node=node, select=False)
            mainInfluenceList =[influence.name() for influence in mainInfluence]
            
            # - Mian Data Tree - #
            dataInfoTree = ElementTree()
            dataInfoMain = Element('dataInfoMain')
            dataInfoTree._setroot(dataInfoMain)

            # - Data Info - #
            dataInfoElement = Element('dataInfo')
            SubElement(dataInfoElement, 'Author', {'value': self.user})
            SubElement(dataInfoElement, 'Date', {'value': self.getTime()})
            SubElement(dataInfoElement, 'Maya', {'value': self.mayaVersion})
            dataInfoMain.append(dataInfoElement)

            # - Node Info - #
            nodeInfoElement = Element('nodeInfo')
            SubElement(nodeInfoElement, 'Node', {'value': str(node.name())})
            SubElement(nodeInfoElement, 'Type', {'value': str(type)})
            SubElement(nodeInfoElement, 'Element', {'value': str(countElement)})
            SubElement(nodeInfoElement, 'Influence', {'value': str(mainInfluenceList)})
            dataInfoMain.append(nodeInfoElement)

            # - Data Vertex Weight - #
            dataElement = Element('dataElement')
            if type == 'mesh' :
                i = 0
                for component in components :
                    influenceList = pm.skinPercent(skinClusterNodes[0], 
                                                   component, 
                                                   ignoreBelow=self.IGNORE_VALUE, 
                                                   query=True, 
                                                   t=None)
                    influenceIndexList = [mainInfluenceList.index(eachInfluence) for eachInfluence in influenceList]
                    weightList = pm.skinPercent(skinClusterNodes[0], 
                                                component, 
                                                ignoreBelow=self.IGNORE_VALUE, 
                                                query=True, 
                                                v=True)
                    SubElement(dataElement, 'Vertex', {'index': str(component.currentItemIndex()), 
                                                       'influence': str(influenceIndexList), 
                                                       'weight': str(weightList)})
                    i += 1
                    try :
                        QWidget[0].setValue(i)
                    except : pass

            elif type == 'nurbsSurface' :
                i = 0
                for component in components :
                    influenceList = pm.skinPercent(skinClusterNodes[0], 
                                                   component, 
                                                   ignoreBelow=self.IGNORE_VALUE, 
                                                   query=True, 
                                                   t=None)
                    influenceIndexList = [mainInfluenceList.index(eachInfluence) for eachInfluence in influenceList]
                    weightList = pm.skinPercent(skinClusterNodes[0], 
                                                component, 
                                                ignoreBelow=self.IGNORE_VALUE, 
                                                query=True, 
                                                v=True)
                    SubElement(dataElement, 'Vertex',{'index': str([component.currentItemIndex()[0], component.currentItemIndex()[1]]), 
                                                      'influence': str(influenceIndexList), 
                                                      'weight': str(weightList)})                
                    i += 1
                    try :
                        QWidget[0].setValue(i)
                    except : pass

            elif type == 'nurbsCurve' :
                i = 0
                for component in components :
                    influenceList = pm.skinPercent(skinClusterNodes[0], 
                                                   component, 
                                                   ignoreBelow=self.IGNORE_VALUE, 
                                                   query=True, 
                                                   t=None)
                    influenceIndexList = [mainInfluenceList.index(eachInfluence) for eachInfluence in influenceList]
                    weightList = pm.skinPercent(skinClusterNodes[0], 
                                                component, 
                                                ignoreBelow=self.IGNORE_VALUE, 
                                                query=True, 
                                                v=True)
                    SubElement(dataElement, 'Vertex', {'index': str(component.currentItemIndex()), 
                                                       'influence': str(influenceIndexList), 
                                                       'weight': str(weightList)})   
                    i += 1
                    try :
                        QWidget[0].setValue(i)
                    except : pass

            elif type == 'lattice' :
                i = 0
                for component in components :
                    influenceList = pm.skinPercent(skinClusterNodes[0], component, ignoreBelow=self.IGNORE_VALUE, query=True, t=None)
                    influenceIndexList = [mainInfluenceList.index(eachInfluence) for eachInfluence in influenceList]
                    weightList = pm.skinPercent(skinClusterNodes[0],component,ignoreBelow=self.IGNORE_VALUE,query=True,v=True)
                    SubElement(dataElement, 'Vertex', {'index': str([component.currentItemIndex()[0], 
                                                                     component.currentItemIndex()[1], 
                                                                     component.currentItemIndex()[2]]), 
                                                       'influence': str(influenceIndexList), 
                                                       'weight': str(weightList)})  
                    i += 1
                    try :
                        QWidget[0].setValue(i)
                    except : pass

            dataInfoMain.append(dataElement)

            # - Write XML File - #
            exportPath = os.path.join(exportPath, (node.name().replace('|','#') + '[' + type + '].xml'))
            dataInfoTree.write(exportPath, 'utf-8')

            if QWidget != None :
                QWidget[0].setValue(0)
                newItem = QtWidgets.QListWidgetItem(QWidget[1])
                newItem.linkType = 'weight'
                newItem.linkPath = exportPath
                newItem.linkName = node.name() + '[' + type + '].xml'
                newItem.setText(node.name())
                icon = QtGui.QIcon()
                if type == 'mesh' :
                    icon.addPixmap(__pixmap__('icon_mesh'))
                elif type == 'nurbsSurface' :
                    icon.addPixmap(__pixmap__('icon_surface'))
                elif type == 'nurbsCurve' :
                    icon.addPixmap(__pixmap__('icon_curve'))
                elif type == 'lattice' :
                    icon.addPixmap(__pixmap__('icon_lattice'))
                newItem.setIcon(icon)
        else :
            pm.displayWarning('no skinCluster found %s' %node)

    def __importSkinWeight(self, node=None, type=None, skinClusterNode=None, 
                           influence=None, dataElement=None, QWidget=None) :
        count = 0
        for element in dataElement.getiterator('Vertex'):
            weightList = eval(element.attrib['weight'])
            influenceList = eval(element.attrib['influence'])
            index = eval(element.attrib['index'])

            skinPercentList = []
            for i,each in enumerate(influenceList) :
                skinPercentList.append([influence[each], weightList[i]])

            if type == 'mesh' :
                pm.skinPercent(skinClusterNode, node.vtx[index], transformValue=skinPercentList)

            elif type == 'nurbsSurface' :
                pm.skinPercent(skinClusterNode, node.cv[index[0]][index[1]], transformValue=skinPercentList)

            elif type == 'nurbsCurve' :
                pm.skinPercent(skinClusterNode, node.cv[index], transformValue=skinPercentList)

            elif type == 'lattice' :
                pm.skinPercent(skinClusterNode, node.pt[index[0]][index[1]][index[2]], transformValue=skinPercentList)
            else : pass
            count += 1
            if QWidget != None :
                QWidget[0].setValue(count)

    def importSkinWeight(self, method=None, weightFilePath=None, QWidget=None) :
        xmlTree = parse(weightFilePath)
        rootElement = xmlTree.getroot()
        nodeInfoElement = rootElement.find('nodeInfo')
        dataElement = rootElement.find('dataElement')
        _node = nodeInfoElement.find('Node').attrib['value']
        _type = nodeInfoElement.find('Type').attrib['value']
        _element = eval(nodeInfoElement.find('Element').attrib['value'])
        _influence = eval(nodeInfoElement.find('Influence').attrib['value'])

        if method == 'batch' :           
            if pm.objExists(_node) :
                node = pm.PyNode(_node)                
            else :
                pm.displayWarning('%s not found in sence'%_node)
                return

        elif method == 'single' :
            nodes = pm.selected()
            if len(nodes):
                node = nodes[0]
            else :
                pm.displayWarning('nothing selected')
                return 
        else :
            return

        shape = node.getShape()
        if shape :
            type = shape.type()
            if type == _type :
                skinClusterNodes = self.getSkinCluster(node)
                if len(skinClusterNodes) :
                    skinClusterNode = skinClusterNodes[0]
                else :
                    skinClusterNode = pm.skinCluster(_influence, node, sm=0, tsb=True)

                if QWidget != None :
                    QWidget[0].setValue(0)
                    QWidget[0].setRange(0, _element)

                self.__importSkinWeight(node=node, type=_type, skinClusterNode=skinClusterNode, 
                                        influence=_influence, dataElement=dataElement, QWidget=QWidget)
            else :
                pm.displayWarning('%s shape type not match '%node.name())
        else :
            pm.displayWarning('oject %s has no shape '%node.name())

    def getInfluenceFromWeightData(self, weightFilePath=None) :
        xmlTree = parse(weightFilePath)
        rootElement = xmlTree.getroot()
        badList = []
        for element in rootElement.getiterator('nodeInfo') :
            influences = eval(element.find('Influence').attrib['value'])
            pm.select(cl=True)
            for influence in influences :
                if not pm.objExists(influence) :
                    badList.append(influence)
            if len(badList) :
                print '%s not found in sence' %badList
            else :
                pm.select(influences, r=True)
