def bbox_from_feature(feature):
    coords = _flatten_coords(feature["geometry"])
    lons = [c[0] for c in coords]
    lats = [c[1] for c in coords]
    return min(lons), min(lats), max(lons), max(lats)


def bbox_from_features(features):
    boxes = [bbox_from_feature(f) for f in features]
    return (
        min(b[0] for b in boxes),
        min(b[1] for b in boxes),
        max(b[2] for b in boxes),
        max(b[3] for b in boxes),
    )


def _flatten_coords(geom):
    t = geom["type"]
    if t == "Polygon":
        return [pt for ring in geom["coordinates"] for pt in ring]
    if t == "MultiPolygon":
        return [pt for poly in geom["coordinates"] for ring in poly for pt in ring]
    raise ValueError(f"bbox_from_feature: unsupported geometry type '{t}'")
