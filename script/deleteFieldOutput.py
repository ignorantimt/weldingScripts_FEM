from abaqus import *

modelName = "singleBlade"

odb = session.openOdb(odbFileName)
model = odb.models[modelName]
steps = model.steps.keys()
outputsToDelete = ["F-Output-1", "H-Output-1"]

for stepName in steps:
    step = model.steps[stepName]
    for outputName in outputsToDelete:
        if outputName in step.fieldOutputs.keys():
            del step.fieldOutputs[outputName]
        if outputName in step.historyRegions.keys():
            del step.historyRegions[outputName]

odb.save()
odb.close()
