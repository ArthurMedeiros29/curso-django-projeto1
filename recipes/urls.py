from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),  # noqa: E501
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    path('recipes/search/', lambda request: ..., name="search"),
]
