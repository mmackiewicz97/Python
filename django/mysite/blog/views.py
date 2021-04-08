from django.shortcuts import render
from django.http import HttpResponse
from models import BlogPost
from django.template import loader

# Create your views here.
def witaj(request):
    return HttpResponse("Witaj świecie")

def blog(response):
    posts=BlogPost.objects.all()
    t=loader.get_template("blog.html")
    c={'posts':posts}
    return HttpResponse(t.reader(c))
