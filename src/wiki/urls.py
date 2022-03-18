from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiRoutes),
    path('wiki-home-page/', views.wikiHomePage),
    path('query/', views.query),
]