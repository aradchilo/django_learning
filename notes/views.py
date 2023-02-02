from django.shortcuts import render

from .models import Notes

from django.http import Http404

from django.views.generic import ListView


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exists")
    return render(request, 'notes/notes_detail.html', {'note': note})
