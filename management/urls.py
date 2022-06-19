from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from app01.views import depart, pretty, user, admin

urlpatterns = [
    path('', depart.depart_list),
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),

    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/model/form/add/', user.user_model_form_add),
    path('user/<int:nid>/delete/', user.user_delete),
    path('user/<int:nid>/edit/', user.user_edit),

    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),

    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),

]
