from boreholeCreator.settings.appdata import AppdataSetting

GEOMETRY = "geometry"

class GeometryProperties:
    geometry_context = None

class GeometrySettings:
    radius = AppdataSetting(GEOMETRY, "radius", float, 1.0)
