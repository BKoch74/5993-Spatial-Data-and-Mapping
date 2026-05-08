from ipyleaflet import GeoJSON, Map, basemaps

from wdo.geometry.bbox import bbox_from_feature, bbox_from_features

DEFAULT_STYLE = {
    "color":       "#264653",
    "fillColor":   "#2a9d8f",
    "weight":      2,
    "fillOpacity": 0.5,
}


def make_map(center=(20, 10), zoom=2, basemap=None, scroll_wheel_zoom=True):
    if basemap is None:
        basemap = basemaps.CartoDB.Positron
    return Map(
        center=center,
        zoom=zoom,
        basemap=basemap,
        scroll_wheel_zoom=scroll_wheel_zoom,
        layout={"height": "420px"},
    )


def add_geojson(map_obj, data, style=None):
    layer = GeoJSON(data=data, style=style or DEFAULT_STYLE)
    map_obj.add(layer)
    return layer


def fit_map_to_geojson(map_obj, data):
    if data.get("type") == "FeatureCollection":
        min_lon, min_lat, max_lon, max_lat = bbox_from_features(data["features"])
    else:
        min_lon, min_lat, max_lon, max_lat = bbox_from_feature(data)
    map_obj.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])
