from django.urls import path
from . import views

app_name = 'workorder'

urlpatterns = [
    path("search/", views.HoistWorkOrderListView.as_view(), name="hwo_search"),
    path("<int:hwo>/", views.HoistWorkOrderDetailView.as_view(), name="hwo_detail"),
    path("add/", views.AddNewHoistWorkOrderView.as_view(), name="add_hwo"),
    path("customer/add/", views.AddNewCustomerView.as_view(), name="add_customer"),
    path("add/excel/", views.UploadExcelView.as_view(), name="add_excel"),
    path("add/excel/success/", views.UploadExcelSuccessView.as_view(), name="add_success"),
]
