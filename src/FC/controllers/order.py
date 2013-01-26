from FC.models import Restaurant
from django.shortcuts import render_to_response
from FC.models.ProductCategory import ProductCategory
from datetime import date, timedelta
from FC.viewmodels.CreateOrderViewModels import CreateOrderViewModel, \
    CreateOrderCategoryViewModel, CreateOrderProductViewModel
from FC.models.Product import Product

def order(request):
    restaurants = Restaurant.objects.all()
    return render_to_response("order/order.html", {"restaurants":restaurants})

def m_order_create_step1(request):
    restaurants = Restaurant.objects.all()
    return render_to_response("m_order/orderStep1.html", {"restaurants":restaurants})

def m_order_create_step2(request, restaurantId):
    restaurant = Restaurant.objects.get(id = restaurantId);
    days = []
    tday = date.today()
    for i in range(1, 8):
        days.append(tday + timedelta(days = i))
    return render_to_response("m_order/orderStep2.html",
                              {"days":days,
                               "restaurant":restaurant})

def m_order_create_step3(request, restaurantId, year, month, day):
    restaurant = Restaurant.objects.get(id = restaurantId);
    categories = ProductCategory.objects.filter(restaurant = restaurant)
    model = CreateOrderViewModel()
    for categorie in categories:
        cat_view_model = CreateOrderCategoryViewModel()
        cat_view_model.category = categorie

        products = Product.objects.filter(product_category = categorie)
        for produs in products:

            pro_view_model = CreateOrderProductViewModel()
            pro_view_model.product = produs

            cat_view_model.list_product = cat_view_model.list_product + [pro_view_model]

        model.list_category = model.list_category + [cat_view_model]
    return render_to_response("m_order/orderStep3.html",
                              {"orderpanel":model,
                               "restaurant":restaurant})
