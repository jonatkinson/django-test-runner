import unittest

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.db.models import get_app, get_apps
from django.test.utils import setup_test_environment, teardown_test_environment
from django.test.simple import build_suite, build_test, reorder_suite
from django.test.testcases import OutputChecker, DocTestRunner, TestCase

# from test.util import HTMLTestRunner
from test import HTMLTestRunner

def index(request):
	"""
	The test index.
	"""
	
	# Get the installed apps for this project.
	installed_apps = settings.INSTALLED_APPS
		
	# Done.
	return render_to_response("test_index.html", {'installed_apps': installed_apps})
	
def run(request):
	"""
	Runs all the tests.
	"""

	# Some stuff.
	verbosity=1
	interactive=True
	extra_tests=[]

	# Setup the response.
	response = HttpResponse()

	# Get the installed apps for this project.
	installed_apps = settings.INSTALLED_APPS

	# The list of applications which will be tested.
	test_labels = []

	# Populate the test_labels list with the POST data.
	for item in request.POST.getlist('apps'):
		test_labels.append(settings.INSTALLED_APPS[int(item)])

	try:
		setup_test_environment()

		settings.DEBUG = False
		settings.DATABASE_ENGINE = 'sqlite3'
		suite = unittest.TestSuite()

		if test_labels:
			for label in test_labels:
				if '.' in label:
					suite.addTest(build_test(label))
				else:
					app = get_app(label)
					suite.addTest(build_suite(app))
		else:
			for app in get_apps():
				suite.addTest(build_suite(app))

		for test in extra_tests:
			suite.addTest(test)

		suite = reorder_suite(suite, (TestCase,))

		old_name = settings.DATABASE_NAME
		from django.db import connection
		connection.creation.create_test_db(verbosity, autoclobber=not interactive)
		result = HTMLTestRunner.HTMLTestRunner(stream=response, verbosity=verbosity).run(suite)
		connection.creation.destroy_test_db(old_name, verbosity)

		teardown_test_environment()
	except Exception, e:
		from ipdb import set_trace; set_trace()
		raise e

	return response