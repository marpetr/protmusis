import os
import sys

sys.path.append('D:\\VS2011\\protmusis')
sys.path.append('D:\\VS2011')
os.environ['DJANGO_SETTINGS_MODULE'] = 'protmusis.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
