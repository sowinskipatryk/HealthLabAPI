from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from patients.models import Patient
from orders.models import Order
from results.models import Result
from patients.serializers import PatientSerializer, PatientProfileSerializer
from orders.serializers import ShortOrderSerializer
from results.serializers import LongResultSerializer


class PatientListView(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientUpdateView(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDeleteView(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = ShortOrderSerializer


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = ShortOrderSerializer


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = ShortOrderSerializer


class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = ShortOrderSerializer


class ResultListView(ListAPIView):
    queryset = Result.objects.all()
    serializer_class = LongResultSerializer


class ResultDetailView(RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = LongResultSerializer


class ResultUpdateView(UpdateAPIView):
    queryset = Result.objects.all()
    serializer_class = LongResultSerializer


class ResultDeleteView(DestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = LongResultSerializer


class PatientProfileDetailView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientProfileSerializer
