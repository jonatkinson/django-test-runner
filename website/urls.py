from os import path
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	# Recorder and player.
	(r'^test/', include('test.urls')),

)
