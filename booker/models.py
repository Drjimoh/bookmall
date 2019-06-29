from django.db import models
from django.conf import settings



offer_type = (
	('Free', 'Free'),
	('Negotiable', 'Negotiable'),
	)

class Booker(models.Model):
	id = models.IntegerField(primary_key=True, editable=False)
	bookman = models.ForeignKey(to=settings.AUTH_USER_MODEL,
						 on_delete=models.SET_NULL, null=True, default=1)
	title = models.CharField(max_length=200, blank=False, null=False)
	author = models.CharField(max_length=100, blank=False, null=False)
	price = models.CharField(choices=offer_type, max_length=100, default='Free')
	location = models.CharField(max_length=100, blank=False, null=False, 
		default='Nigeria')
	def __str__(self):
		return str(self.title) + ' by ' + str(self.author)


class BookRequest(models.Model):
	id = models.IntegerField(primary_key=True, editable=False)
	bookman = models.ForeignKey(to=settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL, null=True, default=1)
	title = models.CharField(max_length=200, null=False, blank=False)
	author = models.CharField(max_length=100, null= False, blank=False)
	location = models.CharField(max_length=100, null=False, blank=False)
	def __str__(self):
		return str(self.title) + ' by ' + str(self.author)

		