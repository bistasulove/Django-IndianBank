from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('',views.api_root),
    path('banks/', views.BankList.as_view(), name='bank-list'),
    path('branches/', views.BranchList.as_view(), name='branch-list'),
    path('banks/<int:pk>/', views.BankDetail.as_view(),name='bank-detail'),
    path('branches/<int:pk>/', views.BranchDetail.as_view(),name='branch-detail'),
])


