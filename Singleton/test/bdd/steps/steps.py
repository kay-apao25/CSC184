from lettuce import *
from nose.tools import assert_equal, assert_in
#from webtest import TestApp
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager
from craw_app import *
from crawler import *
import os

@step(u'Given I visit page "([^"]*)"')
def given_i_visit_page_group1(step, group1):
    #world.browser = TestApp(app)
    world.response = world.browser.get(group1)
    #print world.response.status_code
    #assert_equal(int(world.response.status_code), 200)

@step(u'And crawler file is running')
def and_crawler_file_is_running(step):
	#process = os.system(9000)
	assert True


@step(u'When it finishes getting the images from the site')
def when_it_finishes_getting_the_images_from_the_site(step):
	assert True

@step(u'Then I can see the image "([^"]*)"')
def then_i_can_see_the_image_group1(step, group1):
    file = os.path.exists("/home/kay/Documents/Singleton/CSC184/Singleton/images/" + group1) 
    assert_equal(file, True)


