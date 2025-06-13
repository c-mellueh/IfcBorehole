from __future__ import annotations

import logging
import tempfile
import time
import uuid
from typing import Any, TYPE_CHECKING

import ifcopenshell
import ifcopenshell.api
import ifcopenshell.guid
import pandas as pd

import boreholeCreator
import boreholeCreator.core.tool
from boreholeCreator import tool

if TYPE_CHECKING:
    from boreholeCreator.module.ifc.prop import IfcProperties,IfcSettings

from boreholeCreator.module.ifc.prop import AUTHOR,ORGANIZATION
from boreholeCreator.settings.appdata import Appdata as appdata_tool

class Ifc(boreholeCreator.core.tool.Ifc):
    @classmethod
    def get_properties(cls) -> IfcProperties:
        return boreholeCreator.IfcProperties

    @classmethod
    def get_settings(cls) -> IfcSettings:
        return boreholeCreator.IfcSettings

    @classmethod
    def create_guid(cls):
        return ifcopenshell.guid.compress(uuid.uuid1().hex)

    @classmethod
    def reset(cls):
        prop = cls.get_properties()
        prop.ifcfile = None
        prop.owner_history = None
        prop.ifcfile = None
        prop.project = None
        prop.geometric_representation_context = None
        prop.site = None
        prop.ifc_person = None
        prop.ifc_organization = None

    @classmethod
    def get_ifcfile(cls) -> ifcopenshell.file:
        if cls.get_properties().ifcfile is None:
            cls.get_properties().ifcfile = cls.create_base_ifc()
        return cls.get_properties().ifcfile

    @classmethod
    def create_base_ifc(cls):
        template = cls.create_template()
        temp_handle, temp_filename = tempfile.mkstemp(suffix=".ifc")
        with open(temp_filename, "w") as f:
            f.write(template)
        ifcfile = ifcopenshell.open(temp_filename)
        return ifcfile

    @classmethod
    def fill_person_and_org(cls):
        creator_dict = appdata_tool.section_to_dict(AUTHOR)
        organization_dict =appdata_tool.section_to_dict(ORGANIZATION)

        tool.Util.fill_entity_with_dict(cls.get_person(), creator_dict)
        tool.Util.fill_entity_with_dict(cls.get_organization(), organization_dict)

    @classmethod
    def get_person(cls):
        return cls._get_ifc_entity("IfcPerson", "ifc_person")

    @classmethod
    def get_organization(cls):
        return cls._get_ifc_entity("IfcOrganization", "ifc_organization")

    @classmethod
    def create_template(cls):
        ifc_settings = cls.get_settings()
        filename = ifc_settings.file_name
        creator_name = ifc_settings.author_family_name
        organization_name = ifc_settings.organization_name
        timestamp = int(time.time())
        timestring = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(timestamp))
        template = f"""ISO-10303-21;
        HEADER;
        FILE_DESCRIPTION(('ViewDefinition[CoordinationView]'),'2;1');
        FILE_NAME('{filename}','{timestring}',('{creator_name}'),('{organization_name}'),'{ifc_settings.application_name}','{ifc_settings.application_name}','');
        FILE_SCHEMA(('{ifc_settings.file_schema}'));
        ENDSEC;
        DATA;
        #1=IFCPERSON($,$,$,$,$,$,$,$);
        #2=IFCORGANIZATION($,'{organization_name}',$,$,$);
        #3=IFCPERSONANDORGANIZATION(#1,#2,$);
        #4=IFCAPPLICATION(#2,'{ifc_settings.application_version}','{ifc_settings.application_name}','');
        #5=IFCOWNERHISTORY(#3,#4,$,.ADDED.,{timestamp},#3,#4,{timestamp});
        #6=IFCDIRECTION((1.,0.,0.));
        #7=IFCDIRECTION((0.,0.,1.));
        #8=IFCCARTESIANPOINT((0.,0.,0.));
        #9=IFCAXIS2PLACEMENT3D(#8,#7,#6);
        #10=IFCGEOMETRICREPRESENTATIONCONTEXT($,'Model',3,1.E-05,#9,$);
        #11=IFCGEOMETRICREPRESENTATIONSUBCONTEXT('Body','Model',*,*,*,*,#10,$,.MODEL_VIEW.,$);
        #12=IFCDIMENSIONALEXPONENTS(0,0,0,0,0,0,0);
        #13=IFCSIUNIT(*,.LENGTHUNIT.,$,.METRE.);
        #14=IFCSIUNIT(*,.AREAUNIT.,$,.SQUARE_METRE.);
        #15=IFCSIUNIT(*,.VOLUMEUNIT.,$,.CUBIC_METRE.);
        #16=IFCSIUNIT(*,.PLANEANGLEUNIT.,$,.RADIAN.);
        #17=IFCMEASUREWITHUNIT(IFCPLANEANGLEMEASURE(1.74532925199433E-2), #16);
        #18=IFCCONVERSIONBASEDUNIT(#12,.PLANEANGLEUNIT.,'DEGREE',#17);
        #19=IFCUNITASSIGNMENT((#13,#14,#15,#18));
        #20=IFCPROJECT('{ifc_settings.project_gobal_id}',#5,'{ifc_settings.project_name}',$,$,$,$,(#10),#19);
        ENDSEC;
        END-ISO-10303-21;
        """
        return template

    @classmethod
    def get_site(cls) -> ifcopenshell.entity_instance:
        return cls.get_properties().site

    @classmethod
    def create_ifc_site(cls,site_placement:ifcopenshell.entity_instance):
        ifcfile = cls.get_ifcfile()
        owner_history = cls.get_owner_history()
        project = cls.get_project()
        site = ifcfile.createIfcSite(cls.create_guid(), owner_history, "Site", None, None, site_placement, None, None,
                                     "ELEMENT", None, None, None, None, None)

        ifcfile.createIfcRelAggregates(cls.create_guid(), owner_history, "Project Container", None, project,
                                       [site])
        cls.get_properties().site = site
        return site


    @classmethod
    def _get_ifc_entity(cls,ifc_name,prop_name):
        ifcfile = cls.get_ifcfile()
        if getattr(cls.get_properties(),prop_name) is None:
            p = ifcfile.by_type(ifc_name)
            if p:
                setattr(cls.get_properties(),prop_name,p[0])
        return getattr(cls.get_properties(),prop_name)

    @classmethod
    def get_owner_history(cls) -> ifcopenshell.entity_instance | None:
        return cls._get_ifc_entity("IfcOwnerHistory","owner_history")

    @classmethod
    def get_project(cls):
        return cls._get_ifc_entity("IfcProject","project")

    @classmethod
    def get_geometric_representation_context(cls):
        return cls._get_ifc_entity("IFCGEOMETRICREPRESENTATIONSUBCONTEXT","geometric_representation_context")

    @classmethod
    def create_pset_dict(cls, row: pd.Series, ignored_collumns) -> dict[str, dict[str, Any]]:
        pset_dict = dict()
        pset_base_name = cls.get_settings().pset_base_name
        for attribute_name, value in row.items():
            if attribute_name in ignored_collumns:
                continue
            if pd.isna(value):
                value = None
            name = str(attribute_name).split(":")
            if len(name) < 2:
                name = [pset_base_name, attribute_name]
            elif len(name) > 2:
                logging.warning(
                    f"Attributename '{attribute_name}' contains too much ':'  to be splitted correctly -> take first 2 values")
                name = name[:2]
            if pset_dict.get(name[0]) is None:
                pset_dict[name[0]] = dict()
            pset_dict[name[0]][name[1]] = value
        return pset_dict

    @classmethod
    def add_attributes(cls, entity: ifcopenshell.entity_instance, data: dict[str, dict[str, Any]]):
        ifcfile = cls.get_ifcfile()
        owner_history = cls.get_owner_history()
        for pset_name, attribute_dict in data.items():
            pset = ifcopenshell.api.run("pset.add_pset", ifcfile, product=entity, name=pset_name)
            relation = pset.DefinesOccurrence[0]
            # relation.OwnerHistory = owner_history
            # pset.OwnerHistory = owner_history
            ifcopenshell.api.run("pset.edit_pset", ifcfile, pset=pset, properties=attribute_dict)

    @classmethod
    def create_borehole(cls, row: pd.Series, borehole_placement, shape):
        from boreholeCreator.module.borehole import prop
        ifcfile = cls.get_ifcfile()

        ifcborehole = ifcfile.create_entity(row[prop.IFC_TYPE],
                                            GlobalId=cls.create_guid(),
                                            OwnerHistory=cls.get_owner_history(),
                                            Name=row[prop.NAME],
                                            Description="Auto Generated",
                                            ObjectPlacement=borehole_placement,
                                            Tag=row[prop.ID],
                                            Representation=shape)

        optional_column_names = tool.Borehole.get_optional_column_names()
        required_column_names = tool.Borehole.get_required_column_names()
        data = cls.create_pset_dict(row, required_column_names + optional_column_names)
        cls.add_attributes(ifcborehole, data)
        return ifcborehole

    @classmethod
    def create_stratum(cls, shape, row: pd.Series, borehole_placement):
        from boreholeCreator.module.stratum import prop
        name = row[prop.NAME]
        local_pos = 0.0, 0., row[prop.Z]
        ifcfile = cls.get_ifcfile()
        owner_history = cls.get_owner_history()
        placement = tool.Location.create_ifclocalplacement(ifcfile, local_pos, relative_to=borehole_placement)
        stratum = ifcfile.create_entity(row[prop.IFC_TYPE],
                                        GlobalId=cls.create_guid(),
                                        OwnerHistory=owner_history,
                                        Name=str(name),
                                        Description="Auto Generated",
                                        ObjectPlacement=placement,
                                        Representation=shape,
                                        Tag=row[prop.ID], )
        #stratum.OwnerHistory = owner_history
        required_column_names = tool.Stratum.get_required_column_names()
        optional_column_names = tool.Stratum.get_optional_column_names()
        pset_dict = cls.create_pset_dict(row, required_column_names + optional_column_names)
        cls.add_attributes(stratum, pset_dict)
        return stratum

    @classmethod
    def assign_stratums_to_borehole(cls, borehole, stratums_list):
        ifcfile = cls.get_ifcfile()
        ifcopenshell.api.run("aggregate.assign_object", ifcfile, products=stratums_list, relating_object=borehole)

    @classmethod
    def assign_entities_to_site(cls, entities: list[ifcopenshell.entity_instance]):
        ifcfile = cls.get_ifcfile()
        site = cls.get_site()
        container = ifcfile.create_entity("IFCRELCONTAINEDINSPATIALSTRUCTURE",GlobalId=cls.create_guid(),OwnerHistory=cls.get_owner_history())
        container.RelatedElements = entities
        container.RelatingStructure = site
        # ifcopenshell.api.run("spatial.assign_container", ifcfile, products=entities, relating_structure=site)
