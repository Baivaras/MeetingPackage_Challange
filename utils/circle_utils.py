import math


def get_circle_boundaries(lat: float, lon: float, radius_in_km: int) -> tuple:
    """
    Returns tuple of latitude and longitude min max boundaries.
    """

    lat_change = radius_in_km / 111.2
    lon_change = abs(math.cos(lat * (math.pi / 180)))

    lat_min = lat - lat_change
    lon_min = lon - lon_change
    lat_max = lat + lat_change
    lon_max = lon + lon_change

    return lat_max, lat_min, lon_max, lon_min
