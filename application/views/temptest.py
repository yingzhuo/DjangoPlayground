from django.http import HttpResponse
from django_sugar.valueobject import IntRangeCollectionField
from django_sugar.web import http
from rest_framework import views, serializers


class ClientDataSerializer(serializers.Serializer):
    price_zone = IntRangeCollectionField(
        error_messages={
            'required': '价格带缺失',
        },
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class TempTestView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        client_data = http.get_client_sent_data(request, default_values={}, kwargs=kwargs)

        ser = ClientDataSerializer(data=client_data)
        ser.is_valid(raise_exception=True)

        price_zone = ser.validated_data['price_zone']
        print(price_zone)

        return HttpResponse('Temp Test')
