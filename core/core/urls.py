from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    # apps
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include('django.contrib.auth.urls')),
    # login with rest-framework
    path('api-login/', include('rest_framework.urls')),
    # swagger
    path('', settings.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/output.json/', settings.schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
