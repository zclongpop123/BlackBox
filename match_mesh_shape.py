#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Fri, 08 Jan 2016, 14:22:19
#========================================
import pymel.core
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def match_mesh_shape(src, dst, sapce='object'):
    #- pymel
    src_pml_node = pymel.core.PyNode(src)
    dst_pml_node = pymel.core.PyNode(dst)

    #- api
    src_api_node = src_pml_node.__apiobject__()
    dst_api_node = dst_pml_node.__apiobject__()

    #- mfn
    src_mfn_node = OpenMaya.MFnMesh(src_api_node)
    dst_mfn_node = OpenMaya.MFnMesh(dst_api_node)

    #- get set points
    api_pnt_ary = OpenMaya.MPointArray()
    space_array = dict((('object', OpenMaya.MSpace.kObject), ('world', OpenMaya.MSpace.kWorld)))
    src_mfn_node.getPoints(api_pnt_ary, space_array.get(sapce, OpenMaya.MSpace.kObject))
    dst_mfn_node.setPoints(api_pnt_ary, space_array.get(sapce, OpenMaya.MSpace.kObject))