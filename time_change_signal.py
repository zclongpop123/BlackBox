#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Wed, 23 Sep 2015, 14:36:18
#========================================
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def func(*args):
    print "time triggered..."

#- create time change signal, 3 is 3 seconds, you can input a float number...
time_event_id = OpenMaya.MTimerMessage.addTimerCallback (3, func)

#- delete it, don't run this with up codes..
OpenMaya.MMessage.removeCallback(time_event_id)