import boreholeCreator.core.tool
import ifcopenshell
import math
O = 0., 0., 0.
X = 1., 0., 0.
Y = 0., 1., 0.
Z = 0., 0., 1.
MZ = 0.0, 0.0, -1.0
class Geometry(boreholeCreator.core.tool.Geometry):
    @classmethod
    def create_ifcextrudedareasolid(cls, ifcfile:ifcopenshell.file, surface, ifcaxis2placement, extrude_dir, extrusion):
        ifcdir = ifcfile.createIfcDirection(extrude_dir)
        ifcextrudedareasolid = ifcfile.createIfcExtrudedAreaSolid(surface, ifcaxis2placement, ifcdir, extrusion)
        return ifcextrudedareasolid

    def create_circle(cls,ifcfile, radius, name):
        return ifcfile.create_entity("IfcCircleProfileDef", ProfileType="AREA", ProfileName=name, Radius=radius)

    def create_rectangle(cls,ifcfile, x, y, name):
        return ifcfile.create_entity("IfcRectangleProfileDef", ProfileType="AREA", ProfileName=name, XDim=x, YDim=y)

    def create_triangle(cls,ifcfile, radius, name):
        c = 2 * radius * math.sqrt(3.0)
        coordinates = ((-0.5 * c, radius), (0.5 * c, radius), (0.0, -2 * radius))
        point_list = ifcfile.create_entity("IfcCartesianPointList2D", CoordList=coordinates)
        curve = ifcfile.create_entity("IfcIndexedPolyCurve", Points=point_list)
        return ifcfile.create_entity("IfcArbitraryClosedProfileDef", ProfileType="AREA", ProfileName=name,
                                     OuterCurve=curve)