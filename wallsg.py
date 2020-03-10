from Autodesk.Revit.DB import Document,Element,FilteredElementCollector
from Autodesk.Revit.DB import UnitUtils,Parameter,BuiltInParameter,BuiltInCategory,UnitType
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *
#--------------------------------------------------------------
from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication
from Autodesk.Revit.DB import ElementSet, ElementId
#--------------------------------------------------------------
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
def jt_GetName(e):
	return Element.Name.GetValue(e)
def jt_FromIntUnits(lengthValue ):
	return UnitUtils.ConvertFromInternalUnits(lengthValue,Document.GetUnits(doc).GetFormatOptions(UnitType.UT_Length).DisplayUnits)
def jt_toInternalUnits(lengthValue):
	return UnitUtils.ConvertToInternalUnits(lengthValue,Document.GetUnits(doc).GetFormatOptions(UnitType.UT_Length).DisplayUnits)
#--------------------------------------------------------------
def get_all_wall_curves():
    wfec = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()
    walls = wfec.ToElements()
    swfec = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StackedWalls).WhereElementIsNotElementType()
    swalls = swfec.ToElements()
    wtd = jt_getWallTypesDictionary()
    stacked = []
    walltypes = []
    print ' -- Stacked--' , len(swalls)
    for w in swfec:
        if jt_GetName(w.WallType) not in stacked:
            stacked.append(jt_GetName(w.WallType))
    print stacked
    print ' -- Other--' , len(walls)
    for w in walls:
        if jt_GetName(w.WallType) not in walltypes:
            walltypes.append(jt_GetName(w.WallType))
    print walltypes
    for x in swalls:
        jt_getWallCurve(x)
#--------------------------------------------------------------
def jt_getWallCurve(wall):
    if wall.Location.Curve.ToString().endswith('Line'):
        print 'easy'
    else:
        print 'not so easy ' , wall.Location.Curve.ToString()
#--------------------------------------------------------------
def jt_getWallTypesDictionary():
    wfec = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType()
    wtd =  {}
    wtypes = wfec.ToElements()
    for wt in wtypes:
        wtd[jt_GetName(wt)] = wt
    return wtd

#--------------------------------------------------------------
get_all_wall_curves()