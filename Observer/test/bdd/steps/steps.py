from lettuce import *
from nose.tools import assert_equal, assert_in
from observer import *
import os

@step(u'Given I run observer file')
def given_i_run_observer_file(step):
    os.system('python observer.py')

@step(u'When it registers the usa and eu time observers')
def when_it_registers_the_usa_and_eu_time_observers(step):
    assert True

@step(u'Then I can see the following:')
def then_i_can_see_the_following(step):
    file = open('myfile', 'r')
    for row in step.hashes: 
        n = file.readline().splitlines()
        assert_equal(n, row.values())
