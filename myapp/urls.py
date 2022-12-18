from django.urls import path,include
from myapp import views

app_name='app'
urlpatterns = [
    path('products', views.products, name='products'),
    path('events', views.all_events, name="list-events"),
]

