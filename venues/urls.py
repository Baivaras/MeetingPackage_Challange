from django.urls import path

from venues.views import ListNearbyVenuesView

urlpatterns = [
    path('get-nearby-venues/', ListNearbyVenuesView.as_view(), name='get-nearby-venues'),
]
