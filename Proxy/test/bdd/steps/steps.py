from lettuce import *
from nose.tools import assert_equal, assert_in
from proxy import *
import os

@step(u'Given I run proxy file')
def given_i_run_proxy_file(step):
    os.system('python proxy.py')

@step(u'When it finishes creating the main object')
def when_it_finishes_creating_the_main_object(step):
    assert True

@step(u'And after creating the references to that object')
def and_after_creating_the_references_to_that_object(step):
    assert True

@step(u'And then deletes the said references')
def and_then_deletes_the_said_references(step):
    assert True

@step(u'Then I can see the following:')
def then_i_can_see_the_following(step):
    file = open('myfile', 'r')
    for row in step.hashes: 
        n = file.readline().splitlines()
        assert_equal(n, row.values())
