from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext as _

from users.models import Profile
from django.contrib.auth.models import User

class ListUsers( ListView ):

    template_name = 'users/list.html'
    model = Profile
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'headers': dict(
                id                  = _('id'),
                username            = _('user'),
                first_name          = _('first name'),
                last_name           = _('last name'),
                email               = _('email'),
                user_permissions    = _('access level'),
                is_active           = _('enabled'),
                last_login          = _('last access'),
                actions             = '',
                ),
            'txt': dict(
                title       = _('users'),
                no_users    = _('there\'s no users available for this filter.' ),
                total       = _('Total Cases')
            )
        })

        return context
class ReadUser( DetailView ):
    model = Profile
    template_name = 'users/read.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update({
            'titles': dict(
                table               = _('user data'),
                id                  = _('id'),
                username            = _('user'),
                first_name          = _('first name'),
                last_name           = _('last name'),
                email               = _('email'),
                user_permissions    = _('access level'),
                is_active           = _('enabled'),
                last_login          = _('last access'),
                )
        })

        return context

class CreateUser( CreateView ):
    model = Profile
    template_name = 'users/create_update.html'
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'user_permissions',
        'is_active',
        'last_login',
    ]

class UpdateUser( UpdateView ):
    model = Profile
    template_name = 'users/create_update.html'
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'user_permissions',
        'is_active',
        'last_login',
    ]


class DeleteUser( DeleteView ):
    model = Profile
    template_name = 'users/delete.html'

    success_url = reverse_lazy('users:list')

