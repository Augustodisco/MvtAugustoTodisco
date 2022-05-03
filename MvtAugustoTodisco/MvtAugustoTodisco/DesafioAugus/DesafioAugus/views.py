from contextvars import Context
from django.shortcuts import render
from django.template import loader,Context,Template
from django.http import HttpResponse

def htmlTemplate(self):
    nombrepadre="Hernan"
    nombremadre="Laura"
    nombretio="Nestor"
    nombretia="Romina"
    diccionario={'nombrepadre': nombrepadre, 'nombremadre': nombremadre, 'nombretia': nombretia, 'nombretio': nombretio}
    
    plantilla=loader.get_template("template.html") 
    documento=plantilla.render(diccionario)  
    return HttpResponse (documento)