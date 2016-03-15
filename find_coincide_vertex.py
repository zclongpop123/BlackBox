#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Sun, 06 Sep 2015, 11:23:26
#========================================
import md5
import maya.cmds as mc
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def findCoincideVertex(geometry):
    #-
    pointCount = mc.polyEvaluate(geometry, v=True)
    posidict  = dict()
    for i in range(pointCount):
        ps = mc.xform('%s.vtx[%d]'%(geometry, i), q=True, ws=True, t=True)

        MD5 = md5.new()
        MD5.update('%f%f%f'%(ps[0], ps[1], ps[2]))
        posidict.setdefault(MD5.hexdigest(), list()).append('%s.vtx[%d]'%(geometry, i))

    #-
    res = list()
    for v in posidict.itervalues():
        if len(v) < 2:
            continue
        res.extend(v)

    #-
    mc.select(res)
