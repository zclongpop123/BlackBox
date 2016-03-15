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
    geo_pml_node = pymel.core.PyNode(geometry)
    geo_dag_path = geo_pml_node.__apiobject__()

    api_sign_comp = OpenMaya.MFnSingleIndexedComponent()
    api_edge_comp = api_sign_comp.create(OpenMaya.MFn.kMeshEdgeComponent)

    script_util = OpenMaya.MScriptUtil()
    connect_face_count_ptr = script_util.asIntPtr()

    iterator = OpenMaya.MItMeshEdge(geo_pml_node.__apiobject__())
    while not iterator.isDone():
        iterator.numConnectedFaces(connect_face_count_ptr)

        connect_face_count = OpenMaya.MScriptUtil(connect_face_count_ptr).asInt()
        if connect_face_count < 2:
            api_sign_comp.addElement(iterator.index())

        iterator.next()

    api_sel_list = OpenMaya.MSelectionList()
    api_sel_list.add(geo_dag_path, api_edge_comp)

    OpenMaya.MGlobal.setActiveSelectionList(api_sel_list)
