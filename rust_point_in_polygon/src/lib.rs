use geo::{Polygon, Contains, LineString, point};
use geojson::{GeoJson, Value};
use pyo3::prelude::*;

#[pyfunction]
fn is_point_in_polygon(polygon_geojson: &str, point_geojson: &str) -> PyResult<bool> {
    let polygon_geojson: GeoJson = polygon_geojson.parse().unwrap();
    let point_geojson: GeoJson = point_geojson.parse().unwrap();

    if let GeoJson::Feature(polygon_feature) = polygon_geojson {
        if let Some(geometry) = polygon_feature.geometry {
            if let Value::Polygon(polygon_coords) = geometry.value {
                // Convert outer ring (first set of coordinates) to LineString
                let outer_ring = polygon_coords[0]
                    .iter()
                    .map(|coord| (coord[0], coord[1]))
                    .collect::<Vec<(f64, f64)>>();

                let polygon = Polygon::new(LineString::from(outer_ring), vec![]);

                if let GeoJson::Feature(point_feature) = point_geojson {
                    if let Some(geometry) = point_feature.geometry {
                        if let Value::Point(point_coords) = geometry.value {
                            let point = point!(x: point_coords[0], y: point_coords[1]);
                            return Ok(polygon.contains(&point));
                        }
                    }
                }
            }
        }
    }

    Ok(false)
}

#[pymodule]
fn rust_point_in_polygon(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(is_point_in_polygon, m)?)?;
    Ok(())
}
