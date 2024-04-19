from django.urls import path
from . import views

app_name='products'
urlpatterns = [
    path('<int:pk>/',views.product, name='product'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/',views.delete, name='delete'),
]