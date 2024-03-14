from django.contrib import admin
from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "first_name", "last_name"]
    list_filter = ["created_date", "updated_date"]
    search_fields = ["first_name", "last_name"]
    raw_id_fields = ["user"]
