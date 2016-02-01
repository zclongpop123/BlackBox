#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Mon, 01 Feb 2016, 17:43:53
#========================================
import pymel.core
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def get_all_anim_nodes(input_node):
    '''
    find all of anim curves on node history...
    '''
    node_mel_instance = input_node
    node_pml_instance = pymel.core.PyNode(node_mel_instance)
    node_api_instance = node_pml_instance.__apimobject__()

    dg_iterator = OpenMaya.MItDependencyGraph(node_api_instance, OpenMaya.MItDependencyGraph.kUpstream, OpenMaya.MItDependencyGraph.kPlugLevel)
    while not dg_iterator.isDone():
        item_obj = dg_iterator.currentItem()
        item_mfn = OpenMaya.MFnDependencyNode(item_obj)

        if item_obj.hasFn(OpenMaya.MFn.kAnimCurve):
            yield item_mfn.name()

        dg_iterator.next()