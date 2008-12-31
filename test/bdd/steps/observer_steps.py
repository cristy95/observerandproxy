from lettuce import step
from nose.tools import assert_equal
from observer import *
import os

subject = Subject()
myfile = open('MyFile', 'r')

@step(u'observer.py is running')
def given_observer_py_is_running(step):
	os.system('python observer.py')
	assert True

@step(u'When the processes are done')
def when_the_processes_are_done(step):
	assert True

@step(u'Then I should see the following:')
def then_i_should_see_the_following(step):
	for row in step.hashes:
		a = myfile.readline().splitlines()
		assert_equal(a, row.values())