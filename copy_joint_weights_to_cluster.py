#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 15 Mar 2016, 15:57:52
#========================================
import pymel.core
import maya.cmds as mc
from maya import OpenMaya, OpenMayaAnim
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def copy_joint_weights_to_cluster(skin_mel_node, joint_mel_node):
    '''
    '''
    #- initlize api nodes
    skin_mfn_node  = OpenMayaAnim.MFnSkinCluster(pymel.core.PyNode(skin_mel_node).__apiobject__())
    joint_dag_path = OpenMaya.MDagPath(pymel.core.PyNode(joint_mel_node).__apiobject__())

    #- get joint influcenced points and weight values
    components = OpenMaya.MSelectionList()
    weights    = OpenMaya.MDoubleArray()
    skin_mfn_node.getPointsAffectedByInfluence(joint_dag_path, components, weights)

    #- create cluster
    component_strings = list()
    components.getSelectionStrings(component_strings)
    cluster_mel_node = mc.cluster(component_strings)[0]
    clus_mfn_node  = OpenMayaAnim.MFnWeightGeometryFilter(pymel.core.PyNode(cluster_mel_node).__apiobject__())

    #- get geometry's dagpath and component
    geo_dag_path = OpenMaya.MDagPath()
    geo_comp_obj = OpenMaya.MObject()
    components.getDagPath(0, geo_dag_path, geo_comp_obj)

    #- convert skinweights type to cluster weights type
    cluster_weights_array = OpenMaya.MFloatArray()
    for v in weights:
        cluster_weights_array.append(v)

    #- set weights
    clus_mfn_node.setWeight(geo_dag_path, geo_comp_obj, cluster_weights_array)


if __name__ == '__main__':
    copy_joint_weights_to_cluster('skinCluster1', 'joint1')
