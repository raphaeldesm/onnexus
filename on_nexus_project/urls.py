"""
URL configuration for on_nexus_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('explore/', include('explore.urls')), # Aponta para o app de exploração)
    path('cursos/', include('courses.urls')), # Aponta para o app de cursos
    path('users/', include('users.urls')), # Aponta para o app de usuários
    path('payments/', include('payments.urls')), # Aponta para o app de pagamentos
    path('', include('home.urls')), # Aponta para o app de home
]

# Para servir arquivos estáticos e de mídia (uploads) em desenvolvimento
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)