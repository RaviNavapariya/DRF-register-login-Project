from django.urls import path
from.views import UserSignupApiview,UserLoginApiview

urlpatterns = [
    path('signup/',UserSignupApiview.as_view(),name='signup'),
    path('login/',UserLoginApiview.as_view,name='login')

]
