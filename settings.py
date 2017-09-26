#!/usr/bin/env python
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# #                 Django settings for OMERO.qa project.               # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
# Copyright (c) 2009 University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Aleksandra Tarkowska <A(dot)Tarkowska(at)dundee(dot)ac(dot)uk>, 2008.
#
# Version: 1.0
#

import os.path
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Debuging mode.
# A boolean that turns on/off debug mode.
# For logging configuration please change 'LEVEL = logging.INFO' below
#
# NEVER DEPLOY a site into production with DEBUG turned on.
DEBUG = False # handler404 and handler500 works only when False
TEMPLATE_DEBUG = DEBUG

# Configure logging and set place to store logs.
INTERNAL_IPS = ()
LOGGING_LOG_SQL = False

ADMINS = (
    # ('Admin name', 'admin email'),
)

MANAGERS = ADMINS

ENGINE = os.environ.get("ENGINE", "django.db.backends.postgresql_psycopg2")
DBNAME = os.environ.get("DBNAME", "feedback")
DBUSER = os.environ.get("DBNAME", "feedback")
DBPASS = os.environ.get("DBNAME", "feedback")
DBHOST = os.environ.get("DBNAME", "db")
DBPORT = os.environ.get("DBNAME", "5432")

DATABASES = {
    # 'default': {
    #     'ENGINE': ENGINE,    # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': DBNAME,      # Or path to database file if using sqlite3.
    #     'USER': DBUSER,      # Not used with sqlite3.
    #     'PASSWORD': DBPASS,  # Not used with sqlite3.
    #     'HOST': DBHOST,      # Set to empty string for localhost. Not used with sqlite3.
    #     'PORT': DBPORT,      # Set to empty string for default. Not used with sqlite3.
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data.sqlite3')
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(os.path.dirname(__file__), '..', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
# Make this unique, and don't share it with anybody.
SECRET_KEY = '52**!p9_e^oc9oa^6s)$wxidc-+3ahye76e_^a%eay_-%y!nxt'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # FIXME 'django.middleware.http.SetRemoteAddrFromForwardedFor',
)

ROOT_URLCONF = 'omero_qa.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'omero_qa.wsgi.application'

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (
    os.path.join(os.path.join(os.path.dirname(__file__), 'feedback'), 'templates').replace('\\','/'),
    os.path.join(os.path.join(os.path.dirname(__file__), 'qa'), 'templates').replace('\\','/'),
#    os.path.join(os.path.join(os.path.dirname(__file__), 'registry'), 'templates').replace('\\','/'),
#    os.path.join(os.path.join(os.path.dirname(__file__), 'validator'), 'templates').replace('\\','/'),
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',  # FIXME
    'omero_qa.qa',
    'omero_qa.feedback'
)
# Logging levels: logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR logging.CRITICAL
# FORMAT: 2010-01-01 00:00:00,000 INFO  [omeroweb.webadmin.webadmin_utils        ] (proc.1308 ) getGuestConnection:20 Open connection is not available

LOGDIR = os.path.join(os.path.dirname(__file__), '..', 'log')
if not os.path.isdir(LOGDIR):
    os.makedirs(LOGDIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)5.5s [%(name)40.40s] (proc.%(process)5.5d) %(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGDIR, 'OMEROqa.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGDIR, 'OMEROqa_request.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django.request': { # Stop SQL debug from logging to main logger
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django_auth_ldap': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
#    'django.contrib.auth.backends.ModelBackend',
)

FEEDBACK_URL = "qa.openmicroscopy.org.uk:80"

IGNORABLE_404_ENDS = ('*.ico')

PERPAGE = 25
# Cookies config
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # False
SESSION_COOKIE_AGE = 86400 # 1 day in sec (86400)
# We need to disable HttpOnly cookies because then plug-ins like the
# SWFUploader cannot get access to the session cookie.  Since Django 1.4
# the default is True.
#  * https://code.djangoproject.com/ticket/3304 (Add HttpOnly)
#  * https://code.djangoproject.com/ticket/16847 (HttpOnly = True; default)
# Thu Nov  8 11:36:14 GMT 2012 -- <callan@glencoesoftware.com>
SESSION_COOKIE_HTTPONLY = False

# file upload settings
FILE_UPLOAD_TEMP_DIR = '/tmp'
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440 #default 2621440

GEODAT = os.path.join(os.path.dirname(__file__), 'GeoLiteCity.dat').replace('\\','/')
GEOIP = os.path.join(os.path.dirname(__file__), 'GeoIP.dat').replace('\\','/')
GOOGLE_KEY = ""
GOOGLE_KEY2 = ""


# UPLOAD dir
UPLOAD_ROOT = "/ome/apache_repo"
# if not os.path.isdir(UPLOAD_ROOT):
#     try:
#         os.mkdir(UPLOAD_ROOT)
#     except Exception, x:
#         exctype, value = sys.exc_info()[:2]
#         raise exctype, value

VALIDATOR_UPLOAD_ROOT = "/Validator"
# if not os.path.isdir(VALIDATOR_UPLOAD_ROOT):
#     try:
#         os.mkdir(VALIDATOR_UPLOAD_ROOT)
#     except Exception, x:
#         exctype, value = sys.exc_info()[:2]
#         raise exctype, value

TESTNG_ROOT = "/TestNG"
# if not os.path.isdir(TESTNG_ROOT):
#     try:
#         os.mkdir(TESTNG_ROOT)
#     except Exception, x:
#         exctype, value = sys.exc_info()[:2]
#         raise exctype, value


OME_HUDSON_PATH = "/ome/hudson/jobs"

#Application Host
APPLICATION_HOST = "https://www.openmicroscopy.org/qa2"

# Application allows to notify user
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = '[OMERO.qa] '
EMAIL_USE_TLS = False
SERVER_EMAIL = 'qa@openmicroscopy.org.uk' # email address
SEND_BROKEN_LINK_EMAILS = False

DEMO_SERVER = {'host':'', 'port':4064, 'username':'', 'passwd':''}

# LDAP configuration options
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfUniqueNamesType
AUTH_LDAP_SERVER_URI = 'ldaps://'
AUTH_LDAP_USER_SEARCH = LDAPSearch('ou=,o=',
        ldap.SCOPE_SUBTREE, '(cn=%(user)s)')
AUTH_LDAP_GLOBAL_OPTIONS = {
        ldap.OPT_X_TLS_REQUIRE_CERT: ldap.OPT_X_TLS_NEVER,
}
AUTH_LDAP_GROUP_SEARCH = LDAPSearch('ou=,o=',
        ldap.SCOPE_SUBTREE, '(objectClass=groupOfUniqueNames)')
AUTH_LDAP_GROUP_TYPE = GroupOfUniqueNamesType(name_attr='cn')
AUTH_LDAP_REQUIRE_GROUP = 'cn=,ou=,o='
AUTH_LDAP_USER_ATTR_MAP = {
        'first_name': 'givenName',
        'last_name': 'sn',
	'email': 'mail',
}
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
        'is_staff': 'cn=,ou=,o=',
}
