import django_filters.rest_framework
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework import filters, status, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('age',)
    search_fields = ('age',)

    def delete(self, request):
        Customer.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
