from django.shortcuts import render
from django.template import RequestContext

def index(request):
    return render_to_response('index.html')

