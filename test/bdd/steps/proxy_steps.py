from lettuce import step
from nose.tools import assert_equal
import os

@step(u'Given an object is created and I run the proxy python file')
def given_an_object_is_created_and_i_run_the_proxy_python_file(step):
    os.system('python proxy.py')

@step(u'When It finishes the processes')
def when_it_finishes_the_processes(step):
    assert True

@step(u'Then I should see the following number of references and count of objects deleted:')
def then_i_should_see_the_following_number_of_references_and_count_of_objects_deleted(step):
    pfile = open('ProxyFile', 'r')
    for row in step.hashes:
    	a = pfile.readline().splitlines()
    	assert_equal(a, row.values())
