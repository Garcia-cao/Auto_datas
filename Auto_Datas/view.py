# -*- coding: utf-8 -*-
# !/usr/bin/python3
# @Author : Garcia
# @Time   : 2019/12/11
# @File   : view.py

import execjs
import datetime
import requests
from Auto_Datas import models
from common import connect_database
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.forms.models import model_to_dict


def login(request):
    err_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == '0000':
            return redirect('/index')
        else:
            err_msg = '* 用户名或密码错误'
    return render(request, 'login.html', {'err_msg': err_msg})
    # elif request.method == "GET":
    #     return render(request, "login.html")


def index(request):
    return render(request, 'index.html')


def set_database(request):
    return render(request, 'set_databases.html')


def databases_data(request):
    return render(request, 'databases_data.html')


def projects_data(request):
    return render(request, 'projects_data.html')


def set_interfaces(request):
    return render(request, 'set_interfaces.html')


def interface_data(request):
    return render(request, 'interface_data.html')


def set_flows(request):
    return render(request, 'set_flows.html')


def flows_data(request):
    return render(request, 'flows_data.html')


def flow_information(request):
    return render(request, 'flow_information.html')


def get_database(request):
    """
    获取数据库信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'GET':
        all_data = models.ProjectsDatabase.objects.all().order_by('-update_date')
        for data in all_data:
            dict_data.append(model_to_dict(data))
        # return render(request, 'set_databases.html', {'database': dict_data})
    json_data = {'totals': all_data.count(), 'database': dict_data}
    return JsonResponse(json_data)


def search_database(request):
    """
    根据条件搜索相关数据库信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        database_type = request.POST.get('type')
        database_server = request.POST.get('server')
        all_data = models.ProjectsDatabase.objects.filter(type__icontains=database_type). \
            filter(server__icontains=database_server).order_by('-update_date')
        for data in all_data:
            dict_data.append(model_to_dict(data))
    json_data = {'totals': all_data.count(), 'database': dict_data}
    return JsonResponse(json_data)


def add_database(request):
    """
    添加相关数据库信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        projects_database = models.ProjectsDatabase()
        projects_database.type = request.POST.get('type')
        projects_database.server = request.POST.get('server')
        projects_database.host = request.POST.get('host')
        projects_database.port = request.POST.get('port')
        projects_database.username = request.POST.get('username')
        projects_database.password = request.POST.get('password')
        projects_database.create_date = datetime.datetime.now().strftime('%Y-%m-%d')
        projects_database.update_date = datetime.datetime.now().strftime('%Y-%m-%d')
        projects_database.save()
        all_data = models.ProjectsDatabase.objects.all().order_by('-update_date')
        for data in all_data:
            dict_data.append(model_to_dict(data))
    json_data = {'totals': all_data.count(), 'database': dict_data}
    return JsonResponse(json_data)


def delete_database(request):
    """
    删除相关数据库信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        database_id = request.POST.get('id')
        models.ProjectsDatabase.objects.filter(id=database_id).delete()
        all_data = models.ProjectsDatabase.objects.all().order_by('-update_date')
        for data in all_data:
            dict_data.append(model_to_dict(data))
    json_data = {'totals': all_data.count(), 'database': dict_data}
    return JsonResponse(json_data)


def get_project(request):
    """
    获取项目信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'GET':
        all_data = models.Projects.objects.all().values('id', 'name', 'url', 'landfall_location', 'database_id',
                                                        'create_date', 'update_date', 'database__server',
                                                        'database__host').order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        all_data = models.Projects.objects.filter(id=project_id)
        for data in all_data:
            dict_data.append(model_to_dict(data))
    json_data = {'totals': all_data.count(), 'project': dict_data}
    return JsonResponse(json_data)


def search_project(request):
    """
    根据条件搜索相关项目信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')
        all_data = models.Projects.objects.filter(name__icontains=name).filter(url__icontains=url). \
            values('id', 'name', 'url', 'landfall_location', 'create_date', 'update_date', 'database__server', 'database__host'). \
            order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    json_data = {'totals': all_data.count(), 'project': dict_data}
    return JsonResponse(json_data)


def add_project(request):
    """
    添加相关项目信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        projects = models.Projects()

        projects.name = request.POST.get('name')
        projects.url = request.POST.get('url')
        projects.landfall_location = request.POST.get('landfall_location')
        projects.create_date = datetime.datetime.now().strftime('%Y-%m-%d')
        projects.update_date = datetime.datetime.now().strftime('%Y-%m-%d')
        database_id = models.ProjectsDatabase.objects.get(id=int(request.POST.get('database')))
        projects.database = database_id
        projects.save()
        all_data = models.Projects.objects.all().values('id', 'name', 'url', 'landfall_location', 'create_date',
                                                        'update_date', 'database__server', 'database__host')\
            .order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    json_data = {'totals': all_data.count(), 'project': dict_data}
    return JsonResponse(json_data)


def delete_project(request):
    """
    删除相关项目信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        project_id = request.POST.get('id')
        models.Projects.objects.filter(id=project_id).delete()
        all_data = models.Projects.objects.all(). \
            values('id', 'name', 'url', 'create_date', 'update_date', 'database__server', 'database__host'). \
            order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    json_data = {'totals': all_data.count(), 'project': dict_data}
    return JsonResponse(json_data)


