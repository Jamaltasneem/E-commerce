from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('new',views.new),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('place_order/<int:product_id>/', views.place_order, name='place_order'),

]