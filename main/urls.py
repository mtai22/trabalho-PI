"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from caderno.views import descricao_editar, descricao_remover, descricao_criar, descricao_listar, index, detalhe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('descricao/',descricao_criar,name='descricao_criar'),
    path('descricao/editar/<int:id>/',descricao_editar,name='descricao_editar'),
    path('descricao/remover/<int:id>/',descricao_remover,name='descricao_remover'),
    path('descricao/listar/',descricao_listar,name='descricao_listar'),
    path('detalhe/<int:id>', detalhe, name= 'detalhe'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
