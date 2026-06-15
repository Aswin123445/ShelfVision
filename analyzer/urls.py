from django.urls import path
from .views import AnalyzeShelfView

urlpatterns = [
    path("analyze/", AnalyzeShelfView.as_view()),
]
