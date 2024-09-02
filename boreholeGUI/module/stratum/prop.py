import pandas as pd

from boreholeCreator.module.stratum import prop


class StratumProperties:
    widget = None
    dataframe: pd.DataFrame = None
    tooltips = {
        prop.IFC_TYPE:     "IFC-Klasse z.B. 'IfcBuildingElementProxy'",
        prop.HEIGHT: "Z-Ausdehnung der Schicht",
        prop.BOREHOLE_ID:  "Identifier der Säule notwendig um Matching mit Schicht zu erstellen",
        prop.Z:            "Starthöhe der Schicht in Bezug auf OK Säule",
        prop.TRANSPARENCY: "Transparenz: \n0 = Undurchsichtig \n1 = Durchsichtig "
    }
