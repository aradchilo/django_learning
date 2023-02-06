from urllib import request

from django.shortcuts import render

from .forms import NotesForm
from .models import Notes

from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/ssmart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
