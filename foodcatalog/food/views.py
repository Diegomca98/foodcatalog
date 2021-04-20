from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def food(request):
    item_list = Item.objects.all()
    return render(request, "items.html",{
        'item_list': item_list,
    })

class FoodClassView(ListView):
    model = Item
    template_name = 'items.html'
    context_object_name = 'item_list'

def details(request, item_id):
    detail = Item.objects.get(pk=item_id)
    return render(request, "item.html", {
        'item': detail,
    })

class DetailsClassView(DetailView):
    model = Item
    #context = 'item'
    template_name = 'item.html'

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food')
    
    return render(request, 'item-form.html', {
        'form': form
    })

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

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