def get_api(request):
    """
    获取接口信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'GET':
        all_data = models.ProjectApi.objects.all().values('id', 'name', 'api_rap_id', 'create_date', 'update_date',
                                                          'project__name').order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        all_data = models.ProjectApi.objects.filter(project_id=project_id)
        for data in all_data:
            dict_data.append(model_to_dict(data))
    json_data = {'totals': all_data.count(), 'api': dict_data}
    return JsonResponse(json_data)


def search_api(request):
    """
    根据条件搜索相关接口信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        name = request.POST.get('name')
        api_rap_id = int(request.POST.get('api_rap_id'))
        project = int(request.POST.get('project'))
        all_data = models.ProjectApi.objects.filter(name__icontains=name).filter(api_rap_id__icontains=api_rap_id). \
            filter(project_id=project).values('id', 'name', 'api_rap_id', 'create_date', 'update_date',
                                              'project__name'). \
            order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    json_data = {'totals': all_data.count(), 'api': dict_data}
    return JsonResponse(json_data)


def add_api(request):
    """
    添加相关接口信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        api = models.ProjectApi()
        api.name = request.POST.get('name')
        api.api_rap_id = int(request.POST.get('api_rap_id'))
        api.project = models.Projects.objects.get(id=int(request.POST.get('project')))
        api.create_date = datetime.datetime.now().strftime('%Y-%m-%d')
        api.update_date = datetime.datetime.now().strftime('%Y-%m-%d')
        api.save()
        all_data = models.ProjectApi.objects.all().values('id', 'name', 'api_rap_id', 'create_date', 'update_date',
                                                          'project__name').order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    json_data = {'totals': all_data.count(), 'api': dict_data}
    return JsonResponse(json_data)


def delete_api(request):
    """
    删除相关接口信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        api_id = request.POST.get('id')
        models.ProjectApi.objects.filter(id=api_id).delete()
        all_data = models.ProjectApi.objects.all().values('id', 'name', 'api_rap_id', 'create_date', 'update_date',
                                                          'project__name').order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    json_data = {'totals': all_data.count(), 'api': dict_data}
    return JsonResponse(json_data)


def get_flow(request):
    """
    获取流程信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'GET':
        all_data = models.ProjectFlow.objects.all().values('id', 'name', 'project', 'project__name', 'create_date',
                                                           'update_date').order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    json_data = {'totals': all_data.count(), 'flow': dict_data}
    return JsonResponse(json_data)


def search_flow(request):
    """
    根据条件搜索相关流程信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        name = request.POST.get('name')
        project = int(request.POST.get('project'))
        all_data = models.ProjectFlow.objects.filter(name__icontains=name, project_id=project). \
            values('id', 'name', 'project', 'project__name', 'create_date', 'update_date').order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    json_data = {'totals': all_data.count(), 'flow': dict_data}
    return JsonResponse(json_data)


def add_flow(request):
    """
    添加相关流程信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        flow = models.ProjectFlow()
        flow.name = request.POST.get('name')
        flow.project_id = int(request.POST.get('project'))
        flow.create_date = datetime.datetime.now().strftime('%Y-%m-%d')
        flow.update_date = datetime.datetime.now().strftime('%Y-%m-%d')
        flow.save()
        all_data = models.ProjectFlow.objects.all().values('id', 'name', 'project', 'project__name', 'create_date',
                                                           'update_date').order_by('-update_date')
        for data in all_data:
            dict_data.append(data)
    json_data = {'totals': all_data.count(), 'flow': dict_data}
    return JsonResponse(json_data)


def get_sub_flow(request):
    """
    获取相关子流程信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'GET':
        flow = int(request.GET.get('flow_id'))
        all_data = models.ProjectSubFlow.objects.filter(flow_id=flow).order_by('step')
        for data in all_data:
            dict_data.append(model_to_dict(data))
    json_data = {'totals': all_data.count(), 'sub_flow': dict_data}
    return JsonResponse(json_data)


