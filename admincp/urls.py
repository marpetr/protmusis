from django.conf.urls.defaults import patterns, include, url
import protmusis.admin

urlpatterns = patterns('protmusis.admincp.views',
	url(r'^controlpanel/$', 'controlpanel', name='admincp_index'),
	url(r'^controlpanel/(\d+)/$', 'controlpanel', name='admincp_index_wqnum'),
	url(r'^controlpanel/show_question$', 'show_question', name='admincp_show_question'),
	url(r'^controlpanel/hide_question$', 'hide_question', name='admincp_hide_question'),
	url(r'^controlpanel/get_image/(\d+)$', 'get_question_image', name='admincp_get_image'),
	url(r'^controlpanel/put_static_image', 'put_static_image', name='admincp_put_static_image'),
)
