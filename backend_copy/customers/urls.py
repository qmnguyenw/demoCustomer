from django.conf.urls import url 
from django.urls import path, include
from rest_framework import routers
from .views import * 

router = routers.DefaultRouter()
router.register(r'', CustomerViewSet)

# create url 
urlpatterns = [ 
    path('customer/', include(router.urls)),
    # url(r'^customers/$', CustomerViewSet),
    # url(r'^customers/age/(?P<age>[0-9]+)/$', views.customer_list_age), # <age> identify [0-9]+ stand for age
]