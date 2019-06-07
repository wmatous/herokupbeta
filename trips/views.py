from django.shortcuts import render
from trips.models import Trip, Marker, Layer, LayerPoint
from rest_framework import routers, serializers, viewsets, response
from drf_writable_nested import WritableNestedModelSerializer

class MarkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marker
        fields = ('ID', 'LAT', 'LONG', 'ALT', 'TS', 'CLS', 'EL')

class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

class LayerPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LayerPoint
        fields = ('LAT', 'LONG', 'ALT', 'TS')

class LayerPointViewSet(viewsets.ModelViewSet):
    queryset = LayerPoint.objects.all()
    serializer_class = LayerPointSerializer

class LayerSerializer(WritableNestedModelSerializer):
    POINTS = LayerPointSerializer(many=True)
    class Meta:
        model = Layer
        fields = ('ID', 'COLOUR', 'POINTS')

   #""" def create(self, validated_data):
   #     print(validated_data)
   #     validated_data.pop('ID')
   #     return Layer.objects.create(**validated_data) """

class LayerViewSet(viewsets.ModelViewSet):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer

class TripSerializer(WritableNestedModelSerializer):
    MARKERS = MarkerSerializer(many=True)
    LAYERS = LayerSerializer(many=True)
    class Meta:
        model = Trip
        fields = ('ID', 'TITLE', 'DESCRIPTION',  'LAYERS', 'MARKERS')

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {obj['ID']: obj for obj in serializer.data}
        return response.Response(data) 