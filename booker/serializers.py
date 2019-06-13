from rest_framework import serializers
from booker.models import Booker, BookRequest

class BookerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booker 
		fields = '__all__'


class BookRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookRequest
		fields = '__all__'

