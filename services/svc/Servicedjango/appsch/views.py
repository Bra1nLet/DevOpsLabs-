from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .models import Item
from .someform import ItemForm



class AllItems(ListView):
    template_name = 'appsch/home.html'
    model = Item

    def get(self, response):
        a = self.model.objects.all()
        ctx = {'items': a}

        print(a)

        if a.count() > 0:
            return render(response, template_name=self.template_name, context=ctx)
        return render(response, template_name=self.template_name, context=ctx)


class AddItem(ListView):
    template_name = 'appsch/createItem.html'
    model = Item

    def get(self, response):
        a = self.model.objects.all()
        form = ItemForm()
        ctx = {'item': a, 'form': form}

        if a.count() > 0:
            return render(response, template_name=self.template_name, context=ctx)
        return render(response, template_name=self.template_name, context=ctx)

    def post(self, response):
        data = ItemForm(response.POST, response.FILES)
        n = self.model(name=data.data['item'], price=data.data['price'], about_item=data.data['detail'], picture=data.files['picture'])
        n.save()
        return redirect('appsch:all_items')


class ShowItem(ListView):
    template_name = 'appsch/home.html'
    model = Item

    def get(self, response, itemid):
        a = self.model.objects.all().filter(id=itemid)
        ctx = {'item': a[0]}
        if a.count() > 0:
            return render(response, template_name=self.template_name, context=ctx)
        raise Http404

