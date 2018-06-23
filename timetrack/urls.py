from django.urls import path

from . import views

urlpatterns = [
    path('api/companies/get', views.api_get_set_companies_and_settings),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]