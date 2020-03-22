from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext as _

from cases.models import Case

class ListCases( ListView ):

    template_name = 'cases/list.html'
    model = Case
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'headers': dict(
                id          = _('id'),
                type_of     = _('type'),
                title       = _('title'),
                state       = _('state'),
                priority    = _('priority'),
                difficulty  = _('difficulty'),
                assignee    = _('assignee'),
                ),
            'txt': dict(
                no_cases    = _('there\'s no cases available for this filter.' ),
                total       = _('Total Cases')
            )
        })

        return context
class ReadCase ( DetailView ):
    model = Case
    template_name = 'cases/read.html'

class CreateCase( CreateView ):
    model = Case
    template_name = 'cases/create_update.html'
    fields = [
        'title',
        'description',
        'assignee',
        'type_of',
        'state',
        'difficulty',
        'priority',
    ]

class UpdateCase( UpdateView ):
    model = Case
    template_name = 'cases/create_update.html'
    fields = [
        'title',
        'description',
        'assignee',
        'type_of',
        'state',
        'difficulty',
        'priority',
    ]

class DeleteCase( DeleteView ):
    model = Case
    template_name = 'cases/delete.html'
    success_url = reverse_lazy('cases:index')

