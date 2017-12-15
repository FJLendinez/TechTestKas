#Cambios en la configuración

Aquí hay poco que explicar!!

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'API'
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]


```

Documentar cansa mucho

![tired](img/tired.jpg)