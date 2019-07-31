from django.shortcuts import render
from .models import Product,Customer
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

# Create your views here.
class productlistview(ListView):
    model=Product
    template_name = 'online/product_list.html'
class productdetailsview(DetailView):
    context_object_name = 'school_details'
    model = Product
    template_name = 'online/product_detail.html'
    template_name='online/product_list.html'


