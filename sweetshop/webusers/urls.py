from django.urls import path

from sweetshop.webusers.views import SignUpView, SignInView, SignOutView, UserDetailsView, UserEditView, UserDeleteView, \
    NoProfileView

urlpatterns = (
    path("register/", SignUpView.as_view(), name= "register user"),
    path("login/", SignInView.as_view(), name= "login user"),
    path("logout/", SignOutView.as_view(), name= "logout user"),
    path("no-profile/", NoProfileView.as_view(), name= "profile without auth"),
    path("profile/<int:pk>/", UserDetailsView.as_view(), name= "details profile"),
    path("profile/edit/<int:pk>/", UserEditView.as_view(), name= "edit profile"),
    path("profile/delete/<int:pk>/", UserDeleteView.as_view(), name= "delete profile"),
)