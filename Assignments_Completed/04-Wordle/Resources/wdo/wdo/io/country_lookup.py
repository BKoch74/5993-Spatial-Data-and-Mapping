ALIASES = {
    "Aland":                                          "Aland Islands",
    "British Virgin Islands":                         "Virgin Islands (British)",
    "Brunei":                                         "Brunei Darussalam",
    "Cape Verde":                                     "Cabo Verde",
    "East Timor":                                     "Timor-Leste",
    "French Southern and Antarctic Lands":            "French Southern Territories",
    "Guinea Bissau":                                  "Guinea-Bissau",
    "Hong Kong S.A.R.":                               "Hong Kong",
    "Ivory Coast":                                    "Côte d'Ivoire",
    "Macao S.A.R":                                    "Macau",
    "Macedonia":                                      "North Macedonia",
    "Palestine":                                      "State of Palestine",
    "Pitcairn Islands":                               "Pitcairn",
    "Republic of Congo":                              "Republic of the Congo",
    "Republic of Serbia":                             "Serbia",
    "Saint Barthelemy":                               "Saint Barthélemy",
    "Saint Helena":                                   "Saint Helena, Ascension and Tristan da Cunha",
    "South Georgia and South Sandwich Islands":       "South Georgia and the South Sandwich Islands",
    "Swaziland":                                      "Eswatini",
    "The Bahamas":                                    "Bahamas",
    "Turkey":                                         "Türkiye",
    "United Republic of Tanzania":                    "Tanzania",
    "United States Virgin Islands":                   "Virgin Islands (U.S.)",
    "Vatican":                                        "Holy See",
}


def build_country_lookup(countries_geojson, flag_index):
    flag_by_name = {entry["name"]: entry for entry in flag_index}

    lookup = {}
    misses = []

    for feature in countries_geojson.get("features", []):
        props = feature["properties"]
        name  = props.get("ADMIN", "")
        iso3  = props.get("ISO_A3", "")

        flag_entry = flag_by_name.get(name)

        if flag_entry is None:
            flag_entry = flag_by_name.get(ALIASES.get(name, ""))

        if flag_entry is None:
            misses.append(f"{name} ({iso3})")
            iso2      = None
            flag_path = None
        else:
            iso2      = flag_entry["code"]
            flag_path = flag_entry.get("flag_4x3", f"flags/4x3/{iso2}.svg")

        lookup[iso3] = {
            "name":      name,
            "iso3":      iso3,
            "iso2":      iso2,
            "flag_path": flag_path,
            "feature":   feature,
        }

    if misses:
        print(
            f"[build_country_lookup] {len(misses)} unmatched "
            f"(no flag will show for these):\n  " + "\n  ".join(misses)
        )

    return lookup
