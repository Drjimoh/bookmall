from django.forms import ModelForm, PasswordInput
from booker.models import BookRequest



class BookRequestForm(ModelForm):
	class Meta:
		model = BookRequest
		fields = '__all__'