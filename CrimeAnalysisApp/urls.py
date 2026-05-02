from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('adminlogin/', views.AdminLogin, name='adminlogin'),
    path('admin/', views.Admin, name='admin'),

    path('upload/', views.UploadDataset, name='upload'),
    path('uploadAction/', views.UploadDatasetAction, name='uploadAction'),

    path('cluster/', views.ClusterPrediction, name='cluster'),
    path('clusterAction/', views.ClusterPredictionAction, name='clusterAction'),

    path('future/', views.FuturePrediction, name='future'),
    path('futureAction/', views.FuturePredictionAction, name='futureAction'),

    path('analysis/', views.Analysis, name='analysis'),
    path('analysisAction/', views.AnalysisAction, name='analysisAction'),
]