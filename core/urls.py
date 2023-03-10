from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from control.urls import router
from django.views.static import serve

urlpatterns = [
    path('acceso/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'pusinex'))),
    path('', include('control.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
