#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 22:33
# @Author  : Leslee

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data,label,name):
    return data[label].get(name)

def store(data,fullname):
    names = fullname.split()
    if len(names) ==2:
        names.insert(1,'')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(fullname)
        else:
            data[label][name] = [fullname]

myName = {}
init(myName)
store(myName,'mage lie het')
print(lookup(myName,'middle','lie'))
