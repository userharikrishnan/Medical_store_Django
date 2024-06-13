from django.shortcuts import render, redirect
from .forms import ProductForm, ProductSearchForm
from .models import Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404



def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})

def product_read(request):
    product_list=Product.objects.all()
    return render(request,'retrieve.html',{'product_list':product_list})

def product_update(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'}, status=204)
    return JsonResponse({'message': 'Method not allowed'}, status=405)



def product_search(request):
    form = ProductSearchForm(request.GET)
    product = []
    
    if form.is_valid():
        query = form.cleaned_data['query']
        product = Product.objects.filter(name__icontains=query)
    
    return render(request, 'search.html', {'form': form, 'products':product})


