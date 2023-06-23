from django.urls import path
from .views import SearchResultsView , HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('search/', SearchResultsView.as_view(), name='search'),
]