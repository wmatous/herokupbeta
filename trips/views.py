from django.shortcuts import render
from trips.models import Trip, Marker, Layer, LayerPoint
from rest_framework import routers, serializers, viewsets

class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = ('TITLE', 'DESCRIPTION', 'MARKERS', 'LAYERS')

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class MarkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marker
        fields = ('TRIP', 'LAT', 'LONG', 'ALT', 'TS', 'CLS', 'EL')

class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

class LayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Layer
        fields = ('COLOUR', 'TRIP')

class LayerViewSet(viewsets.ModelViewSet):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer

class LayerPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LayerPoint
        fields = ('LAYER', 'LAT', 'LONG', 'ALT', 'TS')

class LayerPointViewSet(viewsets.ModelViewSet):
    queryset = LayerPoint.objects.all()
    serializer_class = LayerPointSerializer