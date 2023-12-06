from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
import uuid

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('mybooks/', views.mybooks, name='mybooks'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('borrowed/', views.borrowed, name='borrowed'),
    path('addbooks/', views.addbooks, name='addbooks'),
    path('bookinfo/<uuid:book_id>/', views.bookinfo, name='bookinfo'),
    path('requests/', views.requests, name='requests'),
    # path('add_to_wishlist/<uuid:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    # path('book_detail/<uuid:book_id>/', views.book_detail, name='book_detail'),
    # path('add_review/<uuid:book_id>/', views.add_review, name='add_review'),
    # path('request-to-borrow/<uuid:book_id>/', views.request_to_borrow, name='request_to_borrow'),
    path('add-to-wishlist/<uuid:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)