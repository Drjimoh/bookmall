from django.shortcuts import render
from django.views import generic 
from booker.models import Booker, BookRequest
from booker.forms import BookRequestForm
from django.conf import settings
from django.urls import reverse_lazy


class Homepage(generic.ListView):
	model = Booker 

	def  get_queryset(self):
		return Booker.objects.all()

class BookView(generic.DetailView):
	model = Booker 

class BookRequestView(generic.CreateView):
	form_class = BookRequestForm
	template_name = 'booker/request_book.html'
	success_url = reverse_lazy('booker:request_success')

	
class OfferListView(generic.ListView):
	model = Booker
	template_name = 'booker/offer_list.html'

	def get_queryset(self):
		return Booker.objects.filter(
			bookman=self.request.user
			)

class RequestListView(generic.ListView):
	model = BookRequest
	template_name = 'booker/request_list.html'

	def get_queryset(self):
		return BookRequest.objects.filter(
			bookman=self.request.user
			)
def request_success(request):
	return render(request, 'booker/request_success.html', {})
