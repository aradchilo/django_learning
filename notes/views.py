from urllib import request

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NotesForm
from .models import Notes

from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/ssmart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/admin"


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
    login_url = "/admin"
