from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'test.views.index', name="test_index"),
	url(r'^run/$', 'test.views.run', name="test_run"),
)
