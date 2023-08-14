from django.urls import path
from . import views
from workorder.views import HoistWorkOrderDetailView

app_name = 'infosheet'

urlpatterns = [
    path("search/", views.InformationSheetListView.as_view(), name="his_search"),
    path("<str:his>/", views.InformationSheetDetailView.as_view(), name="his_detail"),
]
