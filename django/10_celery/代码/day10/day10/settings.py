"""
Django settings for day10 project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from celery.schedules import crontab
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1c7o@sw)0!96=krt8y@u9rvx&w+de!i-(+5=(nwp4n6(=)zk$1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App.apps.AppConfig',
    # celery配置
    'celery',
    'django_celery_results',
    'djcelery'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'day10.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'day10.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'day10',
        'HOST':'127.0.0.1',
        'USER':'root',
        'PASSWORD':'123',
        'PORT':3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# celery配置
BROKER_URL='redis://localhost:6379/5'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'              # 任务序列化和反序列化使用json
CELERY_RESULT_SERIALIZER = 'json'            # 结果序列化为json

# celery定时任务配置
# CELERYBEAT_SCHEDULE = {
#     'schedule-test': {
#         'task': 'App.tasks.hello',
#         'schedule': timedelta(seconds=3),
#
#     },
#
# }

# 计划任务（定点执行）


CELERYBEAT_SCHEDULE = {
    "every-ten-second-run-my_task": {
        "task": "App.tasks.fib",
        "schedule": crontab(minute="01", hour="15"),
        "args": (10,)
    }
}


# 邮件配置
# smtp服务的邮箱服务器
EMAIL_HOST = 'smtp.126.com'
# smtp服务固定的端口是25
EMAIL_PORT = 25   # 也有可能是465
#发送邮件的邮箱
EMAIL_HOST_USER = 'landmark_csl@126.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'csl111'
#收件人看到的发件人 <此处要和发送邮件的邮箱相同>
EMAIL_FROM = 'python<landmark_csl@163.com>'

import djcelery

djcelery.setup_loader()


