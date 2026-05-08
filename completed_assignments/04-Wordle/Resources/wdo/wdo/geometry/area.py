import math

EARTH_RADIUS_KM = 6371.0088

EASY_THRESHOLD   = 1_000_000
MEDIUM_THRESHOLD =   100_000

TIERS = ("easy", "medium", "hard")


def polygon_area_km2(feature):
    geom = feature["geometry"]
    t    = geom["type"]
    if t == "Polygon":
        return abs(_ring_area_km2(geom["coordinates"][0]))
    if t == "MultiPolygon":
        return sum(abs(_ring_area_km2(poly[0])) for poly in geom["coordinates"])
    raise ValueError(f"polygon_area_km2: unsupported geometry type '{t}'")


def _ring_area_km2(coords):
    n = len(coords)
    if n < 3:
        return 0.0
    lons = [math.radians(c[0]) for c in coords]
    lats = [math.radians(c[1]) for c in coords]
    area = 0.0
    for i in range(n):
        prev_lon = lons[(i - 1) % n]
        next_lon = lons[(i + 1) % n]
        area += (next_lon - prev_lon) * math.sin(lats[i])
    return area * EARTH_RADIUS_KM ** 2 / 2.0


def difficulty_tier(area_km2):
    if area_km2 >= EASY_THRESHOLD:
        return "easy"
    if area_km2 >= MEDIUM_THRESHOLD:
        return "medium"
    return "hard"


def tier_label(tier):
    return {"easy": "🟢 Easy", "medium": "🟡 Medium", "hard": "🔴 Hard"}[tier]
