"""from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world!")"""
    
"""from django.http import HttpResponse
from django.template import loader
from .models import Members


def index(request):
  mymembers = Members.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["firstname"]
  return HttpResponse(output)
"""    
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from .models import Material

def violenciaDeGenero(request):
  return HttpResponse(render(request, 'violenciadegenero.html'))

def inicio(request):
    return render(request,'inicio.html')
  
def indexM(request):
  mymembers = Material.objects.all().values()
  template = loader.get_template('indexM.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def addM(request):
  template = loader.get_template('addMATERIALES.html')
  return HttpResponse(template.render({}, request))


# ...existing code...

def addrecordM(request):
    if request.method == "POST":
        descripcion= request.POST['descripcion']
        proceso= request.POST['proceso']
      
        member=Material(
            descripcion=descripcion,
            proceso=proceso,
        )
        member.save()
        return redirect('/reciclados/indexM')


# ...existing code...
def delete(request, idMaterial):
    try:
        member = Material.objects.get(idMaterial=idMaterial)
        member.delete()
    except Material.DoesNotExist:
        raise Http404("Material no encontrado")
    return HttpResponseRedirect(reverse('reciclados:indexM'))



def updateM(request, idMaterial):
  mymember = Material.objects.get(idMaterial=idMaterial)
  template = loader.get_template('updateMATERIALES.html')
  context = {  'mymember': mymember,  }
  return HttpResponse(template.render(context, request))

# ...existing code...
def updaterecordM(request, idMaterial):
    if request.method == "POST":
        descripcion = request.POST['descripcion']
        proceso = request.POST['proceso']
        member = Material.objects.get(idMaterial=idMaterial)
        member.descripcion = descripcion
        member.proceso = proceso
        member.save()
        return redirect('/reciclados/indexM')








































































































