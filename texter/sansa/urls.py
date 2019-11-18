from django.urls import path
from .views import main_page, created_page

urlpatterns=[
	path('', main_page, name='main_page_url'),
	path('created/', created_page, name='text_create_url')
]