from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
import uuid
from .views import sign_in,custom_logout

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('home/', views.home, name='home'),
    path('logout/', custom_logout, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('mybooks/', views.mybooks, name='mybooks'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('borrowed/', views.borrowed, name='borrowed'),
    path('addbooks/', views.addbooks, name='addbooks'),
    path('bookinfo/<uuid:book_id>/', views.bookinfo, name='bookinfo'),
    path('requests/', views.requests, name='requests'),
    path('remove_book/<uuid:book_id>/', views.remove_book, name='remove_book'),
    path('remove_from_wishlist/<uuid:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),




    # path('add_to_wishlist/<uuid:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    # path('book_detail/<uuid:book_id>/', views.book_detail, name='book_detail'),
    # path('add_review/<uuid:book_id>/', views.add_review, name='add_review'),
    path('request_to_borrow/<uuid:book_id>/', views.request_to_borrow, name='request_to_borrow'),
    path('add-to-wishlist/<uuid:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('update_user/', views.update_user, name='update_user'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)