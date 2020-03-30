from rest_framework import serializers
from .models import Customer

# create serializer
class CustomerSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Customer
        fields = ('id', 'name', 'age', 'active')