from FC.models.Restaurant import Restaurant
from FC.models.ProductCategory import ProductCategory
from django.http import HttpResponse
from FC.models.Product import Product
def populateDatabase(request):
    for i in range(0, 5):
        r = Restaurant(
            name = "restaurant" + str(i),
            email = "res" + str(i) + "@yahoo.com",
            phone = str(i) + "phone",
            website = "http://restaurant" + str(i) + ".com")
        r.save()
        for j in range(0, 5):
            pc = ProductCategory(
                restaurant = r,
                name = "pCat" + str(j) + r.name,
                presentation_index = j)
            pc.save()
            for k in range(0, 5):
                p = Product(
                    name = "product" + str(k) + pc.name,
                    price = 10 + k,
                    image_url = "image" + str(k),
                    visibility = True,
                    description = "product" + str(k),
                    presentation_index = k,
                    product_category = pc)
                p.save()
    return HttpResponse("Succes")
