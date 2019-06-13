from django.forms import ModelForm, PasswordInput
from booker.models import BookRequest, Booker 



class BookRequestForm(ModelForm):
	class Meta:
		model = BookRequest 
		exclude = ['bookman']


class BookOfferForm(ModelForm):
	class Meta:
		model = Booker
		exclude = ['bookman']
