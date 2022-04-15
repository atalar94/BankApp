from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Sube",views.SubeViewSet,basename="Sube")

app_name="Banking"



urlpatterns = [
    path("",include(router.urls)),
    path("login/",views.UserLogin.as_view(),name="login"),#user/login/
    path("logout/",views.UserLogout.as_view(),name="logout"),
    path("register/",views.RegisterUser.as_view(),name="register"),
    path("assign/<str:name>/",views.AssignCustomerToBranch.as_view(),name="assign"),
    path("deposit/",views.Deposit.as_view(),name="deposit"),
    path("send-money/<str:name>/",views.SendMoney.as_view(),name="send_money"),
    path("wd/",views.WithDraw.as_view(),name="withdraw"),
    path("users/",views.AllUsers.as_view(),name="all_users"),
]