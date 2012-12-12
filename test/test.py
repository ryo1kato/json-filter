#!/usr/bin/env python

import unittest
import os

import json
import jsonfilter as jf

#
# mytest.json
# mytest@name1.name2[99].name3.json
# mytest@name1.name2[99].name3%leaf.json
#
#

testdatadir = os.path.dirname( __file__ )

def testdata(name):
    return os.path.join(testdatadir, name)

def load_testdata(name):
    return json.load( open(testdata(name)) )

test_json = load_testdata('test.json')
expected_json = load_testdata('test@hoge.var3.baz.json')
filtered, leaves = jf.dotdictget(test_json, 'hoge.var3.baz')

#print json.dumps(expected_json, indent=4)
#print '----------'
#print json.dumps(filtered, indent=4)

if expected_json == filtered:
    print "True"
else:
    print "False"
