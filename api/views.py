from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from patients.models import Patient
from orders.models import Order
from results.models import Result
from patients.serializers import PatientSerializer
from orders.serializers import ShortOrderSerializer, LongOrderSerializer
from results.serializers import ShortResultSerializer, LongResultSerializer


@api_view(['GET'])
def get_patient_page(request, id):
    try:
        patient = Patient.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response({'error': 'Patient with given ID does not exist!'}, status=404)

    data = {}

    patient_serializer = PatientSerializer(patient)
    data['patient'] = patient_serializer.data
    data['orders'] = []

    orders = patient.order_set.all()
    for order in orders:
        order_serializer = ShortOrderSerializer(order)
        order_data = order_serializer.data
        order_data['results'] = []

        results = order.result_set.all()
        for result in results:
            result_serializer = ShortResultSerializer(result)
            order_data['results'].append(result_serializer.data)

        data['orders'].append(order_data)

    return Response(data)


class PatientListView(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = LongOrderSerializer


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = LongOrderSerializer


class ResultListView(ListAPIView):
    queryset = Result.objects.all()
    serializer_class = LongResultSerializer


class ResultDetailView(RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = LongResultSerializer
