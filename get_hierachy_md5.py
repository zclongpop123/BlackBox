#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Sun, 17 Jan 2016, 10:25:48
#========================================
import md5, pymel.core
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def get_hierachy_md5(group_name, ignoreShape=True):
    '''
    '''
    MD5 = md5.new()
    geo_grp_pml_node = pymel.core.PyNode(group_name)
    geo_grp_api_node = geo_grp_pml_node.__apimobject__()


    dag_iterator = OpenMaya.MItDag()
    if ignoreShape:
        dag_iterator.reset(geo_grp_api_node, OpenMaya.MItDag.kDepthFirst, OpenMaya.MFn.kTransform)
    else:
        dag_iterator.reset(geo_grp_api_node, OpenMaya.MItDag.kDepthFirst)


    while not dag_iterator.isDone():
        MD5.update('{0}'.format(dag_iterator.depth()))
        MD5.update('{0}'.format(dag_iterator.partialPathName()))
        dag_iterator.next()

    return MD5.hexdigest()
