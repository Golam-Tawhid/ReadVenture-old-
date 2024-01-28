from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
import uuid
from .views import sign_in,custom_logout

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('addbooks/', views.addbooks, name='addbooks'),
    # path('add_to_wishlist/<uuid:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('add-to-wishlist/<uuid:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    # path('add_review/<uuid:book_id>/', views.add_review, name='add_review'),
    path('bookinfo/<uuid:book_id>/', views.bookinfo, name='bookinfo'),
    path('borrowed/', views.borrowed, name='borrowed'),
    # path('book_detail/<uuid:book_id>/', views.book_detail, name='book_detail'),
    path('home/', views.home, name='home'),
    path('logout/', custom_logout, name='logout'),
    path('mybooks/', views.mybooks, name='mybooks'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('profile/', views.profile, name='profile'),
    path('remove_book/<uuid:book_id>/', views.remove_book, name='remove_book'),
    path('remove_from_wishlist/<uuid:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('requests/', views.requests, name='requests'),
    path('request_to_borrow/<uuid:book_id>/', views.request_to_borrow, name='request_to_borrow'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('signup/', views.signup, name='signup'),
    #path('toggle_availablility/<uuid:book_id>/', views.toggle_availability, name='toggle_availability'),
    path('update_user/', views.update_user, name='update_user'),
    path('wishlist/', views.wishlist, name='wishlist'),
    #-------------------------------------------------------------
    #path('book_requests/', views.book_requests, name='book_requests'),
    re_path(r'^ignore_request/(?P<exchange_id>[\w-]+)/$', views.ignore_request, name='ignore_request'),
    re_path(r'^accept_request/(?P<exchange_id>[\w-]+)/$', views.accept_request, name='accept_request'),
    re_path(r'^cancel_request/(?P<exchange_id>[\w-]+)/$', views.cancel_request, name='cancel_request'),

    # path('ignore_request/<int:exchange_id>/', views.ignore_request, name='ignore_request'),
    # path('accept_request/<int:exchange_id>/', views.accept_request, name='accept_request'),
    # path('cancel_request/<int:exchange_id>/', views.cancel_request, name='cancel_request'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)