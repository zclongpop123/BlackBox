#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Thu, 27 Aug 2015, 17:21:26
#========================================
import pymel.core
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def deleteDefaultDagNode(object_name):
    api_node = pymel.core.PyNode(object_name).__apimobject__()
    api_tool = OpenMaya.MDagModifier()

    api_tool.deleteNode(api_node)
