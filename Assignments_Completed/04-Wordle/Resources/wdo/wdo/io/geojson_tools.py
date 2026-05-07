import json


def load_geojson(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    features = data.get("features", [])
    data["feature_count"] = len(features)
    data["property_names"] = list(features[0]["properties"].keys()) if features else []
    return data


def iter_features(geojson):
    yield from geojson.get("features", [])
