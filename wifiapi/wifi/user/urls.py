from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('postwifi/',views.postwifi.as_view()),
    path('getwifi/', views.getwifi.as_view()),
]