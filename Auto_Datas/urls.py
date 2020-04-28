"""Auto_Datas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from Auto_Datas import view

urlpatterns = [
    url(r'^$', view.login),
    url(r'^index', view.index),
    url(r'^set_databases', view.set_database),
    url(r'^databases_data', view.databases_data),
    url(r'^projects_data', view.projects_data),
    url(r'^set_interfaces', view.set_interfaces),
    url(r'^interface_data', view.interface_data),
    url(r'^set_flows', view.set_flows),
    url(r'^flows_data', view.flows_data),
    url(r'^flow_information', view.flow_information),

    url(r'^get_database', view.get_database),
    url(r'^search_database', view.search_database),
    url(r'^add_database', view.add_database),
    url(r'^delete_database', view.delete_database),

    url(r'^get_project', view.get_project),
    url(r'^search_project', view.search_project),
    url(r'^add_project', view.add_project),
    url(r'^delete_project', view.delete_project),

    url(r'^get_api', view.get_api),
    url(r'^search_api', view.search_api),
    url(r'^add_api', view.add_api),
    url(r'^delete_api', view.delete_api),

    url(r'^get_flow', view.get_flow),
    url(r'^search_flow', view.search_flow),
    url(r'^add_flow', view.add_flow),

    url(r'^get_sub_flow', view.get_sub_flow),
    url(r'^add_sub_flow', view.add_sub_flow),

    url(r'create_data', view.create_data)
]
