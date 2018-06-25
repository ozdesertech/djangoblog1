from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {'mydata' : "HELLO WORLD"}
    return render(request, 'blog/index.html', data)
