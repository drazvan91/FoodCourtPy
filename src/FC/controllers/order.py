from FC.models import Restaurant
from django.shortcuts import render_to_response

def order(request):
    restaurants = Restaurant.objects.all()
    return render_to_response("order/order.html", {"restaurants":restaurants})
