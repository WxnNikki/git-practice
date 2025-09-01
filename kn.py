# Application definition

INSTALLED_APPS = [
    "django.contrib.admin"             ,
    "django.contrib.auth"              ,
    "polymorphic"                      ,
    "django.contrib.contenttypes"      ,
    "django.contrib.sessions"          ,
    "django.contrib.messages"          ,
    "django.contrib.staticfiles"       ,
    "planting_guide"                   ,
    "assetMaintenance"                 ,
    "assetManagement"                  ,
    "assetExpenses"                    ,
    "assetOperation"                   ,
    "UserAuth"                         ,
    "Settings"                         ,
    "crispy_forms"                     ,
    "crispy_bootstrap4"                ,
    "FarmAcc"                          ,
    "Tasks"                            ,
    "Emergency"                        ,
    "Dashboard"                        ,
    "django_extensions"                ,
    "dashing"                          ,
    "django_cleanup.apps.CleanupConfig" # This is used to delete media files upon deletion of a model instance
]
