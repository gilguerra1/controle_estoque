from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('products.urls')),
    path('api/v1/', include('suppliers.urls')),
    path('api/v1/', include('categories.urls')),
    path('api/v1/', include('movements.urls'))
]
