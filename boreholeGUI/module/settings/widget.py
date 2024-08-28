# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QDoubleSpinBox,
                               QFormLayout, QFrame, QLabel, QLineEdit,
                               QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1001, 486)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout = QFormLayout(self.tab)
        self.formLayout.setObjectName(u"formLayout")
        self.la_application_name = QLabel(self.tab)
        self.la_application_name.setObjectName(u"la_application_name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.la_application_name)

        self.le_application_name = QLineEdit(self.tab)
        self.le_application_name.setObjectName(u"le_application_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_application_name)

        self.la_application_version = QLabel(self.tab)
        self.la_application_version.setObjectName(u"la_application_version")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.la_application_version)

        self.le_application_version = QLineEdit(self.tab)
        self.le_application_version.setObjectName(u"le_application_version")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_application_version)

        self.line_1 = QFrame(self.tab)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShape(QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.line_1)

        self.la_author = QLabel(self.tab)
        self.la_author.setObjectName(u"la_author")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.la_author)

        self.la_family_name = QLabel(self.tab)
        self.la_family_name.setObjectName(u"la_family_name")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.la_family_name)

        self.le_author_family_name = QLineEdit(self.tab)
        self.le_author_family_name.setObjectName(u"le_author_family_name")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_author_family_name)

        self.la_given_name = QLabel(self.tab)
        self.la_given_name.setObjectName(u"la_given_name")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.la_given_name)

        self.le_author_given_name = QLineEdit(self.tab)
        self.le_author_given_name.setObjectName(u"le_author_given_name")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_author_given_name)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.line_2)

        self.la_company = QLabel(self.tab)
        self.la_company.setObjectName(u"la_company")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.la_company)

        self.la_company_name = QLabel(self.tab)
        self.la_company_name.setObjectName(u"la_company_name")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.la_company_name)

        self.le_company_name = QLineEdit(self.tab)
        self.le_company_name.setObjectName(u"le_company_name")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.le_company_name)

        self.la_company_description = QLabel(self.tab)
        self.la_company_description.setObjectName(u"la_company_description")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.la_company_description)

        self.le_company_description = QLineEdit(self.tab)
        self.le_company_description.setObjectName(u"le_company_description")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.le_company_description)

        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.line_3)

        self.la_fileschema = QLabel(self.tab)
        self.la_fileschema.setObjectName(u"la_fileschema")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.la_fileschema)

        self.cb_file_schema = QComboBox(self.tab)
        self.cb_file_schema.addItem("")
        self.cb_file_schema.addItem("")
        self.cb_file_schema.addItem("")
        self.cb_file_schema.setObjectName(u"cb_file_schema")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.cb_file_schema)

        self.la_default_pset_name = QLabel(self.tab)
        self.la_default_pset_name.setObjectName(u"la_default_pset_name")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.la_default_pset_name)

        self.le_default_pset_name = QLineEdit(self.tab)
        self.le_default_pset_name.setObjectName(u"le_default_pset_name")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.le_default_pset_name)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_3)

        self.sb_radius = QDoubleSpinBox(self.tab)
        self.sb_radius.setObjectName(u"sb_radius")
        self.sb_radius.setMaximum(15.000000000000000)
        self.sb_radius.setSingleStep(0.250000000000000)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.sb_radius)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.formLayout_3 = QFormLayout(self.tab_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cb_mapconversion = QCheckBox(self.tab_3)
        self.cb_mapconversion.setObjectName(u"cb_mapconversion")
        self.cb_mapconversion.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.cb_mapconversion)

        self.wi_map_conversion = QWidget(self.tab_3)
        self.wi_map_conversion.setObjectName(u"wi_map_conversion")
        self.formLayout_4 = QFormLayout(self.wi_map_conversion)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.le_map_conv = QLabel(self.wi_map_conversion)
        self.le_map_conv.setObjectName(u"le_map_conv")

        self.formLayout_4.setWidget(0, QFormLayout.SpanningRole, self.le_map_conv)

        self.le_map_conv_easting = QLabel(self.wi_map_conversion)
        self.le_map_conv_easting.setObjectName(u"le_map_conv_easting")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.le_map_conv_easting)

        self.le_eastings = QLineEdit(self.wi_map_conversion)
        self.le_eastings.setObjectName(u"le_eastings")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.le_eastings)

        self.le_map_conv_northing = QLabel(self.wi_map_conversion)
        self.le_map_conv_northing.setObjectName(u"le_map_conv_northing")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.le_map_conv_northing)

        self.le_northings = QLineEdit(self.wi_map_conversion)
        self.le_northings.setObjectName(u"le_northings")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.le_northings)

        self.le_map_conv_orth_height = QLabel(self.wi_map_conversion)
        self.le_map_conv_orth_height.setObjectName(u"le_map_conv_orth_height")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.le_map_conv_orth_height)

        self.le_orthogonal_height = QLineEdit(self.wi_map_conversion)
        self.le_orthogonal_height.setObjectName(u"le_orthogonal_height")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.le_orthogonal_height)

        self.le_map_conv_xaxis_absc = QLabel(self.wi_map_conversion)
        self.le_map_conv_xaxis_absc.setObjectName(u"le_map_conv_xaxis_absc")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.le_map_conv_xaxis_absc)

        self.le_x_axis_abscissa = QLineEdit(self.wi_map_conversion)
        self.le_x_axis_abscissa.setObjectName(u"le_x_axis_abscissa")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.le_x_axis_abscissa)

        self.le_map_conv_xaxis_ord = QLabel(self.wi_map_conversion)
        self.le_map_conv_xaxis_ord.setObjectName(u"le_map_conv_xaxis_ord")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.le_map_conv_xaxis_ord)

        self.le_x_axis_ordinate = QLineEdit(self.wi_map_conversion)
        self.le_x_axis_ordinate.setObjectName(u"le_x_axis_ordinate")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.le_x_axis_ordinate)

        self.le_map_conv_scale = QLabel(self.wi_map_conversion)
        self.le_map_conv_scale.setObjectName(u"le_map_conv_scale")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.le_map_conv_scale)

        self.le_scale = QLineEdit(self.wi_map_conversion)
        self.le_scale.setObjectName(u"le_scale")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.le_scale)

        self.la_crs = QLabel(self.wi_map_conversion)
        self.la_crs.setObjectName(u"la_crs")

        self.formLayout_4.setWidget(8, QFormLayout.SpanningRole, self.la_crs)

        self.la_crs_name = QLabel(self.wi_map_conversion)
        self.la_crs_name.setObjectName(u"la_crs_name")

        self.formLayout_4.setWidget(9, QFormLayout.LabelRole, self.la_crs_name)

        self.le_crs_name = QLineEdit(self.wi_map_conversion)
        self.le_crs_name.setObjectName(u"le_crs_name")

        self.formLayout_4.setWidget(9, QFormLayout.FieldRole, self.le_crs_name)

        self.la_crs_description = QLabel(self.wi_map_conversion)
        self.la_crs_description.setObjectName(u"la_crs_description")

        self.formLayout_4.setWidget(10, QFormLayout.LabelRole, self.la_crs_description)

        self.le_crs_description = QLineEdit(self.wi_map_conversion)
        self.le_crs_description.setObjectName(u"le_crs_description")

        self.formLayout_4.setWidget(10, QFormLayout.FieldRole, self.le_crs_description)

        self.la_geodetic_datum = QLabel(self.wi_map_conversion)
        self.la_geodetic_datum.setObjectName(u"la_geodetic_datum")

        self.formLayout_4.setWidget(11, QFormLayout.LabelRole, self.la_geodetic_datum)

        self.le_geodetic_datum = QLineEdit(self.wi_map_conversion)
        self.le_geodetic_datum.setObjectName(u"le_geodetic_datum")

        self.formLayout_4.setWidget(11, QFormLayout.FieldRole, self.le_geodetic_datum)

        self.la_vertical_datum = QLabel(self.wi_map_conversion)
        self.la_vertical_datum.setObjectName(u"la_vertical_datum")

        self.formLayout_4.setWidget(12, QFormLayout.LabelRole, self.la_vertical_datum)

        self.le_vertical_datum = QLineEdit(self.wi_map_conversion)
        self.le_vertical_datum.setObjectName(u"le_vertical_datum")

        self.formLayout_4.setWidget(12, QFormLayout.FieldRole, self.le_vertical_datum)

        self.la_map_projection = QLabel(self.wi_map_conversion)
        self.la_map_projection.setObjectName(u"la_map_projection")

        self.formLayout_4.setWidget(13, QFormLayout.LabelRole, self.la_map_projection)

        self.le_map_projection = QLineEdit(self.wi_map_conversion)
        self.le_map_projection.setObjectName(u"le_map_projection")

        self.formLayout_4.setWidget(13, QFormLayout.FieldRole, self.le_map_projection)

        self.le_crs_map_zone = QLabel(self.wi_map_conversion)
        self.le_crs_map_zone.setObjectName(u"le_crs_map_zone")

        self.formLayout_4.setWidget(14, QFormLayout.LabelRole, self.le_crs_map_zone)

        self.le_mapzone = QLineEdit(self.wi_map_conversion)
        self.le_mapzone.setObjectName(u"le_mapzone")

        self.formLayout_4.setWidget(14, QFormLayout.FieldRole, self.le_mapzone)

        self.line = QFrame(self.wi_map_conversion)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout_4.setWidget(7, QFormLayout.SpanningRole, self.line)


        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.wi_map_conversion)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.la_application_name.setText(QCoreApplication.translate("Form", u"Application Name", None))
        self.la_application_version.setText(QCoreApplication.translate("Form", u"Application Version", None))
        self.la_author.setText(QCoreApplication.translate("Form", u"Author", None))
        self.la_family_name.setText(QCoreApplication.translate("Form", u"FamilyName", None))
        self.la_given_name.setText(QCoreApplication.translate("Form", u"GivenName", None))
        self.la_company.setText(QCoreApplication.translate("Form", u"Company", None))
        self.la_company_name.setText(QCoreApplication.translate("Form", u"Name", None))
        self.la_company_description.setText(QCoreApplication.translate("Form", u"Description", None))
        self.la_fileschema.setText(QCoreApplication.translate("Form", u"FileSchema", None))
        self.cb_file_schema.setItemText(0, QCoreApplication.translate("Form", u"IFC2X3", None))
        self.cb_file_schema.setItemText(1, QCoreApplication.translate("Form", u"IFC4", None))
        self.cb_file_schema.setItemText(2, QCoreApplication.translate("Form", u"IFC4X3_ADD2", None))

        self.cb_file_schema.setCurrentText(QCoreApplication.translate("Form", u"IFC2X3", None))
        self.la_default_pset_name.setText(QCoreApplication.translate("Form", u"Default Pset Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"BoreHole Radius", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("Form", u"General", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Activate IfcMapConversion", None))
        self.cb_mapconversion.setText("")
        self.le_map_conv.setText(QCoreApplication.translate("Form", u"IfcMapConversion", None))
        self.le_map_conv_easting.setText(QCoreApplication.translate("Form", u"Eastings", None))
        self.le_map_conv_northing.setText(QCoreApplication.translate("Form", u"Nortings", None))
        self.le_map_conv_orth_height.setText(QCoreApplication.translate("Form", u"OrthogonalHeight", None))
        self.le_map_conv_xaxis_absc.setText(QCoreApplication.translate("Form", u"XAxisAbscissa", None))
        self.le_map_conv_xaxis_ord.setText(QCoreApplication.translate("Form", u"XAxisOrdinate", None))
        self.le_map_conv_scale.setText(QCoreApplication.translate("Form", u"Scale", None))
        self.la_crs.setText(QCoreApplication.translate("Form", u"IfcProjectedCRS", None))
        self.la_crs_name.setText(QCoreApplication.translate("Form", u"Name", None))
        self.la_crs_description.setText(QCoreApplication.translate("Form", u"Description", None))
        self.la_geodetic_datum.setText(QCoreApplication.translate("Form", u"GeodeticDatum", None))
        self.la_vertical_datum.setText(QCoreApplication.translate("Form", u"VerticalDatum", None))
        self.la_map_projection.setText(QCoreApplication.translate("Form", u"MapProjection", None))
        self.le_crs_map_zone.setText(QCoreApplication.translate("Form", u"MapZone", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QCoreApplication.translate("Form", u"Location", None))
    # retranslateUi

