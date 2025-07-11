from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#Example of a View
def home(request):
    return HttpResponse("Welcome to the homepage.")


def about(request):
    return HttpResponse('This is About response')

#Example: Rendering Templates with Views
def index(request):
    return render(
        request, 'Unit2/index.html'
    )

def unit(request, pk):
    return HttpResponse(
        f"The integre send was {pk}"
    )