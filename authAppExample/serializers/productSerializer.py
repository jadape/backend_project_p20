from authAppExample.models.product              import Product
from rest_framework                             import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Product
        fields = ['id', 'name', 'description', 'price', 'amount']

    def to_representation(self, obj):
        product = Product.objects.get(id = obj.id)
        return{
            'id'         : product.id,
            'name'       : product.name,
            'description': product.description,
            'price'      : product.price,
            
        }