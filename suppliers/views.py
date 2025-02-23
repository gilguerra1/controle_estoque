from rest_framework import generics
from suppliers.serializers import SupplierSerializer
from suppliers.models import Supplier


class SupplierCreateListView(generics.ListCreateAPIView):

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierRetriveUpdateDetroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
