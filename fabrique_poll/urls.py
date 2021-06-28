from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('poll_app.urls')),
]
