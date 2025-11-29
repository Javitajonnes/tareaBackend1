from rest_framework import serializers
from .models import Ticket
class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields=['task','completed','user']