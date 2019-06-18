from django.shortcuts import render
from django.views import generic 
from booker.models import Booker, BookRequest
from booker.forms import BookRequestForm, BookOfferForm
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response 
from booker.serializers import BookerSerializer, BookRequestSerializer
from rest_framework import status
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect

class Homepage(generic.ListView):
	model = Booker 
	requests = list(BookRequest.objects.all())
	context = {'requests':requests}
	def  get_queryset(self):
		return Booker.objects.all()




class RequestedBookView(generic.DetailView):
	model = BookRequest 

class OfferedBookView(generic.DetailView):
	model = Booker


	
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
	#@login_required()
	def get_queryset(self, *args, **kwargs):
		return BookRequest.objects.filter(
			bookman=self.request.user
			).order_by('id')


class BookRequestView(generic.CreateView):
	form_class = BookRequestForm
	template_name = 'booker/request_book.html'
	success_url = reverse_lazy('booker:request_success')

	def form_valid(self, form_class):
		print(self.request.user)
		book_requested = form_class.save(commit=False)
		book_requested.bookman = User.objects.get(username=self.request.user)
		book_requested.save()
		return HttpResponseRedirect(self.success_url)

class BookOfferView(generic.CreateView):
	form_class = BookOfferForm
	template_name = 'booker/offer_book.html'
	success_url = reverse_lazy('booker:offer_success')

	def form_valid(self, form_class):
		print(self.request.user)
		book_requested = form_class.save(commit=False)
		book_requested.bookman = User.objects.get(username=self.request.user)
		book_requested.save()
		return HttpResponseRedirect(self.success_url)


def index(request):
	book_requests = list(BookRequest.objects.all())[::-1]
	book_offers = list(Booker.objects.all())[::-1]
	return render(request, 
		'booker/booker_list.html',
		 {'book_requests':book_requests, 'book_offers':book_offers})
	

@login_required
def request_success(request):
	return render(request, 'booker/request_success.html', {})

@login_required
def offer_success(request):
	return render(request, 'booker/offer_success.html', {})

class BookerApiView(APIView):
	def get(self, response):
		booker = Booker.objects.all()
		serializer = BookerSerializer(booker, many=True)
		return Response(serializer.data)

	def post(self, response):
		serializer = BookerSerializer(data=response.data, many=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, 
				status=status.HTTP_201_CREATED)
		return Response(serializer.errors, 
			status=status.HTTP_400_BAD_REQUEST)

class BookRequestApiView(APIView):
	def get(self, response):
		bookrequest = BookRequest.objects.all()
		serializer = BookRequestSerializer(bookrequest, many=True)
		return Response(serializer.data)

	def post(self, response):
		serializer = BookRequestSerializer(data=response.data, many=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,
				status=status.HTTP_201_CREATED)
		return Response(serializer.errors, 
			status=status.HTTP_400_BAD_REQUEST)


def delete_offered_book(request, pk):
	book = Booker.objects.get(id=pk)
	book.delete()

	book_list = Booker.objects.filter(
			bookman=request.user
			)
	return render(request, 
		'booker/offered_book_deleted.html',
			 {'books':book_list})

def delete_requested_book(request, pk):
	book = BookRequest.objects.get(id=pk)
	book.delete()
	book_list = BookRequest.objects.filter(
			bookman=request.user
			)
	return render(request, 
		'booker/requested_book_deleted.html',
			 {'books':book_list})