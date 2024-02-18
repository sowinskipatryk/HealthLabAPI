from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from patients.models import Patient
from orders.models import Order
from results.models import Result
from patients.serializers import PatientSerializer, PatientProfileSerializer
from orders.serializers import OrderSerializer
from results.serializers import ResultSerializer


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
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ResultListView(ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultDetailView(RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultUpdateView(UpdateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultDeleteView(DestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class PatientProfileDetailView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientProfileSerializer

    @extend_schema(
        examples=[
            OpenApiExample(
                'Response',
                value={
                    "patient": {
                        "id": 0,
                        "name": "string",
                        "surname": "string",
                        "sex": "string",
                        "birthDate": "string"
                    },
                    "orders": [
                        {
                            "orderId": 0,
                            "results": [
                                {
                                    "name": "string",
                                    "value": "string",
                                    "reference": "string"
                                }
                            ]
                        }
                    ]
                }
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)
