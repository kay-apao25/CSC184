from lettuce import *
from nose.tools import assert_equal, assert_in
from observer import *
import os

@step(u'Given I run observer file')
def given_i_run_observer_file(step):
    os.system('python observer.py')

@step(u'When it registers the first observer and displays the 12-hour time format')
def when_it_registers_the_first_observer_and_displays_the_12_hour_time_format(step):
    assert True

@step(u'And it registers another server and displays both the 12-hour and 24-hour time format')
def and_it_registers_another_server_and_displays_both_the_12_hour_and_24_hour_time_format(step):
    assert True

@step(u'And then unregisters the first observer and display the 24-hour format')
def and_then_unregisters_the_first_observer_and_display_the_24_hour_format(step):
    assert True

@step(u'Then I can see the following:')
def then_i_can_see_the_following(step):
    file = open('myfile', 'r')
    for row in step.hashes: 
        n = file.readline().splitlines()
        assert_equal(n, row.values())
