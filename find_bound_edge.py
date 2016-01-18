#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Mon, 18 Jan 2016, 15:29:35
#========================================
import pymel.core
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def find_bound_edge(geometry):
    '''
    find polygon's bound edge...
    '''
    geo_pml_node = pymel.core.PyNode('geometry')
    geo_dag_path = geo_pml_node.__apiobject__()

    face_int_array = OpenMaya.MIntArray()
    iterator = OpenMaya.MItMeshEdge(geo_pml_node.__apiobject__())

    api_sign_comp = OpenMaya.MFnSingleIndexedComponent()
    api_edge_comp = vertSelection.create(OpenMaya.MFn.kMeshEdgeComponent)

    while not iterator.isDone():
        iterator.getConnectedFaces(face_int_array)

        if face_int_array.length() < 2:
            vertSelection.addElement(iterator.index())

        iterator.next()

    api_sel_list = OpenMaya.MSelectionList()
    api_sel_list.add(geo_dag_path, api_edge_comp)

    OpenMaya.MGlobal.setActiveSelectionList(api_sel_list)