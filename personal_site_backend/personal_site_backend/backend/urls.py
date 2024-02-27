from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/api/data/', views.get_data, name='get_data'),
]
