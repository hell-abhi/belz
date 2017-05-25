from rest_framework import serializers
from .models import User

from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.Serializer):
    user_id = serializers.UUIDField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    college = serializers.CharField()


    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.college = validated_data.get('college', instance.college)

        instance.save()
        return instance

    def delete(self, instance, pk):
        user = self.get_object(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
