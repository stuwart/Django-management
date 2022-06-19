from django.shortcuts import render, HttpResponse, redirect
from app01.utils.form import *
from app01.utils.pagination import *
from app01 import models


def admin_list(request):
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['username__contains'] = search_data

    queryset = models.Admin.objects.filter(**data_dict)

    # 分页 常规组件
    page_object = Pagination(request, queryset)
    queryset = page_object.page_queryset
    page_string = page_object.html
    # context = {
    #     'queryset': page_object.page_queryset,
    #     'page_string': page_object.html,
    # }

    return render(request, 'admin_list.html', locals())


def admin_add(request):
    title = '添加管理员'
    if request.method == "GET":
        form = AdminModelForm
        return render(request, 'add.html', locals())

    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request,'add.html',locals())