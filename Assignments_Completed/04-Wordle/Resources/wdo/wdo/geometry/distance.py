import math

EARTH_RADIUS_KM = 6371.0088
EARTH_RADIUS_MI = 3958.8


def haversine_km(point1, point2):
    lat1, lon1 = math.radians(point1[0]), math.radians(point1[1])
    lat2, lon2 = math.radians(point2[0]), math.radians(point2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * EARTH_RADIUS_KM * math.asin(math.sqrt(a))


def haversine_miles(point1, point2):
    return haversine_km(point1, point2) * (EARTH_RADIUS_MI / EARTH_RADIUS_KM)
