from django.urls import path
from . import views
urlpatterns = [
    path('', views.predictor, name='predictor'),
    path('predict/', views.predict_diabetes, name='predict_diabetes'),
]
