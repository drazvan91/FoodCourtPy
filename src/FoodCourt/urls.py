from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import FC
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FoodCourt.views.home', name='home'),
    # url(r'^FoodCourt/', include('FoodCourt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^account/', include('FC.urls')),
    url(r'^order/', 'FC.controllers.order.order'),
    
    url(r'^m/order/$',
        'FC.controllers.order.m_order_create_step1'),
    url(r'^m/order/(?P<restaurantId>\d+)/$',
        'FC.controllers.order.m_order_create_step2'),
    url(r'^m/order/(?P<restaurantId>\d+)/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$',
        "FC.controllers.order.m_order_create_step3"),
    
    url(r'^admin/', include(admin.site.urls)),
)
