from django.conf import settings

DATA_DIR = settings.django_sec_DATA_DIR = getattr(
    settings,
    'django_sec_DATA_DIR',
    '/tmp/django_sec')

DEFAULT_FILE_STORAGE = 'sec_http_storage.FallbackStorage'

FALLBACK_STORAGE_URL = 'http://www.sec.gov/Archives'

MEDIA_ROOT = '/sec_files/'
