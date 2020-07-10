from rest_framework import serializers
from django.core import exceptions
from main_app import models
import dateutil.parser
from main_app.serializers import DynamicFieldsModelSerializer

class EventSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = models.Event
        fields = '__all__'
            
    def validate_datetime_end(self, value):
        try:
            dt = dateutil.parser.parse(value)
            return dt
        except:
            raise serializers.ValidationError('Datetime provided is broken or incorrect')
        
