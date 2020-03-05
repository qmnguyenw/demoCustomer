from django.conf.urls import url 
from backend.customers import views 

# create url 
urlpatterns = [ 
    url(r'^customers/$', views.customer_list),
    url(r'^customers/(?P<pk>[0-9]+)$', views.customer_detail), # <pk> identify [0-9]+ stand for pk
    url(r'^customers/age/(?P<age>[0-9]+)/$', views.customer_list_age), # <age> identify [0-9]+ stand for age
]