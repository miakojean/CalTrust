from django.urls import path
from .views import *

urlpatterns = [
    #Post a review about firm
    path('firms/<int:firm_id>/', ReviewAPIView.as_view(), name='firm-reviews'),
    #Get a specific review
    path('<int:review_id>/', ReviewAPIView.as_view(), name='review-detail'),
    #Get review about Firm
    path('firm/<int:firm_id>/review/', FirmReviewsAPIView.as_view(), name='firm-reviews'),
    path('response/', RespondToReviewAPIView.as_view(), name='response'),  
    path('reviews/<int:review_id>/respond/', RespondToReviewAPIView.as_view(), name='respond-to-review'),
    path('reviews/search/', ReviewSearchView.as_view(), name='review-search'),
    path('public/recent/', RecentReviewsAPIView.as_view(), name='public-recent-reviews'),
]