from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('banks/', views.BankList.as_view() ),
    path('banks/<int:pk>/', views.BankDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
