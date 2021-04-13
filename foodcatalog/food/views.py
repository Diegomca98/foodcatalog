from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

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

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food')
    
    return render(request, 'item-form.html', {
        'form': form
    })

def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food')

    return render(request, 'item-form.html', {
        'form': form,
        'item': item,
    })

def delete_item(request, id):
    item = Item.objects.get(pk=id)

    if request.POST:
        item.delete()
        return redirect('food')

    return render(request, 'delete-item.html', {
        'item': item
    })


def index(request):
    return redirect('/food/')