from accountapp.views import hello_world, AccountCreateView
from django.urls import path
from django.urls.conf import include

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('signup/', AccountCreateView.as_view(), name='signup'),
]