import ifcopenshell
class LocationProperties:
    site_position = [0.,0.,0.] #Global Site Positioning
    site_placement :ifcopenshell.entity_instance = None
    use_map_conversion = False
    projected_crs_data = {"Name":          'EPSG:9933',
                          "Description":   'DB_REF2016 zone 3',
                          "GeodeticDatum": None,
                          "VerticalDatum": None,
                          "MapProjection": "Gaus-Krueger",
                          "MapZone":       '3'
                          }
    map_conversion_data = {
        "Eastings":         0.,
        "Northings":        0.,
        "OrthogonalHeight": 0.,
        "XAxisAbscissa":    None,
        "XAxisOrdinate": None,
        "Scale":            None
    }
