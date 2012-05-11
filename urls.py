from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.static import serve
import protmusis.admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'protmusis.views.home', name='home'),
    # url(r'^protmusis/', include('protmusis.foo.urls')),

	url(r'^$', 'protmusis.collection.views.frontpage'),
	url(r'^logout$', 'protmusis.collection.views.logout'),
	url(r'^sync$', 'protmusis.collection.views.sync_state'),
	url(r'^image$', 'protmusis.collection.views.get_image'),
	url(r'^free-view$', 'protmusis.collection.views.free_view'),
	url(r'^free-view/state$', 'protmusis.collection.views.free_view_state'),
	
	url(r'^test$', 'protmusis.collection.views.test_view'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^{0}/(?P<path>.*)$'.format(settings.MEDIA_URL.strip('/')), serve, { 'document_root': settings.MEDIA_ROOT }),

# Uncomment the next line to enable the admin:
    url(r'^admin/', include(protmusis.admin.site.urls)),
)
