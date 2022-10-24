from rest_framework import serializers

from .models import (
    Bank, 
    Location,
    Waybill,
    Category,
    Product,
)


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
        
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'     
        
        
class WaybillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Waybill
        fields = '__all__'     
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'     


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'    


class WaybillDateSerializer(serializers.Serializer):
    date = serializers.DateTimeField(required=True)

