from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def index_view(request):
	saludo = 'Hola Mundo'
	ctx = {'saludo': saludo}
	return render_to_response('index.html',ctx,context_instance = RequestContext(request))

