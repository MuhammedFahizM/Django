from django.urls import path

from ORMapp import views

urlpatterns = [

    path("product_view/",views.product_view,name = "product_view"),
    path("add_product/",views.add_product,name = "add_product"),
    path("create_product_view/",views.create_product_view,name="create_product_view"),

    path("expensive_products/",views.expensive_products,name="expensive_products"),
    path("ordered_products/",views.ordered_products,name="ordered_products"),

    
    path("update_product_view/",views.update_product_view,name="update_product_view"),
    path("delete_product_view/",views.delete_product_view,name="delete_product_view"),
    path("delete_cheap_products/",views.delete_cheap_products,name="delete_cheap_products")
    
]