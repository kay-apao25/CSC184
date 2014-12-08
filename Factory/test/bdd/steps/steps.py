from lettuce import *
from nose.tools import assert_equal, assert_in
from factory import *
from afactory import *
import os

@step(u'Given I run factory file for http')
def given_i_run_factory_file_for_http(step):
    print os.system('python factory.py')

@step(u'When it finishes getting the files from the site')
def when_it_finishes_getting_the_files_from_the_site(step):
    assert True

@step(u'Then I can see the following files http:')
def then_i_can_see_the_following_files_http(step):
    file = open('myfile', 'r')
    for row in step.hashes: 
        n = file.readline().splitlines()
    	assert_equal(n, row.values())

@step(u'Given I run factory file for ftp')
def given_i_run_factory_file_for_ftp(step):
    print os.system('python factory.py')

@step(u'Then I can see the following files ftp:')
def then_i_can_see_the_following_files_ftp(step):
    file = open('myfile', 'r')
    for row in step.hashes: 
        n = file.readline().splitlines()
    	assert_equal(n, row.values())

 