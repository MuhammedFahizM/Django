from __future__ import absolute_import,unicode_literals
import os
from celery import Celery




  # Set default Django settings in module

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'celery_project.settings')

app = Celery('celery_project')


# Load configg from Django settings,using CELERY namespace

app.config_from_object('django.conf:settings',namespace = 'CELERY')

#Discover tasks in registered Django apps

@app.task(bind=True)

def debug_task(self):
    print(f"Request: {self.request!r}")