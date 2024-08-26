import math

import ifcopenshell

import boreholeCreator
import boreholeCreator.core.tool
from boreholeCreator import tool
from boreholeCreator.module.geometry.prop import GeometryProperties

O = 0., 0., 0.
X = 1., 0., 0.
Y = 0., 1., 0.
Z = 0., 0., 1.
MZ = 0.0, 0.0, -1.0


class Geometry(boreholeCreator.core.tool.Geometry):
    @classmethod
    def get_properties(cls) -> GeometryProperties:
        return boreholeCreator.GeometryProperties

    @classmethod
    def get_file(cls) -> ifcopenshell.file:
        return tool.Ifc.get_ifcfile()

    @classmethod
    def get_context(cls) -> ifcopenshell.entity_instance:
        return tool.Ifc.get_geometric_representation_context()

    @classmethod
    def get_radius(cls) -> float:
        return cls.get_properties().radius

    @classmethod
    def create_ifcextrudedareasolid(cls, ifcfile: ifcopenshell.file, surface, ifcaxis2placement, extrude_dir,
                                    extrusion):
        ifcdir = ifcfile.createIfcDirection(extrude_dir)
        ifcextrudedareasolid = ifcfile.createIfcExtrudedAreaSolid(surface, ifcaxis2placement, ifcdir, extrusion)
        return ifcextrudedareasolid

    @classmethod
    def create_circle(cls, ifcfile, radius, name):
        return ifcfile.create_entity("IfcCircleProfileDef", ProfileType="AREA", ProfileName=name, Radius=radius)

    @classmethod
    def create_rectangle(cls, ifcfile, x, y, name):
        return ifcfile.create_entity("IfcRectangleProfileDef", ProfileType="AREA", ProfileName=name, XDim=x, YDim=y)

    @classmethod
    def create_triangle(cls, ifcfile, radius, name):
        c = 2 * radius * math.sqrt(3.0)
        coordinates = ((-0.5 * c, radius), (0.5 * c, radius), (0.0, -2 * radius))
        point_list = ifcfile.create_entity("IfcCartesianPointList2D", CoordList=coordinates)
        curve = ifcfile.create_entity("IfcIndexedPolyCurve", Points=point_list)
        return ifcfile.create_entity("IfcArbitraryClosedProfileDef", ProfileType="AREA", ProfileName=name,
                                     OuterCurve=curve)

    @classmethod
    def create_pyramid(cls):
        radius = cls.get_radius()
        ifcfile = cls.get_file()
        context = cls.get_context()
        c = 2 * radius * math.sqrt(3.0)
        height = 2.
        coord = ((0., 0., 0.), (-0.5 * c, radius, height), (0.5 * c, radius, height), (0.0, -2 * radius, height))
        point_list = ifcfile.create_entity("IFCCARTESIANPOINTLIST3D", CoordList=coord)

        face_indexes = ((3, 2, 4), (1, 3, 4), (1, 2, 3), (1, 4, 2))
        faces = [ifcfile.create_entity("IFCINDEXEDPOLYGONALFACE", CoordIndex=point_list) for point_list in face_indexes]

        face_set = ifcfile.create_entity("IFCPOLYGONALFACESET", Coordinates=point_list, Closed=True, Faces=faces)
        shape = ifcfile.createIfcShapeRepresentation(context, "Body", "Tessellation", [face_set])
        representation = ifcfile.create_entity("IFCPRODUCTDEFINITIONSHAPE", Representations=[shape])
        return representation

    @classmethod
    def create_cylinder(cls, name, depth: float):
        ifcfile = cls.get_file()
        radius = cls.get_radius()
        circle = cls.create_circle(ifcfile, radius, f"Circle_{name}")
        return cls.create_extrusion_shape(circle, name, depth, )

    @classmethod
    def create_cuboid(cls, name, depth: float):
        ifcfile = cls.get_file()
        radius = cls.get_radius()
        reactangle = cls.create_rectangle(ifcfile, radius * 1.2, radius * 1.2, f"Circle_{name}")
        return cls.create_extrusion_shape(reactangle, name, depth)

    @classmethod
    def create_prism(cls, name, depth: float, ):
        ifcfile = cls.get_file()
        radius = cls.get_radius()
        triangle = cls.create_triangle(ifcfile, radius, f"Circle_{name}")
        return cls.create_extrusion_shape(triangle, name, depth)

    @classmethod
    def create_extrusion_shape(cls, profile, name, depth: float, ):
        dir = (0., 0., 1.) if depth <= 0. else (0., 0., -1.)
        context = cls.get_context()
        ifcfile = cls.get_file()
        extrusion_placement = tool.Location.create_ifcaxis2placement(ifcfile, [0.0, 0.0, 0.0], dir,
                                                                     (1.0, 0.0, 0.0))  # Axis down
        solid = cls.create_ifcextrudedareasolid(ifcfile, profile, extrusion_placement, Z, abs(depth))
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])
        product_shape = ifcfile.createIfcProductDefinitionShape(f"{name}", None, [body_representation])
        return product_shape
