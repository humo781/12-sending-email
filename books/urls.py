from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='list'),
    path('book/detail/<int:pk>/', views.BookDetailView.as_view(), name='detail'),
    path('book/create/', views.BookCreateView.as_view(), name='create'),
    path('book/update/<int:pk>/', views.BookUpdateView.as_view(), name='update'),
    path('book/delete/<int:pk>/', views.BookDeleteView.as_view(), name='delete'),
]
