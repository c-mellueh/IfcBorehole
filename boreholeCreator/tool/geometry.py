from typing import Type

import ifcopenshell

import boreholeCreator
import boreholeCreator.core.tool
from boreholeCreator import settings, tool
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
    def get_settings(cls) -> Type[settings.Geometry]:
        return settings.Geometry

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
        c = 2 * radius * 1.7320508076  # sqrt(3)
        coordinates = ((-0.5 * c, radius), (0.5 * c, radius), (0.0, -2 * radius))
        point_list = ifcfile.create_entity("IfcCartesianPointList2D", CoordList=coordinates)
        curve = ifcfile.create_entity("IfcIndexedPolyCurve", Points=point_list)
        return ifcfile.create_entity("IfcArbitraryClosedProfileDef", ProfileType="AREA", ProfileName=name,
                                     OuterCurve=curve)

    @classmethod
    def create_pyramid(cls, use_primitive: bool = True):
        radius = cls.get_radius()
        c = 2 * radius * 1.7320508076
        if use_primitive:
            return cls.create_rectangular_pyramid_shape("Pyramid", -2., c, c)
        else:
            ifcfile = cls.get_file()
            context = cls.get_context()

            height = 2.
            coord = ((0., 0., 0.), (-0.5 * c, radius, height), (0.5 * c, radius, height), (0.0, -2 * radius, height))
            point_list = ifcfile.create_entity("IFCCARTESIANPOINTLIST3D", CoordList=coord)

            face_indexes = ((3, 2, 4), (1, 3, 4), (1, 2, 3), (1, 4, 2))
            faces = [ifcfile.create_entity("IFCINDEXEDPOLYGONALFACE", CoordIndex=point_list) for point_list in
                     face_indexes]

            face_set = ifcfile.create_entity("IFCPOLYGONALFACESET", Coordinates=point_list, Closed=True, Faces=faces)
            shape = ifcfile.createIfcShapeRepresentation(context, "Body", "Tessellation", [face_set])
            representation = ifcfile.create_entity("IFCPRODUCTDEFINITIONSHAPE", Representations=[shape])
            return representation

    @classmethod
    def create_cylinder(cls, name, depth: float, use_primitive: bool = True):
        radius = cls.get_radius()

        if use_primitive:
            cls.create_cylinder_shape(f"Circle_{name}", radius, depth)
        else:
            # Create Cylinder by extruding Circle
            ifcfile = cls.get_file()
            circle = cls.create_circle(ifcfile, radius, f"Circle_{name}")
            return cls.create_extrusion_shape(circle, name, depth, )

    @classmethod
    def create_cuboid(cls, name, depth: float, use_primitive: bool = True):
        radius = cls.get_radius()
        c = 1.4142135624 * radius  # sqrt(2)*radius
        if use_primitive:
            return cls.create_cuboid_shape(f"Cuboid_{name}", depth, c, c)
        else:
            ifcfile = cls.get_file()
            reactangle = cls.create_rectangle(ifcfile, radius * 1.2, radius * 1.2, f"Cuboid_{name}")
            return cls.create_extrusion_shape(reactangle, name, depth)

    @classmethod
    def create_prism(cls, name, depth: float, ):
        ifcfile = cls.get_file()
        radius = cls.get_radius()
        triangle = cls.create_triangle(ifcfile, radius, f"Prism_{name}")
        return cls.create_extrusion_shape(triangle, name, depth)

    @classmethod
    def create_extrusion_shape(cls, profile, name: str, depth: float, ):
        direction = (0., 0., 1.) if depth <= 0. else (0., 0., -1.)
        context = cls.get_context()
        ifcfile = cls.get_file()
        extrusion_placement = tool.Location.create_ifcaxis2placement3D(ifcfile, [0.0, 0.0, 0.0], direction,
                                                                       (1.0, 0.0, 0.0))  # Axis down
        solid = cls.create_ifcextrudedareasolid(ifcfile, profile, extrusion_placement, Z, abs(depth))
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])
        product_shape = ifcfile.createIfcProductDefinitionShape(f"{name}", None, [body_representation])
        return product_shape

    @classmethod
    def create_cylinder_shape(cls, name: str, radius: float, height: float):
        context = cls.get_context()
        ifcfile = cls.get_file()
        direction = (0., 0., 1.) if height <= 0. else (0., 0., -1.)
        placement = tool.Location.create_ifcaxis2placement3D(ifcfile, dir1=direction)  # Axis down
        cylinder = ifcfile.createIfcRightCircularCylinder(placement, height, radius)
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "CSG", [cylinder])
        product_shape = ifcfile.createIfcProductDefinitionShape(f"{name}", None, [body_representation])
        return product_shape

    @classmethod
    def create_cuboid_shape(cls, name: str, height: float, width: float, length: float):
        height = -height
        context = cls.get_context()
        ifcfile = cls.get_file()
        direction = (0., 0., 1.) if height >= 0. else (0., 0., -1.)
        pos = (-width / 2, -length / 2, 0.) if height >= 0. else (-width / 2, length / 2, 0.)
        placement = tool.Location.create_ifcaxis2placement3D(ifcfile, pos, dir1=direction)  # Axis down
        box = ifcfile.createIfcBlock(placement, width, length, abs(height))
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "CSG", [box])
        return ifcfile.createIfcProductDefinitionShape(f"{name}", None, [body_representation])

    @classmethod
    def create_rectangular_pyramid_shape(cls, name: str, height: float, width: float, legth: float):
        direction = (0., 0., 1.) if height >= 0. else (0., 0., -1.)
        ifcfile = cls.get_file()
        context = cls.get_context()

        pos = (-width / 2, -legth / 2, 0.) if height >= 0. else (-width / 2, legth / 2, -height)
        placement = tool.Location.create_ifcaxis2placement3D(ifcfile, pos, dir1=direction)  # Axis down
        pyramid = ifcfile.createIfcRectangularPyramid(placement, width, legth, abs(height))
        body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "CSG", [pyramid])
        return ifcfile.createIfcProductDefinitionShape(f"{name}", None, [body_representation])
