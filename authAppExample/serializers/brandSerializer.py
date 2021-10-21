from authAppExample.models.brand   import Brand
from rest_framework                import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Brand
        fields = ['id', 'name']

    def to_representation(self, obj):
        brand = Brand.objects.get(id = obj.id)
        return {
            'id'   : brand.id,
            'name' : brand.name
        }