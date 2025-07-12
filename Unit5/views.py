from django.http import HttpResponseForbidden
from django.shortcuts import render

# Create your views here.

def check_persmission(request):
    if request.user.has_perm('appname.can_publish'):
        print("Has Permission")
    else:
        return HttpResponseForbidden()