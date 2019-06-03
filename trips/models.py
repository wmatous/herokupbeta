from django.db.models import ( Model, CharField, PositiveSmallIntegerField, FloatField, DecimalField, ForeignKey, DurationField, 
URLField, UUIDField, ManyToManyField, TextField, CASCADE, DateTimeField)
import uuid


# Create your models here.

class Forecast(Model):
    forecast_url = URLField(max_length=200)
    one_day = PositiveSmallIntegerField(null = True)  
    three_day = PositiveSmallIntegerField(null = True)  
    six_day = PositiveSmallIntegerField(null = True)  
    one_day_r = PositiveSmallIntegerField(null = True)  
    three_day_r = PositiveSmallIntegerField(null = True)  
    six_day_r = PositiveSmallIntegerField(null = True)  

class Marker(Model):
    TRIP = ForeignKey('Trip', on_delete=CASCADE)
    LAT = FloatField()
    LONG = FloatField()
    ALT = FloatField()
    TS = DateTimeField()
    CLS = CharField(max_length=20)
    EL = CharField(max_length=20)

    def __str__(self):
        return 'Marker: ' + str(self.LAT) + ' ' + str(self.LONG) 

class Layer(Model):
    COLOUR = CharField(max_length=6)
    TRIP = ForeignKey('Trip', on_delete=CASCADE)

class LayerPoint(Model):
    LAYER = ForeignKey('Layer', on_delete=CASCADE)
    LAT = FloatField()
    LONG = FloatField()
    ALT = FloatField()
    TS = DateTimeField()

    def __str__(self):
        return 'LayerPoint: ' + str(self.LAT) + ' ' + str(self.LONG) 

    class Meta:
        # if you have an inline configured in the admin, this will 
        # make the roles order properly 
        ordering = ['TS'] 

class Trip(Model):
    TITLE = CharField(max_length=255)
    DESCRIPTION = TextField(blank=True)
    #attributes = ManyToManyField('Attribute', blank=True)
   #  distance = DecimalField(max_digits=9, decimal_places=2, null = True)
    # duration = DurationField(null = True)
   # latitude = DecimalField(max_digits=9, decimal_places=6,  null = True)
    # longitude = DecimalField(max_digits=9, decimal_places=6, null = True)
    # forecast_url = URLField(max_length=200,  null = True)
    # forecasts = ManyToManyField('Forecast', blank=True)
    MARKERS = ManyToManyField('Marker', blank=True)
    LAYERS = ManyToManyField('Layer', blank=True)

    def __str__(self):
        return 'Trip: ' + self.TITLE

class Attribute(Model):
    name = CharField(max_length=255)
    badge = CharField(max_length=255)

 
