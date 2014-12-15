from lettuce import *
from nose.tools import assert_equal
import os

@step(u'Given I run template file')
def given_i_run_template_file(step):
    os.system('python template.py')

@step(u'When it has already gathered the top news from Google and Yahoo')
def when_it_has_already_gathered_the_top_news_from_google_and_yahoo(step):
    assert True

@step(u'The I can see the following:')
def the_i_can_see_the_following(step):
    assert True
