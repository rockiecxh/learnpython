
#!/usr/bin/env python
#-*- encoding:UTF-8 -*-

import os, sys, gzip, time, optparse, itertools, datetime, heapq, operator
from operator import itemgetter
from heapq import *
from math import *
from collections import defaultdict, namedtuple

earth_radius=6378.137 * 1000 # Unit in meter

def rad(d):
	""" convert degree to radian """
	return d * pi / 180.0;

# calculate the distance between to coordinates
def distance(lat1, lng1, lat2, lng2):
    radlat1=rad(lat1)
    radlat2=rad(lat2)
    a=radlat1-radlat2
    b=rad(lng1)-rad(lng2)
    s=2*asin(sqrt(pow(sin(a/2),2)+cos(radlat1)*cos(radlat2)*pow(sin(b/2),2)))

    s=s*earth_radius
    return abs(s)

print distance(37.5077724, 127.0565523, 37.50753185, 127.0560124)

# convert a date to int in milliseconds
def datetime2timestamp(date, pattern):
    timeArray = time.strptime(date, pattern)
    return int(time.mktime(timeArray))

# a function to define a enum
def enum(*sequential, **named):
    enums = dict((x, i) for i, x in enumerate(sequential), **named)
    return type('Enum', (), enums)
# define the enum
State = enum('STOP', 'RUN')

print(State.STOP)

print(isinstance(State.STOP , State))
a=State.STOP
b=State.STOP

def isStop(a):
    return a == State.STOP


print(isStop(a))

# sample

now = "2015-07-24 09:53:21"
then = "2015-07-24 09:53:31"

# calculate the time diff
nowt = datetime2timestamp(now, "%Y-%m-%d %H:%M:%S")
thent = datetime2timestamp(then, "%Y-%m-%d %H:%M:%S")
print thent - nowt

# define a dict of list
d = defaultdict(list)
d['a'].append('a')
d['a'].append('b')
d['b'].append('b')

print "length of defaultdict is %s" % len(d)

# generate a list of STOP | RUN | STOP | RUN ...
states=[]
for x in range(5):
    states.append((x, State.RUN if x % 2 == 1 else State.STOP))

def args_to_tuple(lst):
    it = iter(map(float, lst.split()))
    return [(item, next(it)) for item in it]

print states, len(states)

# composite a (0,1),(2,3),(4,5) tuple list
offset=0
for x in zip(states[offset::2], states[offset+1::2]):
    print x
    print "%s, %s" % (x[0], x[1])

# get all combinations of (x, y, z) with offsets 0,1,2
tl=[(x,y,z) for x in states[0::2] for y in states[1::2] for z in states[2::2]]
for x in tl:
    print x
# get all the indexes of (0,2,4,6,...)
indexes=[x*2+offset for x in range(len(states)/2) if x*2+2 < len(states) - offset]
print "indexes: %s" % indexes

result=[]
for x in indexes:
    print "offset: %s,%s,%s" % (x, x+1, x+2)
    result.append((states[x], states[x+1], states[x+2]))
    print result

for (x, y, z) in result:
    print "x:%s, y:%s, z:%s)" % (x, y, z)

tl=[(x,y,z) for x in states[0::2] for y in states[1::2] for z in states[2::2]]
for x in tl:
    #print x
    pass

class Invoice(object):
    """docstring for Invoice"""
    def __init__(self, (line, text)):
        self.line=line
        #self.text=text
        (
            self.invoiceNumber,
            self.workerId,
            self.lat,
            self.lng
        )=(part.strip() for part in text.split(delimiter))

    def key(self):
        return self.invoiceNumber

    def __str__(self):
        return "{invoiceNumber: %s, workerId: %s, lat: %s, lng: %s}" % (self.invoiceNumber, self.workerId, self.lat, self.lng)

delimiter='|'
invoice = Invoice(('1','|'.join( ['invoiceNumber','workerId','lat','lng'] )))
if invoice:
    print invoice






