from django.urls import path
from .views import ReviewAPIView, ReviewSearchView, RecentReviewsAPIView

urlpatterns = [
    path('firms/<int:firm_id>/', ReviewAPIView.as_view(), name='firm-reviews'),
    path('reviews/<int:review_id>/', ReviewAPIView.as_view(), name='review-detail'),
    path('reviews/search/', ReviewSearchView.as_view(), name='review-search'),
    path('public/recent/', RecentReviewsAPIView.as_view(), name='public-recent-reviews'),
]