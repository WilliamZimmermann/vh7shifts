from django.urls import path

from . import views

urlpatterns = [
    path('api/users/get', views.api_get_set_users),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]