from django.http import Http404
from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import RequestContext, loader

from notes.models import Note

def index(request):
	"""Lists all of the Notes in the Database"""
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	if not list_of_notes:
		template = 'notes/empty.html'
	else:
		template = 'notes/index.html'
	context = {'list_of_notes': list_of_notes}
	return render(request, template, context)

def create(request, note_id):
	"""Creates a new note in the Database"""
	pass

def read(request, note_id):
	"""Reads a specific note from the Database"""
	pass

def update(request, note_id):
	"""Updates a specific note in the Database"""
	pass

def delete(request, note_id):
	"""Deletes a specific note from the Database"""
	pass
