import base64
import pathlib
import random

from wdo.geometry.area import difficulty_tier, polygon_area_km2
from wdo.geometry.bbox import bbox_from_feature
from wdo.geometry.bearing import bearing_to_compass, initial_bearing
from wdo.geometry.distance import haversine_km, haversine_miles

ARROWS = {
    "N":  "↑",
    "NE": "↗",
    "E":  "→",
    "SE": "↘",
    "S":  "↓",
    "SW": "↙",
    "W":  "←",
    "NW": "↖",
}


def choose_target(features, seed=None, difficulty=None):
    if difficulty is not None:
        pool = [f for f in features
                if difficulty_tier(polygon_area_km2(f)) == difficulty]
        if not pool:
            raise ValueError(
                f"choose_target: no features found for difficulty={difficulty!r}. "
                f"Valid values: 'easy', 'medium', 'hard'."
            )
    else:
        pool = features
    return random.Random(seed).choice(pool)


def feature_center(feature, method="bbox"):
    if method == "bbox":
        return _center_bbox(feature)
    if method == "mean":
        return _center_mean(feature)
    raise ValueError(f"feature_center: unknown method {method!r}. Use 'bbox' or 'mean'.")


def _center_bbox(feature):
    min_lon, min_lat, max_lon, max_lat = bbox_from_feature(feature)
    return ((min_lat + max_lat) / 2, (min_lon + max_lon) / 2)


def _center_mean(feature):
    coords = _all_coords(feature["geometry"])
    lat = sum(c[1] for c in coords) / len(coords)
    lon = sum(c[0] for c in coords) / len(coords)
    return (lat, lon)


def _all_coords(geom):
    t = geom["type"]
    if t == "Polygon":
        return [pt for ring in geom["coordinates"] for pt in ring]
    if t == "MultiPolygon":
        return [pt for poly in geom["coordinates"] for ring in poly for pt in ring]
    raise ValueError(f"feature_center: unsupported geometry type '{t}'")


def guess_feedback(guess_feature, target_feature):
    guess_iso3  = guess_feature["properties"].get("ISO_A3", "")
    target_iso3 = target_feature["properties"].get("ISO_A3", "")
    correct     = guess_iso3 == target_iso3

    g_center = feature_center(guess_feature)
    t_center = feature_center(target_feature)

    dist_km  = haversine_km(g_center, t_center)
    dist_mi  = haversine_miles(g_center, t_center)
    bearing  = initial_bearing(g_center, t_center)
    compass  = bearing_to_compass(bearing)

    return {
        "correct":        correct,
        "distance_km":    round(dist_km,  1),
        "distance_miles": round(dist_mi,  1),
        "bearing_deg":    round(bearing,  1),
        "compass":        compass,
        "arrow":          ARROWS[compass],
    }


def format_feedback(result, units="km"):
    if result["correct"]:
        return "Correct!"
    dist       = result["distance_km"] if units == "km" else result["distance_miles"]
    unit_label = "km" if units == "km" else "mi"
    return f"{dist:,.0f} {unit_label} away  {result['arrow']} {result['compass']}"


def _flag_src(flag_path, flag_base_dir):
    if not flag_path:
        return None
    full = pathlib.Path(flag_base_dir) / flag_path
    if full.exists():
        data = base64.b64encode(full.read_bytes()).decode()
        return f"data:image/svg+xml;base64,{data}"
    iso2 = pathlib.Path(flag_path).stem
    return f"https://flagcdn.com/w40/{iso2}.png"


def render_guess_row(country_name, flag_path, arrow, distance_km,
                     flag_base_dir=None, guess_number=None):
    if distance_km < 500:
        badge_color = "#2a9d8f"
        emoji       = "🔥"
    elif distance_km < 2000:
        badge_color = "#e9c46a"
        emoji       = "🌡️"
    else:
        badge_color = "#e76f51"
        emoji       = "🧊"

    src = _flag_src(flag_path, flag_base_dir) if flag_base_dir else None
    if not src and flag_path:
        iso2 = pathlib.Path(flag_path).stem
        src  = f"https://flagcdn.com/w40/{iso2}.png"

    flag_html = (
        f'<img src="{src}" width="36" height="24" '
        'style="border:1px solid #ddd;border-radius:2px;'
        'object-fit:cover;flex-shrink:0" '
        'onerror="this.style.display=\'none\'">'
        if src else
        '<span style="display:inline-block;width:36px"></span>'
    )

    num_html = (
        f'<span style="width:22px;text-align:right;color:#bbb;'
        f'font-size:12px;flex-shrink:0">{guess_number}</span>'
        if guess_number is not None else ""
    )

    return (
        f'<div style="display:flex;align-items:center;gap:10px;'
        f'padding:7px 10px;border-bottom:1px solid #f0f0f0;'
        f'font-family:-apple-system,system-ui,sans-serif;font-size:14px">'
        f'{num_html}'
        f'{flag_html}'
        f'<span style="flex:1;font-weight:500">{country_name}</span>'
        f'<span style="font-size:20px">{arrow}</span>'
        f'<span style="background:{badge_color};color:#fff;padding:2px 10px;'
        f'border-radius:12px;font-weight:600;min-width:95px;text-align:center;'
        f'font-variant-numeric:tabular-nums">{distance_km:,.0f} km</span>'
        f'<span style="font-size:16px" title="{distance_km:,.0f} km away">{emoji}</span>'
        f'</div>'
    )
