from django.urls import path
from . import views


app_name = "indianbankapp"

urlpatterns = [
    path('', views.apphome, name="apphome"),
    path('branch/<str:ifsc_code>', views.BranchView.as_view(), name="branch"),
    path('branches/', views.BranchListView.as_view(), name="branches"),

]


