from django.urls import  path
from booker import  views

app_name = 'booker'
urlpatterns = [
	path('', views.Homepage.as_view(),
		name='index'),
	path('<int:pk>/about/book', 
			views.BookView.as_view(),
			name='detail'),
	path('request/book', views.BookRequestView.as_view(),
		name='request_book'),
	path('request/list', views.RequestListView.as_view(),
		name='request_list'),
	path('offer/list', views.OfferListView.as_view(),
		name='offer_list'),
	path('request/success', views.request_success,
		name='request_success'),
    ]
