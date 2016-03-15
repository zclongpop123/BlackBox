#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Fri, 21 Aug 2015, 10:32:44
#========================================
import pymel.core
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def unlockReferencedAttr(attribute):
    pml_attr = pymel.core.PyNode(attribute)
    api_attr = pml_attr.__apimplug__()

    #-
    api_attr.setKeyable(True)
    api_attr.setLocked(False)
