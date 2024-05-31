from django.urls import path
from .views import HomeView,HomeDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('delete/<int:pk>', HomeDeleteView.as_view(), name='delete'),

]