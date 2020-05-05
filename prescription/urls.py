from django.urls import path
from .views import ListPrescriptionView


urlpatterns = [
    path('', ListPrescriptionView.as_view(), name="prescription-data")
]