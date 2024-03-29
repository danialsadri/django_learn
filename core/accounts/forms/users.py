from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"
