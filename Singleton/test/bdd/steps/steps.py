from lettuce import *
from nose.tools import assert_equal, assert_in
from crawler import *
import os


@step(u'Given I run crawler file')
def given_i_run_crawler_file(step):
	print os.system('python crawler.py')

@step(u'When it finishes getting the images from the site')
def when_it_finishes_getting_the_images_from_the_site(step):
	assert True

@step(u'Then I can see the image "([^"]*)"')
def then_i_can_see_the_image_group1(step, group1):
    file = os.path.exists("/home/kay/Documents/Singleton/CSC184/Singleton/images/" + group1) 
    assert_equal(file, True)


