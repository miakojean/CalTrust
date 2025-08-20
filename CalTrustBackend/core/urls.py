from django.urls import path
from .views import NotificationBulkActionView, NotificationView, NotificationDetailView

urlpatterns = [
    path('notifications/', NotificationView.as_view(), name='notifications-list'),
    path('notifications/<int:notification_id>/', NotificationDetailView.as_view(), name='notification-detail'),
    path('notifications/actions/', NotificationBulkActionView.as_view(), name='notifications-actions'),
]