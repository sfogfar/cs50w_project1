from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def hello(request):
    return HttpResponse("Hello world!")

def title(request, title):
    entry = util.get_entry(title)
    
    return render(request, "encyclopedia/title.html", {
        "title": title, "entry": entry
    })