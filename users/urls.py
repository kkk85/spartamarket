from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('<int:pk>/like/', views.like, name='like'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('<int:pk>/follow',views.follow, name='follow')
]