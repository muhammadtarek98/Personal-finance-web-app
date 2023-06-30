from django.urls import include, path
from rest_framework import routers
from .views import SavingGoalViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'saving-goals', SavingGoalViewSet, basename='saving-goal')

urlpatterns = [
    path('', include(router.urls)),
    path('saving-goals/', views.saving_goal_list),
    path('create-saving-goal/', views.create_saving_goal),
]