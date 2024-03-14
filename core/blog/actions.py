def make_activation(model_admin, request, queryset):
    result = queryset.update(status=True)
    model_admin.message_user(request, f"{result} Posts ware accepted")


make_activation.short_description = "تایید پست"


def make_deactivation(model_admin, request, queryset):
    result = queryset.update(status=False)
    model_admin.message_user(request, f"{result} Posts ware rejected")


make_deactivation.short_description = "رد پست"
