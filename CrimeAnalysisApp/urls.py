from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminlogin/', views.Admin, name='Admin'),   # 🔥 THIS LINE IS IMPORTANT
    path('cluster/', views.ClusterPrediction, name='ClusterPrediction'),
    path('future/', views.FuturePrediction, name='FuturePrediction'),
    path('analysis/', views.Analysis, name='Analysis'),
]