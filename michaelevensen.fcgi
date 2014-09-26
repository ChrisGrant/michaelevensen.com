#!/usr/local/bin/python
import sys, os

# Sti til hjemmekatalog
sys.path.append("/home/michaele/michaelevensen.com/michaelevensen")

from django.core.handlers.wsgi import WSGIHandler
from flup.server.fcgi import WSGIServer

# Sti til prosjektet som ble opprettet i punkt 2.
os.chdir("/home/michaele/michaelevensen.com/michaelevensen")

os.environ['DJANGO_SETTINGS_MODULE'] = 'michaelevensen.settings'

WSGIServer(WSGIHandler()).run()
