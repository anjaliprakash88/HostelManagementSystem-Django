from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_form, name='home'),
    path('loginView', views.loginView, name='loginView'),
    path('regform/', views.register_form, name='regform'),
    path('logout', views.logoutView, name='logout'),
    path('register', views. registerView, name='register'),

    path('student', views.student, name='student'),
    path('hostel_view/<int:location_id>/', views.hostel_view, name='hostel_view'),
    path('booking/', views.booking_form, name='booking_form'),
    path('hostel/<int:hostel_id>/rooms/', views.hostel_room_list, name='hostel_room_list'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),


    path('warden', views.warden, name='warden'),

    path('admin1', views.admin1, name='admin1'),
]