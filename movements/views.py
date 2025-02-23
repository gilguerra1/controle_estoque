from rest_framework import generics
from movements.models import StockMovement
from movements.serializers import StockMovementSerializer


class StockMovementListView(generics.ListCreateAPIView):

    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer


class StockMovementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
