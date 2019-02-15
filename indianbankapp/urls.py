from django.urls import path
from . import views


app_name = "indianbankapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('branch/<str:ifsc_code>', views.BranchIfscView.as_view(), name="branch"),
    path('branches/', views.BranchCityView.as_view(), name="branches"),

]


