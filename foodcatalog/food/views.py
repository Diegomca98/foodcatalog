from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

# Create your views here.
def food(request):
    item_list = Item.objects.all()
    return render(request, "items.html",{
        'item_list': item_list,
    })

def details(request, item_id):
    detail = Item.objects.get(pk=item_id)
    return render(request, "item.html", {
        'item': detail,
    })




def index(request):
    return redirect('/food/')