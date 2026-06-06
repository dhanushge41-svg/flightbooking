from django.urls import path
from .views import *
urlpatterns = [
    path('home/',home,name='home'),
    path('book/<int:id>/',book_flight,name='booking'),
    path('history/',booking_history, name='history'),
    path('update/<int:id>/', update_booking, name='update_booking'),
    path('delete/<int:id>/', delete_booking, name='delete_booking'),
    path('historyf/',history,name='historyf'),
    path('rigister/',register,name='register'),
    path('',login_,name='login_'),
    path('logout_/',logout_,name='logout_'),
    path('profile/',profile_,name='profile_'),
    path('update_/',update_,name='update_'),
    path('reset_pasw/',reset_pasw,name='reset_pasw'),
    path('forget/',forget,name='forget'),
]