from django.contrib import admin
from trips.models import Trip, Marker, Layer, LayerPoint

class TripAdmin(admin.ModelAdmin):
    pass
admin.site.register(Trip, TripAdmin)

class MarkerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Marker, MarkerAdmin)

class LayerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Layer, LayerAdmin)

class LayerPointAdmin(admin.ModelAdmin):
    pass
admin.site.register(LayerPoint, LayerPointAdmin)

# Register your models here.
