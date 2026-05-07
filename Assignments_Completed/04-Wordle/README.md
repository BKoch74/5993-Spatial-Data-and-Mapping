# 04 — Worldle

A Wordle-style geography game built in Jupyter. A mystery country polygon is shown on the map with no name or label. Pick a country from the dropdown and click **Guess**. Each wrong guess shows the flag, a directional arrow toward the target, and the great-circle distance. Six guesses to get it.

---

## wdo functions added or finished

| Function | Module | Microlesson | Notes |
|---|---|---|---|
| `bbox_from_feature`, `bbox_from_features` | `wdo.geometry.bbox` | 3 | Flattens Polygon/MultiPolygon coords to min/max lon-lat |
| `make_map`, `add_geojson`, `fit_map_to_geojson` | `wdo.maps.leaflet_helpers` | 3 | ipyleaflet wrappers with CartoDB Positron default |
| `feature_center` | `wdo.games.worldle` | 4 | Two methods: `bbox` (fast) and `mean` (vertex average) |
| `choose_target` | `wdo.games.worldle` | 5 | Seeded random pick; extended with `difficulty=` parameter for grad-student add-on |
| `guess_feedback`, `format_feedback` | `wdo.games.worldle` | 6 | Haversine distance + initial bearing FROM guess TOWARD target |
| `render_guess_row` | `wdo.games.worldle` | 7 | HTML row with base64 flag, arrow, colour-coded distance badge |
| `build_country_lookup` | `wdo.io.country_lookup` | 2 | Name-based join between GeoJSON ADMIN and flag-icons; uses ALIASES for mismatches |
| `polygon_area_km2`, `difficulty_tier`, `tier_label` | `wdo.geometry.area` | Grad-student add-on | Chamberlain-Duquette spherical shoelace formula for polygon area; three difficulty tiers |

---

## Country-name aliases

The polygon GeoJSON uses `ADMIN` names that differ from the flag-icons `name` field in 24 cases. Rather than a hardcoded ISO-3 → ISO-2 dictionary, `build_country_lookup` does a direct name match and falls back to the `ALIASES` dict in `wdo/io/country_lookup.py` for every known mismatch.

| GeoJSON ADMIN name | flag-icons name |
|---|---|
| Aland | Aland Islands |
| British Virgin Islands | Virgin Islands (British) |
| Brunei | Brunei Darussalam |
| Cape Verde | Cabo Verde |
| East Timor | Timor-Leste |
| French Southern and Antarctic Lands | French Southern Territories |
| Guinea Bissau | Guinea-Bissau |
| Hong Kong S.A.R. | Hong Kong |
| Ivory Coast | Côte d'Ivoire |
| Macao S.A.R | Macau |
| Macedonia | North Macedonia |
| Palestine | State of Palestine |
| Pitcairn Islands | Pitcairn |
| Republic of Congo | Republic of the Congo |
| Republic of Serbia | Serbia |
| Saint Barthelemy | Saint Barthélemy |
| Saint Helena | Saint Helena, Ascension and Tristan da Cunha |
| South Georgia and South Sandwich Islands | South Georgia and the South Sandwich Islands |
| Swaziland | Eswatini |
| The Bahamas | Bahamas |
| Turkey | Türkiye |
| United Republic of Tanzania | Tanzania |
| United States Virgin Islands | Virgin Islands (U.S.) |
| Vatican | Holy See |

15 features are coded `ISO_A3 = -99` in the GeoJSON (disputed territories, military bases, etc.) and are excluded from the playable pool entirely. No alias can fix a missing ISO code.

---

## Known bugs / honest notes

**bbox centre drifts for MultiPolygon countries**
`feature_center(method='bbox')` computes the centre of the axis-aligned bounding box. For countries whose GeoJSON includes overseas territories as separate polygons, France (includes French Guiana), United States (includes Alaska and Hawaii), Netherlands (includes Caribbean islands), the bounding box spans far beyond the main landmass. France's bbox centre lands near 14 °N, 3 °W (somewhere in Mali), not Paris. The `method='mean'` option is slightly better but still biased toward vertex-dense coastlines. Fixing this properly would require a proper centroid-of-largest-polygon heuristic.

**Antimeridian-crossing countries (Russia, Fiji, USA)**
`bbox_from_feature` treats longitudes as plain numbers. Russia spans −180 ° to +180 °, so its bbox centre longitude comes out near 0 °. The bbox still *fits* correctly on the ipyleaflet map because Leaflet clips to the tile, but the bearing calculation for those countries will use a wrong centre point.

**Small-polygon area error (Monaco, Vatican, Gibraltar)**
The Chamberlain-Duquette formula accumulates relative error for very small polygons. Monaco's computed area is ~19 km² vs the real ~2 km², Gibraltar ~4 km² vs ~6 km². These are still firmly in the `hard` tier so difficulty assignment is unaffected, but the raw area numbers printed in the analysis cell are inaccurate for micro-states.

**No antimeridian wrapping in distance/bearing**
`haversine_km` and `initial_bearing` work in decimal degrees and do not special-case the antimeridian. Guessing a country near the date line when the target is on the other side may produce a longer-than-expected distance and a backwards arrow.

---

## Screenshot — completed round

![Completed round](screenshot.png)

