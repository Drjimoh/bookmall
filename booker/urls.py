from django.urls import  path
from booker import  views
from django.contrib.auth.decorators import login_required

app_name = 'booker'
urlpatterns = [
	path('', views.index,
		name='index'),
	path('<int:pk>/about/requestedbook', 
			views.RequestedBookView.as_view(),
			name='request_detail'),
	path('<int:pk>/about/offeredbook', 
			views.OfferedBookView.as_view(),
			name='offer_detail'),
	path('request/book', login_required(views.BookRequestView.as_view()),
		name='request_book'),
	path('request/list', login_required(views.RequestListView.as_view()),
		name='request_list'),
	path('offer/list', login_required(views.OfferListView.as_view()),
		name='offer_list'),
	path('request/success', views.request_success,
		name='request_success'),
	path('offer/book', login_required(views.BookOfferView.as_view()),
		name='offer_book'),
	path('offer/success', views.offer_success,
		name='offer_success'),
	path('booker/api', views.BookerApiView.as_view(),
		name='booker_api'),
	path('bookrequest/api', login_required(views.BookRequestApiView.as_view()),
		name='bookrequest_api'),

	path('<int:pk>/delete/request', views.delete_requested_book, 
		name='delete_requested_book'),
	path('<int:pk>/delete/offer', views.delete_offered_book,
		name= 'delete_offered_book'),
    ]
