#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Thu, 14 Jan 2016, 11:15:49
#========================================
import pymel.core
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def find_intersect_vertex(obj_A, obj_b):
    '''
    '''
    src_pml_node = pymel.core.PyNode(obj_A)
    dst_pml_node = pymel.core.PyNode(obj_b)

    src_dag_path = src_pml_node.__apiobject__()
    dst_dag_path = dst_pml_node.__apiobject__()

    src_mfn_node = OpenMaya.MFnMesh(src_dag_path)
    iterator     = OpenMaya.MItGeometry(dst_dag_path)

    comp_list = list()
    closest_point = OpenMaya.MPoint()
    farray = OpenMaya.MFloatPointArray()

    point = OpenMaya.MFloatPoint()
    for i in xrange(iterator.count()):
        current_point = iterator.position(OpenMaya.MSpace.kWorld)
        src_mfn_node.getClosestPoint(current_point, closest_point, OpenMaya.MSpace.kWorld)

        point.setCast(current_point)
        vector = OpenMaya.MFloatVector(closest_point)

        farray.clear()
        src_mfn_node.allIntersections(point, vector, None, None,
                                      False, OpenMaya.MSpace.kWorld,
                                      10000, False, None, False,
                                      farray, None, None, None, None, None)

        if farray.length() % 2 == 1:
            comp_list.append(iterator.index())
        iterator.next()

    api_util = OpenMaya.MScriptUtil()
    api_util.createFromList(comp_list, len(comp_list))
    int_ptr  = api_util.asIntPtr()
    id_array = OpenMaya.MIntArray(int_ptr, len(comp_list))

    single_components = OpenMaya.MFnSingleIndexedComponent()
    vertex_components = single_components.create(OpenMaya.MFn.kMeshVertComponent)
    single_components.addElements(id_array)

    mSelectionList = OpenMaya.MSelectionList()
    mSelectionList.add(dst_dag_path, vertex_components)
    OpenMaya.MGlobal.setActiveSelectionList(mSelectionList)


if __name__ == '__main__':
    find_intersect_vertex('pSphere1', 'pSphere2')