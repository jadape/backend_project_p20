from authAppExample.models.user import User
from rest_framework             import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'name', 'last_name', 'username', 'password', 'email', 'telephone', 'address'] 

def to_representation(self, obj):
    user = User.objects.get(id = obj.id)
    return {
        'name'     : user.name,
        'last_name': user.last_name
    }

