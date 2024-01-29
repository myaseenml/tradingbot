from django.urls import path
from test_app import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about', views.about, name='about'),
    # path('diseases', views.diseases, name='diseases'),
]