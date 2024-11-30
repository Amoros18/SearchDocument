from django.shortcuts import render
from django.http import HttpResponse
from .models import Utilisateur

# Create your views here.

def listUser(Request):
    users = Utilisateur.objects.order_by('-username')[:5]
    output = ",".join([q.username for q in users])
    return HttpResponse(output)

def user(Request,id):
    return HttpResponse("Un utilisateur: %s" % id)


def addUser(Request):
    return HttpResponse("Ajouter Utilisateur")


def updateUser(Request,id):
    return HttpResponse("Modifier un utilisateur %s:"%id)


def deleteUser(Request,id):
    return HttpResponse("Suppression d'un Utilisateur: %s"%id)

