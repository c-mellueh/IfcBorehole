import ifcopenshell
from boreholeCreator.settings.appdata import AppdataSetting


LOCATION = "location"
MAPCONVERSION = "map_conversion"
PROJECTED_CRS = "projected_crs"
class LocationProperties:
    site_position = [0.,0.,0.] #Global Site Positioning
    site_placement :ifcopenshell.entity_instance = None


class LocationSettings:
    mapconversion_is_activated = AppdataSetting(LOCATION, "mapconversion_is_activated", bool, "False")
    
    eastings = AppdataSetting(MAPCONVERSION, "Eastings", float, 0.0)
    northings = AppdataSetting(MAPCONVERSION, "Northings", float, 0.0)
    orthogonal_height = AppdataSetting(MAPCONVERSION, "OrthogonalHeight", float, 0.0)
    x_axis_abscissa = AppdataSetting(MAPCONVERSION, "XAxisAbscissa", float, None)
    x_axis_ordinate = AppdataSetting(MAPCONVERSION, "XAxisOrdinate", float, None)
    scale = AppdataSetting(MAPCONVERSION, "Scale", float, None)
    
    crs_name = AppdataSetting(PROJECTED_CRS, "Name", str, "EPSG:9933")
    crs_description = AppdataSetting(PROJECTED_CRS, "Description", str, "DB_REF2016 zone 3")
    geodetic_datum = AppdataSetting(PROJECTED_CRS, "GeodeticDatum", str, None)
    vertical_datum = AppdataSetting(PROJECTED_CRS, "VerticalDatum", str, None)
    map_projection = AppdataSetting(PROJECTED_CRS, "MapProjection", str, "Gaus-Krueger")
    map_zone = AppdataSetting(PROJECTED_CRS, "MapZone", str, "3")
