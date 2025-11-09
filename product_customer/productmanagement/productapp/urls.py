from django.urls import path

from productapp import views


urlpatterns = [
    path("add",views.addproduct),
    path("editproduct/<id>",views.editproduct),
    path("view_product",views.view_product),
    path("addproduct_post",views.addproduct_post),
    path("edit_product_post/<id>",views.edit_product_post),
    path("deleteproduct/<id>",views.deleteproduct),

    
    path("addcustomer",views.addcustomer), 
    path("addcustomer_post",views.addcustomer_post) , 
    path("view_customer",views.view_customer),
    path("edit_customer/<id>",views.edit_customer),
    path("edit_customer_post/<id>",views.edit_customer_post),
    path("delete_customer/<id>",views.delete_customer),

    path("home",views.static_example)

]



