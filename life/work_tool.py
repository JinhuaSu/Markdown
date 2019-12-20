import time
import pandas as pd
import pickle
import argparse
class mission(object):
    def __init__(self,id,args):
        self.id = id
        self.name = args['name']
        self.root = args['root']
        self.content = args['content']
        self.ddl = args['ddl']
        self.importance = args['importance']
        self.tag = args['tag']
        self.s = self.report()
    def report(self):
        s = \
"""
----mission info-----\n
id:{id}|tag:{tag}\n
ddl:{ddl}|importance:{importance}\n
root:{root}\n
name:{name}\n
content:\n{content}\n
---------------------\n
""".format(id=self.id,tag=self.tag,ddl=self.ddl,\
           importance=self.importance,root=self.root,\
           name=self.name,content=self.content)
        return s
    def __str__(self):
        return self.s
class to_do_manager(object):
    """
    focus on the soft happen mission
    if it is explicit has a start time and last time, 
    just write down it on your calendar or make up a clock.
    to-do-manager target on the soft-ddl mission.
    yes it can be split into several subtask if ddl is on time.
    """
    def __init__(self):
        self.work_flow = {}
        self.id_count = 0
    def order(self,tag):
        self.work_flow[tag].sort(key = lambda x:x.importance)
    def get_mission(self,**kwargs):
        keys = ['root', 'tag', 'name', 'importance', 'content', 'ddl']
        values = [-1,'trifle','',0,'',None]
        default = dict(zip(keys,values))
        for key,value in kwargs.items():
            default[key] = value
        if default['tag'] in self.work_flow.keys():
            self.work_flow[default['tag']].append(mission(self.id_count,default))
            self.order(default['tag'])
        else:
            self.work_flow[default['tag']] = [mission(self.id_count,default)]
        self.id_count += 1
    def show_to_do(self,tag):
        print(self.work_flow[tag][-1])
    def to_do(self,tag,how,*args):
        assert how in ['sub','sure','unsure']
        if how == 'sure':
            print(self.work_flow[tag].pop())
        elif how == 'unsure':
            self.show_to_do(tag)
        elif how == 'sub':
            m = self.work_flow[tag].pop()
            for kwargs in args:
                kwargs['root'] = m.name
                kwargs['tag'] = m.tag
                kwargs['id'] = self.id_count
                self.id_count += 1
                if 'ddl' not in kwargs.keys():
                    kwargs['ddl'] = m.ddl
                if 'importance' not in kwargs.keys():
                    kwargs['importance'] = m.importance
                self.get_mission(**kwargs)
    def show_to_do_list(self,tag):
        for i in range(-1,-(len(self.work_flow[tag])+1),-1):
            print(self.work_flow[tag][i])
    def manage_order(self,id,importance):
        for tag in self.work_flow.keys():
            for i in range(len(self.work_flow[tag])):
                if self.work_flow[tag][i].id == id:
                    self.work_flow[tag][i].importance = importance
                    self.work_flow[tag][i].s = self.work_flow[tag][i].report()
                    self.order(tag)
                    return True
        return False