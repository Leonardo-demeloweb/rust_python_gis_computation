import geopandas as gpd
from shapely.geometry import Polygon, Point
import time

# Define the polygon as a simple triangle
polygon_coords = [(0, 0), (4, 0), (2, 4), (0, 0)]  # Closed ring
polygon = Polygon(polygon_coords)

# Define points (one inside and one outside the triangle)
point_inside = Point(2, 2)
point_outside = Point(5, 5)

# Create a GeoDataFrame for the polygon
polygon_gdf = gpd.GeoDataFrame({"geometry": [polygon]})

# Create a GeoDataFrame for the points
points_gdf = gpd.GeoDataFrame({"geometry": [point_inside, point_outside]})

# Measure performance of point-in-polygon operation
start_time = time.time()

# Perform point-in-polygon check
points_gdf["inside"] = points_gdf.geometry.apply(lambda point: polygon_gdf.contains(point).any())

end_time = time.time()

# Print results
print(points_gdf)
print(f"Time taken for GeoPandas point-in-polygon operation: {end_time - start_time:.6f} seconds")
