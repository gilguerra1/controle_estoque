from django.urls import path
from . import views


urlpatterns = [
    path('stockmoviments/', views.StockMovementListView.as_view(), name='stock-moviment-create-list'),
    path('stockmoviments/<int:pk>', views.StockMovementRetrieveUpdateDestroyView.as_view(), name='stock-moviment-detail-view')
]
