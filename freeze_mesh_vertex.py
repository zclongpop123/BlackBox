#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Fri, 08 Jan 2016, 14:55:38
#========================================
import pymel.core
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def freeze_mesh_vertex(src, space='object'):
    #- pymel
    src_pml_node = pymel.core.PyNode(src)

    #- api
    src_api_node = src_pml_node.__apiobject__()

    #- mfn
    src_mfn_node = OpenMaya.MFnMesh(src_api_node)
    dst_mfn_node = OpenMaya.MFnMesh()

    #- space
    space_array = dict((('object', OpenMaya.MSpace.kObject), ('world', OpenMaya.MSpace.kWorld)))

    #- args
    geo_vtx_count            = src_mfn_node.numVertices()
    geo_face_count           = src_mfn_node.numPolygons()
    geo_pnt_ary              = OpenMaya.MPointArray()
    geo_face_pnt_ary         = OpenMaya.MIntArray()
    geo_face_pnt_connect_ary = OpenMaya.MIntArray()

    #- points
    src_mfn_node.getPoints(geo_pnt_ary, space_array.get(space, OpenMaya.MSpace.kObject))

    #- faces
    temp_in_ary = OpenMaya.MIntArray()
    for i in range(geo_face_count):
        points = src_mfn_node.getPolygonVertices(i, temp_in_ary)

        geo_face_pnt_ary.append(len(temp_in_ary))
        geo_face_pnt_connect_ary += temp_in_ary

    #- create
    dst_mfn_node.create(geo_vtx_count, geo_face_count, geo_pnt_ary, geo_face_pnt_ary, geo_face_pnt_connect_ary)
