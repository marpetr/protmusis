from django.contrib.admin import sites
from django.contrib.auth import admin as auth_admin
import admincp.urls

class MyAdminSite(sites.AdminSite):
	index_template = 'myadmin/index.html'
	
	def get_urls(self):
		urls = super(MyAdminSite, self).get_urls()
		return admincp.urls.urlpatterns + urls

site = MyAdminSite()

site.register(auth_admin.User, auth_admin.UserAdmin)
