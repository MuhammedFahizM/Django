from django.http import HttpResponse
from django.shortcuts import redirect, render

from ORMapp.models import Product

# Create your views here.


def product_view(request):
    products = Product.objects.all()
    return render(request,"home.html",{"products" : products})

def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        if name and amount :
            Product.objects.create(name = name,amount = amount)
            return redirect("product_view")
    return render(request,"add_product.html")





def expensive_products(request):
    expensive_products =Product.objects.filter(amount__gt=100)
    
    return render(request,"expensive_products.html",{"products": expensive_products})





def ordered_products(request):
    ascending_products = Product.objects.order_by('-amount')
    descending_products = Product.objects.order_by('amount')

    return render(request,"ordered_products.html" , {
        "ascending_products" : ascending_products,
        "descending_products" : descending_products,
    })


# ==========================creating new record=======================================================================

def create_product_view(request):
    new_product = Product(name = "Laptop" , amount = 1200)
    new_product.save()

    return HttpResponse(f"Product created: {new_product.name} - {new_product.amount}")


# =============================Updating Existing Records======================================================


def update_product_view(request):
    try :
        product = Product.objects.get(id = 1)
        product.amount = 999
        product.save()

        return HttpResponse(f"Product updated : {product.name} - {product.amount}")
    
    except Product.DoesNotExist:
        return HttpResponse("Product not found")


def delete_product_view(request):

    try:
        product = Product.objects.get(id = 1)
        product.delete()

        return HttpResponse("Product deleted successfully")
    
    except Product.DoesNotExist:
        return HttpResponse ("Product not found")


# ==================================BULK OPERATIONS===========================================================


def delete_cheap_products(request):
    deleted_count = Product.objects.filter(amount__lt = 999).delete()
    return HttpResponse (f"{deleted_count} product(s) deleted successfully")











