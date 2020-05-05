from rest_framework import generics
from .models import Prescriptions
from .serializers import PrescriptionSerializer

class ListPrescriptionView(generics.ListAPIView):
    queryset = Prescriptions.objects.all()
    serializer_class = PrescriptionSerializer