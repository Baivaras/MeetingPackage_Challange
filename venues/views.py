from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.circle_utils import get_circle_boundaries
from venues.models import Venue
from venues.serializers import VenueSerializer


class ListNearbyVenuesView(APIView):
    """
    List view for a venues within the given boundaries

    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        lat = request.GET.get('lat', None)
        lon = request.GET.get('lon', None)
        radius = request.GET.get('radius', None)

        if not lat or not lon or not radius:
            return Response({'message': 'Missing parameters latitude, longitude or radius'}, status=400)

        lat, lat2, lon, lon2 = get_circle_boundaries(float(lat), float(lon), int(radius))

        # get all venues in the range
        venues = Venue.objects.filter(latitude__range=(lat2, lat), longitude__range=(lon2, lon))

        if not venues.exists():
            return Response({'message': 'No venues found'})

        return Response(VenueSerializer(venues, many=True).data)
