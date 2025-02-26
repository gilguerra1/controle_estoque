from django.urls import path
from . import views


urlpatterns = [
    path('suppliers/', views.SupplierCreateListView.as_view(), name='supplier-create-list'),
    path('suppliers/<int:pk>', views.SupplierRetriveUpdateDetroyView.as_view(), name='supplier-datail-view')
]
