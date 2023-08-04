from django.urls import path
from . import views

app_name = 'workorder'

urlpatterns = [
    path("search/", views.HoistWorkOrderListView.as_view(), name="hwo_search"),
]