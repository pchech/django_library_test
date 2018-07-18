from django.conf.urls import url
from django.urls import include,path

from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path(r'^books/$', views.BookListView.as_view(), name='books'),
	path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
	path(r'^author/$', views.AuthorListView.as_view(), name='author'),
	path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
	
]
urlpatterns += [   
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
urlpatterns += [   
    url(r'^loanbooks/$', views.AllLoanedBookView.as_view(), name='all-borrowed'),
]
urlpatterns += [   
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]
urlpatterns += [  
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]
urlpatterns += [  
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
]
urlpatterns += [  
    url(r'^split/$', views.split_calc, name='split'),
]