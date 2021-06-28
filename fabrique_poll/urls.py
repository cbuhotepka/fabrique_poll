from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.urls.conf import re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('poll_app.urls')),
]
