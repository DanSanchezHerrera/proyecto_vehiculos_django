from django.contrib import admin
from django.urls import path, include
from vehiculo import views as vehiculo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vehiculo_views.index, name='index'),
    path('vehiculo/', include('vehiculo.urls')),
]
