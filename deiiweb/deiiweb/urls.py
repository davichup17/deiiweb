"""deiiweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.api.api import UserAPI
from django.conf import settings
from apps.manager_templates.urls import templates_patterns
from apps.report.urls import reports_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.registration.urls')),
    # Paths de Api
    path('api/1.0/created_user/', UserAPI.as_view(), name = "api_create_user"),
    path('templates/', include(templates_patterns)),
    path('reports/', include(reports_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
