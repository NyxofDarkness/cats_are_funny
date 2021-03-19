from rest_framework import generics
from .serializer import CatSerializer
from .models import Cats

class CatList(generics.ListCreateAPIView):
    queryset = Cats.objects.all()
    serializer_class = CatSerializer

class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cats.objects.all()
    serializer_class = CatSerializer
