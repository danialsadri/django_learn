from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from ..serializers import ProfileApiSerializer
from accounts.models import Profile


class ProfileApiView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileApiSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
