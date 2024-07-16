from django.urls import path
from .views import Attendance_ReportView, Revenue_ReportView, Vendor_Performance_ReportView


urlpatterns = [
    path('attendance_report/',Attendance_ReportView.as_view({'get':'list', 'post': 'create'})),
    path('attendance_report/<int:pk>/',Attendance_ReportView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('revenue_report/', Revenue_ReportView.as_view({'get':'list', 'post':'create'})),
    path('revenue_report/<int:pk>/', Revenue_ReportView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('vendor_performance_report/', Vendor_Performance_ReportView.as_view({'get':'list', 'post':'create'})),
    path('vendor_performance_report/<int:pk>/', Vendor_Performance_ReportView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
]
