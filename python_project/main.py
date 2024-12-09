import time
from rust_point_in_polygon import is_point_in_polygon

# GeoJSON Polygon: A simple triangle
polygon_geojson = '''
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[0, 0], [4, 0], [2, 4], [0, 0]]]
  }
}
'''

# GeoJSON Point: Inside the triangle
point_geojson_inside = '''
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [2, 2]
  }
}
'''

# GeoJSON Point: Outside the triangle
point_geojson_outside = '''
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [5, 5]
  }
}
'''

# Measure performance for the point inside
start_time_inside = time.time()
result_inside = is_point_in_polygon(polygon_geojson, point_geojson_inside)
end_time_inside = time.time()

# Measure performance for the point outside
start_time_outside = time.time()
result_outside = is_point_in_polygon(polygon_geojson, point_geojson_outside)
end_time_outside = time.time()

# Print results
print(f"Point is inside the polygon: {result_inside}")
print(f"Time taken for Rust module to check point inside: {end_time_inside - start_time_inside:.6f} seconds")

print(f"Point is outside the polygon: {result_outside}")
print(f"Time taken for Rust module to check point outside: {end_time_outside - start_time_outside:.6f} seconds")