def add_sub_flow(request):
    """
    添加相关子流程信息
    :param request:
    :return:
    """
    dict_data = []
    if request.method == 'POST':
        flow = int(request.POST.get('flow_id'))
        sub_flow = models.ProjectSubFlow()
        sub_flow.type = int(request.POST.get('type'))
        sub_flow.step = int(request.POST.get('step'))
        if sub_flow.type == 1:
            sub_flow.process = request.POST.get('api')
        else:
            sub_flow.process = request.POST.get('process')
        sub_flow.transmit_dict = request.POST.get('transmit_dict')
        sub_flow.transmit = request.POST.get('transmit')
        sub_flow.accept = request.POST.get('accept')
        sub_flow.flow_id = flow
        sub_flow.save()
        all_data = models.ProjectSubFlow.objects.filter(flow_id=flow).order_by('step')
        for data in all_data:
            dict_data.append(model_to_dict(data))
    json_data = {'totals': all_data.count(), 'sub_flow': dict_data}
    return JsonResponse(json_data)


def create_data(request):
    js_function = """
    function get_json(json_template){
        var Mock = require('mockjs')
        var data = Mock.mock(json_template)
        
        return JSON.parse(JSON.stringify(data))
    }
    """
    accept = ''
    transmit = ''
    flow_id = int(request.GET.get('flow_id'))
    dict_data = []
    all_data = models.ProjectSubFlow.objects.filter(flow_id=flow_id).\
        values('id', 'type', 'process', 'transmit_dict', 'transmit', 'accept', 'flow__project__url',
               'flow__project__database_id').order_by('step')
    database_data = models.ProjectsDatabase.objects.filter(id=all_data[0]['flow__project__database_id']).\
        values('type', 'host', 'port', 'server', 'password', 'username')
    landfall_location = models.ProjectFlow.objects.filter(id=flow_id).values('project__landfall_location')

    login_api_information = all_data[0]
    login_information = get_response(login_api_information)
    session_id = login_information[login_api_information['transmit_dict']][login_api_information['transmit']]
    print(landfall_location[0]['project__landfall_location'])
    print(session_id)

    for data in all_data[1:]:
        # data = model_to_dict(data)
        accept = data['accept']
        if data['type'] == 1:
            header = {}
            ctx = execjs.compile(js_function)
            api_data = models.ProjectApi.objects.filter(id=data['process']).values('api_rap_id')
            api_rap_id = str(api_data[0]['api_rap_id'])
            template_url = 'http://rap2-api.rccchina.com/app/mock/template/' + api_rap_id + '?scope=request'
            information_url = 'http://rap2-api.rccchina.com/interface/get?id=' + api_rap_id
            template_response = (requests.get(url=template_url)).json()
            information_response = (requests.get(url=information_url)).json()
            data_json = ctx.call('get_json', template_response)
            if landfall_location[0]['project__landfall_location'] == 'Authorization':
                header = {'Authorization': session_id}
            elif landfall_location[0]['project__landfall_location'] == 'session_id':
                data_json['session_id'] = session_id
            if accept is not None:
                data_json[accept] = transmit
            if information_response['data']['method'] == 'POST':
                response = (requests.post(url=data['flow__project__url'] + information_response['data']['url'],
                                          headers=header, json=data_json)).json()
            else:
                response = (requests.get(url=data['flow__project__url'] + information_response['data']['url'],
                                         headers=header, params=data_json)).json()
            dict_data.append(response)
        else:
            sql = data['process']
            if accept is not None:
                sql = "%s %s = %s" % (data['process'], accept, transmit)
            sql_result = connect_database.judge_database(database_data[0], sql)
            dict_data.append(sql_result)
        if data['transmit_dict'] != '' and data['transmit'] != '' and data['type'] == 1:
            transmit = response['data'][data['transmit_dict']][data['transmit']]
    return JsonResponse(dict_data, safe=False, json_dumps_params={'ensure_ascii': False})


def get_response(data, accept=None, transmit=None):
    js_function = """
    function get_json(json_template){
    var Mock = require('mockjs')
    var data = Mock.mock(json_template)

    return JSON.parse(JSON.stringify(data))
    }
    """
    header = {}
    ctx = execjs.compile(js_function)
    api_data = models.ProjectApi.objects.filter(id=data['process']).values('api_rap_id')
    api_rap_id = str(api_data[0]['api_rap_id'])
    template_url = 'http://rap2-api.rccchina.com/app/mock/template/' + api_rap_id + '?scope=request'
    information_url = 'http://rap2-api.rccchina.com/interface/get?id=' + api_rap_id
    template_response = (requests.get(url=template_url)).json()
    information_response = (requests.get(url=information_url)).json()
    data_json = ctx.call('get_json', template_response)
    if accept is not None:
        data_json[accept] = transmit
    print(data['flow__project__url'] + information_response['data']['url'])
    if information_response['data']['method'] == 'POST':
        response = (requests.post(url=data['flow__project__url'] + information_response['data']['url'],
                                  headers=header, json=data_json)).json()
    else:
        response = (requests.get(url=data['flow__project__url'] + information_response['data']['url'],
                                 headers=header, params=data_json)).json()
    return response






