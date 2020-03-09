from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *
#--------------------------------------------------------------
from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication
from Autodesk.Revit.DB import ElementSet, ElementId
#--------------------------------------------------------------
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

def jit_GetName(e):
	return Element.Name.GetValue(e)
def jit_FromIntUnits(lengthValue ):
	return UnitUtils.ConvertFromInternalUnits(lengthValue,Document.GetUnits(doc).GetFormatOptions(UnitType.UT_Length).DisplayUnits)
def jit_toInternalUnits(lengthValue):
	return UnitUtils.ConvertToInternalUnits(lengthValue,Document.GetUnits(doc).GetFormatOptions(UnitType.UT_Length).DisplayUnits)

