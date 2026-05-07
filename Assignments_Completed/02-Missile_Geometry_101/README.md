# Project 01 — Missile Geometry 101

**Author:** Bryce Koch
**Course:** CMPS 5993
**Semester:** Spring 2026

---

## Overview

This project simulates a spatial defense analysis scenario for the World Defense Organization (WDO). Using Python, GeoPandas, Shapely, and Folium, simulated threats (alien, orbital, airborne, and kaiju-class) are analyzed geometrically — tracking their origins, trajectories, intersections with country borders, and projected damage zones. The goal is not to simulate weapons, but to reason spatially about motion, intersection, and consequence.

---

## Project Structure

```
Project_01/
│
│── Project_01_Code
│   ├── data
│   │   ├── world_borders
│   │   ├── countries.geojson
│   │   └── world_borders.zip
│   ├── outputs
│   │   ├── milestone_1.png
│   │   ├── milestone_1_map.html
│   │   ├── milestone_2.png
│   │   ├── milestone_2_map.html
│   │   ├── milestone_3.png
│   │   ├── milestone_3_map.html
│   │   ├── milestone_4.png
│   │   ├── milestone_4_map.html
│   │   ├── milestone_5.png
│   │   └── milestone_5_map.html
│   ├── src
│   │   ├── geo_math.py
│   │   ├── io_shapefile.py
│   │   ├── simulate_threats.py
│   │   ├── threats.json
│   │   └── viz_map.py
│   └── notebook.ipynb
│
└── README.md

```

---

## Milestones

### Milestone 1 — Plot the World
Loaded a world borders shapefile and rendered it as an interactive Folium map. The WDO base location (Dallas, TX) was added as a labeled marker. The projection file was inspected to confirm the coordinate reference system before any spatial operations were performed.

![Milestone 1 Screenshot]((https://github.com/BKoch74/5993-Spatial-Data-and-Mapping/blob/main/Assignments_Completed/Project_01/Project_01_Code/outputs/milestone_1.png)

---

### Milestone 2 — Distance & Bearing
Loaded simulated threat data from JSON and computed the haversine distance from each threat origin to the WDO base. The closest threat was identified and reported. All threat origins were plotted as circle markers — red for the closest threat, blue for all others.

![Milestone 2 Screenshot](https://github.com/BKoch74/5993-Spatial-Data-and-Mapping/blob/main/Assignments_Completed/Project_01/Project_01_Code/outputs/milestone_2.png)

---

### Milestone 3 — Trajectories
Converted each threat's motion into a visible trajectory by computing a projected destination point over a fixed 20-minute interval. Intermediate waypoints were generated every 2 minutes and rendered as PolyLines on the map. Green endpoint markers show each threat's projected position.

![Milestone 3 Screenshot](https://github.com/BKoch74/5993-Spatial-Data-and-Mapping/blob/main/Assignments_Completed/Project_01/Project_01_Code/outputs/milestone_3.png)

---

### Milestone 4 — Intersections & Borders
Determined which countries each trajectory intersects using a combination of ray-casting point-in-polygon checks and segment-level intersection tests. Trajectories passing within 300 km of the WDO base were flagged and colored red. Intersected countries are highlighted orange on the map.

![Milestone 4 Screenshot](screenshots/milestone_4.png)

---

### Milestone 5 — Damage Zones
Generated circular buffer zones around each threat's projected endpoint. Buffer size varies by threat type:

| Threat Type | Buffer Radius |
|-------------|--------------|
| Alien       | 500 km       |
| Orbital     | 300 km       |
| Airborne    | 150 km       |
| Kaiju       | 100 km       |

Countries falling within each damage zone were identified and assigned a severity rating:

| Severity | Criteria |
|----------|----------|
| CRITICAL | Buffer overlaps the WDO base |
| HIGH     | Strikes a heavily populated country |
| MEDIUM   | Hits any land |
| LOW      | Open ocean impact |

![Milestone 5 Screenshot](screenshots/milestone_5.png)

---

## Reflections

### What Broke
The threshold detection in Milestone 4, determining whether a trajectory passed within a set distance of the WDO base, was the most frustrating part of the project. The logic kept causing the program to break before it was working correctly, and getting the distance check to behave consistently across all threats required several attempts.

### What Surprised Me
How accessible spatial mapping is in Python once you get past the initial learning curve. The combination of Shapely, Folium, and pyproj makes it possible to go from raw coordinates to a fully interactive map with buffers, color-coded trajectories, and popups without a huge amount of code. That was genuinely unexpected.

### What Clicked
Python syntax. Coming into this project it felt like a barrier, but working through each milestone made it feel natural. By Milestone 4 and 5 the code was starting to read almost like plain English, which made debugging and building on previous work much easier.

---

## Dependencies

- Python 3.x
- Folium
- Shapely
- PyProj
- GeoPandas

---

## Notes

Interactive HTML maps are saved to the `outputs/` folder and can be opened in any browser. Screenshots of each map are embedded above for quick reference within the repository.
