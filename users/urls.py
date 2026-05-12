from django.urls import path
from .views import GetCSRFToken, LoginView, LogoutView, MeView, StaffListView

urlpatterns = [
    path('csrf/', GetCSRFToken.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('me/', MeView.as_view()),
    path('staff/', StaffListView.as_view()),
]
