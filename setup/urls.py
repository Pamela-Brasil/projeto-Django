"""
URL configuration for setup project.

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
from clientes.views import saudacao
from clientes.views import home
from clientes.views import Home, Clientes_list

urlpatterns = [
    path('admin/', admin.site.urls),
    #criar o caminho da url
    path('ola/', saudacao),
    path('area/', home),

    path('', Home.as_view()),
    path('clientes_tabela/', Clientes_list.as_view())         #sempre que usar classe tem que usar .as_view
    

]
