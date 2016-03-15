#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Thu, 20 Aug 2015, 17:16:32
#========================================
import pymel.core
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
def renameReadOnlyNode(oldName, newName):
    #- convert node to api node
    pml_node = pymel.core.PyNode(oldName)
    api_node = pml_node.__apiobject__()

    #- we need MObject, if it is MDagPath, convert to MObject
    if isinstance(api_node, maya.OpenMaya.MDagPath):
        api_node = api_node.node()

    #- use depencyNode to rename node
    api_dependencyNode = OpenMaya.MFnDependencyNode(api_node)
    api_dependencyNode.setName(newName)
