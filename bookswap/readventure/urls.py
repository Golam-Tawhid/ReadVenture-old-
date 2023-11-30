from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('home/', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('mybooks/', views.mybooks, name='mybooks'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('borrowed/', views.borrowed, name='borrowed'),
    path('addbooks/', views.addbooks, name='addbooks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)