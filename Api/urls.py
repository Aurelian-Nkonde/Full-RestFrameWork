from django.urls import path
from . import views

urlpatterns = [
	path('', views.BookList.as_view(), name='book-list'),
	path('book-list/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
	path('author-list/', views.AuthorList.as_view(), name='author-list'),
	path('author-list/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
	path('user-list/', views.UserList.as_view(), name='user-list'),
	path('user-detail/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
]