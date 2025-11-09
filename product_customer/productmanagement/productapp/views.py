import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage

from productapp.models import Customer, Products

# Create your views here.

def addproduct(request):
    return render(request,"add.html")

# def editproduct(request):
#     return render(request,"edit.html")

# def viewproduct(request):
#     return render(request,"view.html")

def editproduct(request,id):
    data = Products.objects.get(id = id)
    return render(request,'edit.html',{"data":data,"id":id})





def addproduct_post(request):
    name = request.POST ['productname']
    price =request.POST ['price']
    qauntity = request.POST ['quantity']
    description  = request.POST ['description']
    date = request.POST ['date']


    image = request.FILES ['image']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\HP\Desktop\oct15task\productmanagement\productapp\static\image\\"+dt+'.jpg',image)
    path = '/static/image/'+dt+'.jpg'

    obj = Products()
    obj.productname = name
    obj.price = price
    obj.quantity = qauntity
    obj.description = description
    obj.date = date
    obj.image = path
    obj.save()
    return HttpResponse("Product Added")

def edit_product_post(request,id):
    try:
        name = request.POST ['productname']
        price =request.POST ['price']
        quantity = request.POST ['quantity']
        description  = request.POST ['description']
        date = request.POST ['date']

        image = request.FILES ['image']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\HP\Desktop\oct15task\productmanagement\productapp\static\image\\"+dt+'.jpg',image)
        path = '/static/image/'+dt+'.jpg'

        Products.objects.filter(id=id).update(productname = name,price = price,description=description,quantity = quantity,image = path)
        return redirect('/view_product')

    except Exception as e:
        name = request.POST['productname']
        price =request.POST ['price']
        quantity = request.POST ['quantity']
        description  = request.POST ['description']
        Products.objects.filter(id=id).update(productname = name,price = price,description=description,quantity = quantity,image = path)
        return redirect('/view_product')


def view_product(request):
    data = Products.objects.all()
    print("dataaaaaaaaaa",data)
    return render(request,"view.html",{"res":data})    


def deleteproduct(request,id):
    Products.objects.get(id=id).delete()
    return redirect('/view_product')



            # CRUD  Customer Table section :-


def addcustomer(request):
    return render(request,"add_customer.html")


def addcustomer_post(request):
    name = request.POST['customer_name']
    email = request.POST ['email']
    contact = request.POST ['contact_no']

    obj2 = Customer()
    obj2.cus_name = name
    obj2.email = email
    obj2.contact = contact
    obj2.save()
    return HttpResponse("CustomerAdded!")


def view_customer(request):
    customer_data = Customer.objects.all()
    return render(request,"view_customer.html",{"cust_tab":customer_data})


def edit_customer(request,id):
    customer_data = Customer.objects.get(id=id)
    return render(request,"edit_customer.html",{"cust_tab":customer_data,"id":id})
    


def edit_customer_post(request,id):
    
    name = request.POST['customer_name']
    email = request.POST ['email']
    contact = request.POST ['contact_no']

    Customer.objects.filter(id = id).update(cus_name = name,email=email,contact = contact)
    return redirect("/view_customer")
    
    

def delete_customer(request,id):
    Customer.objects.get(id=id).delete()
    return redirect('/view_customer')



def static_example(request):
    return render(request,'home.html')




