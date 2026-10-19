from django.shortcuts import render,redirect
import markdown2
from . import util
from django.http import HttpResponseNotFound, HttpResponse
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    if title not in util.list_entries():
        return HttpResponseNotFound("Page not found")

    content = util.get_entry(title)
    result = markdown2.markdown(content)

    return render(request, "encyclopedia/title.html",{
        "title": result,
        "upper": title
    })

def search(request):

    data = util.list_entries()
    if request.method == "GET":
        title = str(request.GET.get("q"))
    for i in data:
        if title.lower() in i.lower():
            return redirect(f"/wiki/{i}/")
    return HttpResponseNotFound("Page not found")


def page(request):

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title in util.list_entries():
            return HttpResponse("This title already exists")
        util.save_entry(title,content)
        return redirect(f"/wiki/{title}/")


    return render(request, "encyclopedia/newpg.html")

def edit(request,title):

    if request.method == "POST":
        content = request.POST.get("edit")
        util.save_entry(title,content)
        return redirect(f"/wiki/{title}/")



    return render(request, "encyclopedia/edit.html", {
        "content": util.get_entry(title),
        "title" : title
    })

def randoms(request):
    titles = util.list_entries()
    title = random.choice(titles)
    return redirect(f"/wiki/{title}/")
