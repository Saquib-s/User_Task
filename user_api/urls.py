from .views import User_view
from .views import User_view,check_size,get_client_ip
from django.urls import path

urlpatterns = [
    path('usr/',User_view.as_view()),
    path('usr/<int:id>/', User_view.as_view()),
    path('usr/size/', check_size.as_view()),
    path('usr/ip/', get_client_ip.as_view())


]