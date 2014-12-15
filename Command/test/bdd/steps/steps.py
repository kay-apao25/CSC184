from lettuce import *
from nose.tools import assert_equal
import os

@step(u'Given I run command file')
def given_i_run_command_file(step):
    os.system('python command.py')

@step(u'When it creates and deletes a file')
def when_it_creates_and_deletes_a_file(step):
    assert True

@step(u'The I can see the following:')
def the_i_can_see_the_following(step):
    file = open('myFile', 'r')
    for row in step.hashes:
        n = file.readline().splitlines()
        assert_equal(n, row.values())