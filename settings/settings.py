"""
Django框架设置

官方文档: https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

import pymysql

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-39i@_ouzvap6-v7al)u9-1=kjyw*%560=h4m%t9!!er%@*8#-t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
]

# 应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'application.apps.ApplicationConfig',
]

# DRF
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # request-body 解析器
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
    ],
    # 认证与授权
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'common.security.TokenBasedAuthenticator',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'common.security.RoleUser',
    ],
    'UNAUTHENTICATED_USER': lambda: None,
    'UNAUTHENTICATED_TOKEN': None,
    # 限流
    'DEFAULT_THROTTLE_CLASSES': [
        'common.security.NullThrottle',
    ],
    # 版本号获取器
    'DEFAULT_VERSIONING_CLASS': 'common.misc.Versioning',
    # 错误处理
    'EXCEPTION_HANDLER': 'common.exception.custom_exception_handler',
    # 其他
    'UNICODE_JSON': True,
    'COMPACT_JSON': False,
}

# 中间件
MIDDLEWARE = [
    'common.middleware.StdoutLoggingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', # 已禁用
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

# 页面模板
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'settings.wsgi.application'

# 关系型数据库
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'NAME': 'DjangoPlayground',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()

# 密码校检
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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

# I18n
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 静态资源
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'

# 默认模型主键类型
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
