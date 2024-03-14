from rest_framework import serializers
from accounts.models import Profile


class ProfileApiSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "email", "image", "description"]
