import numpy as np
import pandas as pd

np.random.seed(42)

# 20 sites
sites = pd.DataFrame({
    "site_id": range(1, 21),
    "lat": 52.52 + 0.05 * np.random.randn(20),
    "lon": 13.40 + 0.05 * np.random.randn(20)
})

# 3 sectors per site
sectors = []
for _, r in sites.iterrows():
    for i, az in enumerate([0, 120, 240]):
        sectors.append({
            "site_id": r.site_id,
            "sector_id": f"{r.site_id}_{i+1}",
            "azimuth": az,
            "beamwidth": 120
        })

sectors = pd.DataFrame(sectors)

# Random user points
points = pd.DataFrame({
    "point_id": range(1, 101),
    "lat": 52.52 + 0.08 * np.random.randn(100),
    "lon": 13.40 + 0.08 * np.random.randn(100)
})


from pyproj import Transformer

transformer = Transformer.from_crs("EPSG:4326", "EPSG:32633", always_xy=True)

def project(df):
    xs, ys = transformer.transform(df["lon"].values, df["lat"].values)
    df["x"] = xs
    df["y"] = ys
    return df

sites = project(sites)
points = project(points)

from scipy.spatial import KDTree

site_tree = KDTree(sites[["x","y"]].values)

dist, site_idx = site_tree.query(points[["x","y"]].values)
points["site_id"] = sites.iloc[site_idx]["site_id"].values


import math

def bearing(lat1, lon1, lat2, lon2):
    dlon = math.radians(lon2 - lon1)
    lat1, lat2 = map(math.radians, [lat1, lat2])

    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(dlon)

    return (math.degrees(math.atan2(x, y)) + 360) % 360

def in_sector(point_bearing, azimuth, beamwidth):
    start = (azimuth - beamwidth/2) % 360
    end = (azimuth + beamwidth/2) % 360

    if start < end:
        return start <= point_bearing <= end
    else:
        return point_bearing >= start or point_bearing <= end

assigned_sectors = []

for _, p in points.iterrows():
    site = sites[sites.site_id == p.site_id].iloc[0]
    site_sectors = sectors[sectors.site_id == p.site_id]

    brg = bearing(site.lat, site.lon, p.lat, p.lon)

    candidates = []
    for _, s in site_sectors.iterrows():
        if in_sector(brg, s.azimuth, s.beamwidth):
            diff = abs((brg - s.azimuth + 180) % 360 - 180)
            candidates.append((diff, s.sector_id))

    if candidates:
        best = min(candidates, key=lambda x: x[0])[1]
    else:
        best = None

    assigned_sectors.append(best)

points["serving_sector"] = assigned_sectors


print(points[["point_id","site_id","serving_sector"]])

points.to_csv("data.csv")

import matplotlib.pyplot as plt
import math

plt.figure(figsize=(10,10))

# --------------------
# Plot sites
# --------------------
plt.scatter(
    sites.x, sites.y,
    c="red", marker="^", s=180, label="Sites", zorder=3
)

# Label site IDs
for _, s in sites.iterrows():
    plt.text(
        s.x, s.y + 20,
        f"S{s.site_id}",
        fontsize=9, ha="center", color="red", weight="bold"
    )

# --------------------
# Plot points
# --------------------
plt.scatter(
    points.x, points.y,
    c="blue", s=50, label="Points", alpha=0.8, zorder=2
)

# Label point IDs
for _, p in points.iterrows():
    plt.text(
        p.x, p.y + 10,
        str(p.point_id),
        fontsize=7, color="blue", ha="center"
    )

# --------------------
# Plot sector azimuth lines + sector labels
# --------------------
for _, s in sectors.merge(sites, on="site_id").iterrows():
    length = 500
    az = math.radians(s.azimuth)

    dx = length * math.sin(az)
    dy = length * math.cos(az)

    # Azimuth line
    plt.plot(
        [s.x, s.x + dx],
        [s.y, s.y + dy],
        "k--", alpha=0.5, zorder=1
    )

    # Sector label slightly away from site
    label_x = s.x + 0.6 * dx
    label_y = s.y + 0.6 * dy

    plt.text(
        label_x, label_y,
        s.sector_id,
        fontsize=8, color="black",
        ha="center", va="center",
        bbox=dict(facecolor="white", alpha=0.6, edgecolor="none")
    )

# --------------------
# Final touches
# --------------------
plt.legend()
plt.title("Serving Sector Assignment (Points + Sector Labels)")
plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")
plt.grid(alpha=0.3)
plt.axis("equal")

plt.show()


SITE_TO_PLOT = 6   # change this
RADIUS_METERS = 1200
site = sites[sites.site_id == SITE_TO_PLOT].iloc[0]

points_sub = points[
    ((points.x - site.x)**2 + (points.y - site.y)**2) ** 0.5 < RADIUS_METERS
]
import matplotlib.pyplot as plt
import math

plt.figure(figsize=(8,8))

# --------------------
# Plot selected site
# --------------------
plt.scatter(site.x, site.y, c="red", marker="^", s=220, zorder=3)
plt.text(site.x, site.y + 20, f"Site {site.site_id}", ha="center",
         fontsize=10, weight="bold", color="red")

# --------------------
# Plot points near site
# --------------------
plt.scatter(points_sub.x, points_sub.y, c="blue", s=60, zorder=2)

for _, p in points_sub.iterrows():
    label = f"{p.point_id}\n({p.serving_sector})"
    plt.text(p.x, p.y + 10, label, fontsize=8, ha="center", color="blue")

# --------------------
# Plot sectors of that site
# --------------------
site_sectors = sectors[sectors.site_id == SITE_TO_PLOT]

for _, s in site_sectors.iterrows():
    length = 700
    az = math.radians(s.azimuth)

    dx = length * math.sin(az)
    dy = length * math.cos(az)

    # Azimuth line
    plt.plot(
        [site.x, site.x + dx],
        [site.y, site.y + dy],
        "k--", linewidth=2
    )

    # Sector label
    plt.text(
        site.x + 0.6*dx,
        site.y + 0.6*dy,
        s.sector_id,
        fontsize=9,
        bbox=dict(facecolor="white", alpha=0.7, edgecolor="none")
    )

# --------------------
# Styling
# --------------------
plt.title(f"Site {SITE_TO_PLOT} – Sector Assignment Validation")
plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")
plt.axis("equal")
plt.grid(alpha=0.3)

plt.show()
