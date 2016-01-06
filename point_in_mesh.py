#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Wed, 06 Jan 2016, 18:24:24
#========================================
import pymel.core
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
# http://stackoverflow.com/questions/18135614/querying-of-a-point-is-within-a-mesh-maya-python-api

def pointInMesh(obj, point=(0.0, 0.0, 0.0), direction=(0.0, 0.0, 1.0)):

    obj_dag_path = OpenMaya.MDagPath.getAPathTo(pymel.core.PyNode(obj).__apimobject__())
    obj_mfn_node = OpenMaya.MFnMesh(obj_dag_path)

    api_point     = OpenMaya.MFloatPoint(*point)
    api_direction = OpenMaya.MFloatVector(*direction)
    farray = OpenMaya.MFloatPointArray()

    obj_mfn_node.allIntersections(api_point, api_direction,
                                  None, None,
                                  False, OpenMaya.MSpace.kWorld,
                                  10000, False,
                                  None, # replace none with a mesh look up accelerator if needed
                                  False,
                                  farray,
                                  None, None,
                                  None, None,
                                  None
                                  )

    return farray.length()%2 == 1