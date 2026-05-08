import math

_COMPASS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


def initial_bearing(point1, point2):
    lat1, lon1 = math.radians(point1[0]), math.radians(point1[1])
    lat2, lon2 = math.radians(point2[0]), math.radians(point2[1])
    dlon = lon2 - lon1
    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    return (math.degrees(math.atan2(x, y)) + 360) % 360


def bearing_to_compass(bearing_deg):
    return _COMPASS[round(bearing_deg / 45) % 8]
