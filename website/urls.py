from os import path
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	# Home page
	url(r'^/?$', direct_to_template, {'template': 'index.html'}, name="index"),

	# robots.txt.
	url(r'^robots.txt$', direct_to_template, {'template': 'robots.txt'}, name="robots"),

	# Static folder.
	url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': path.abspath(path.dirname(__file__)) + '/static', 'show_indexes': True}),

	# Admin stuff.
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
