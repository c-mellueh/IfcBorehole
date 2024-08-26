from __future__ import annotations
from typing import TYPE_CHECKING
import boreholeCreator.core.tool
import boreholeCreator
import time
import ifcopenshell
import tempfile
if TYPE_CHECKING:
    from boreholeCreator.module.ifc.prop import IfcProperties


class Ifc(boreholeCreator.core.tool.Ifc):
    @classmethod
    def get_properties(cls) -> IfcProperties:
        return boreholeCreator.IfcProperties

    @classmethod
    def create_base_ifc(cls):
        template = cls.create_template()
        temp_handle, temp_filename = tempfile.mkstemp(suffix=".ifc")
        with open(temp_filename, "w") as f:
            f.write(template)
        return ifcopenshell.open(temp_filename)

    @classmethod
    def create_template(cls,filename, creator, organization, application, application_version, project_globalid,
                        project_name, center):
        timestamp = int(time.time())
        timestring = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(timestamp))
        template = f"""ISO-10303-21;
        HEADER;
        FILE_DESCRIPTION(('ViewDefinition[CoordinationView]'),'2;1');
        FILE_NAME('{filename}','{timestring}',('{creator}'),('{organization}'),'{application}','{application}','');
        FILE_SCHEMA(('IFC4X3_ADD2'));
        ENDSEC;
        DATA;
        #1=IFCPERSON($,$,'{creator}',$,$,$,$,$);
        #2=IFCORGANIZATION($,'{organization}',$,$,$);
        #3=IFCPERSONANDORGANIZATION(#1,#2,$);
        #4=IFCAPPLICATION(#2,'{application_version}','{application}','');
        #5=IFCOWNERHISTORY(#3,#4,$,.ADDED.,{timestamp},#3,#4,{timestamp});
        #6=IFCDIRECTION((1.,0.,0.));
        #7=IFCDIRECTION((0.,0.,1.));
        #8=IFCCARTESIANPOINT((0.,0.,0.));
        #9=IFCAXIS2PLACEMENT3D(#8,#7,#6);
        #10=IFCDIRECTION((0.,1.,0.));
        #11=IFCGEOMETRICREPRESENTATIONCONTEXT($,'Model',3,1.E-05,#9,$);
        #12=IFCDIMENSIONALEXPONENTS(0,0,0,0,0,0,0);
        #13=IFCSIUNIT(*,.LENGTHUNIT.,$,.METRE.);
        #14=IFCSIUNIT(*,.AREAUNIT.,$,.SQUARE_METRE.);
        #15=IFCSIUNIT(*,.VOLUMEUNIT.,$,.CUBIC_METRE.);
        #16=IFCSIUNIT(*,.PLANEANGLEUNIT.,$,.RADIAN.);
        #17=IFCMEASUREWITHUNIT(IFCPLANEANGLEMEASURE(1.74532925199433E-2), #16);
        #18=IFCCONVERSIONBASEDUNIT(#12,.PLANEANGLEUNIT.,'DEGREE',#17);
        #19=IFCUNITASSIGNMENT((#13,#14,#15,#18));
        #20=IFCPROJECT('{project_globalid}',#5,'{project_name}',$,$,$,$,(#11),#19);
        #21=IFCPROJECTEDCRS('EPSG:9933','DB_REF2016 zone 3',$,$,'Gaus-Krueger','3',#13);
        #22=IFCMAPCONVERSION(#11,#21,{float(center[0])},{float(center[1])},{float(center[2])},$,$,$);
        ENDSEC;
        END-ISO-10303-21;
        """
        return template