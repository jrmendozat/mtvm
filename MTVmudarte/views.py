from django.http import *
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader

def home(request):
     return HttpResponse("welcome to my world")


def error404(request):
     template = loader.get_template('404.html')
     context = Context({'message': 'All: %s' % request,})
     return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)

def custom_404e(request):
                    return render_to_response('404.html')


def handler404e(request):
    return details(request, '404-page-url')

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def page_not_found(request, template_name='404.html'):
    return render_to_response('404.html')

def error(request):
    return render(request,'404.html')

def error4(request):
    return HttpResponseNotFound(render_to_string('404.html'))

def custom_404(request, template_name = '404.html'):

     return HttpResponse('<h2 style="text-align: center;"><br /><br />Esto es un error 404: pagina no encontrada.</h2>')
