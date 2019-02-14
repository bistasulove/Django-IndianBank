from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('banks',views.BanksView)
router.register('branches',views.BranchesView)

urlpatterns = [
    path('', include(router.urls))
]
