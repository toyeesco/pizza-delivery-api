from django.urls import path

from authentication.views import HelloAuthView, UserCreationView

urlpatterns = [
    path("", HelloAuthView.as_view(), name='hello_auth'),
    path('signup/', UserCreationView.as_view(), name="signup"),
]
