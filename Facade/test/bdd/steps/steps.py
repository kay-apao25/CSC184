from lettuce import *
from nose.tools import assert_equal, assert_in
from facade import *
import os

@step(u'Given I run facade file')
def given_i_run_facade_file(step):
    os.system('python facade.py')

@step(u'When it finishes checking the temperature of London from the site')
def when_it_finishes_checking_the_temperature_of_london_from_the_site(step):
    assert True
@step(u'Then I can see the temperature "([^"]*)"')
def then_i_can_see_the_temperature_group1(step, group1):
    file = open('myfile', 'r')
    for row in step.hashes: 
        n = file.readline().splitlines()
        assert_equal(n, row.values())
    
   
