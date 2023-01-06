from django.contrib import admin
from django.urls import path
from control.views import MunicipioListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MunicipioListView.as_view())
]
