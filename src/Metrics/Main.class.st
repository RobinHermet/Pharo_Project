Class {
	#name : #Main,
	#superclass : #Object,
	#category : #Metrics
}

{ #category : #accessing }
Main >> main: model [
	"CC=Cyclomatic complexity, avg=average, gt=greater than, GC=god classes, GM=god methods"
	|CCclass nbOfLinesClass avgCCforClasses avgCCforMethods classesForCCgt3 methodsForCCgt2 avgLinesByClass avgLinesByMethod medianLinesOfClasses medianLinesOfMethods nbOfGC nbOfGM 	totalLinesInClasses totalLinesInMethods modelName|.
	"Nom du modèle pour l'affichage"
    modelName := model name ifNil: ['le modèle'].
	"Methods related to cyclomatic complexity"
	CCclass := CyclomaticComplexity new.
	avgCCforClasses := CCclass getAverageCyclomaticComplexityForClasses: model.
	avgCCforMethods := CCclass getAverageCyclomaticComplexityForMethods: model.
	classesForCCgt3 := CCclass getClassesForCyclomaticComplexityGreaterThan: model threshold: 3.
	methodsForCCgt2 := CCclass getMethodsForCyclomaticComplexityGreaterThan: model threshold: 2.
	"Methods related to number of lines"
	nbOfLinesClass := NumberOfLines new.
	avgLinesByClass := nbOfLinesClass averageLinesByClass: model.
	avgLinesByMethod := nbOfLinesClass averageLinesByMethod: model.
	medianLinesOfClasses := nbOfLinesClass medianLinesOfClasses: model.
	medianLinesOfMethods := nbOfLinesClass medianLinesOfMethods: model.
	nbOfGC := nbOfLinesClass numberOfGodClasses: model ceil: 50.
	nbOfGM := nbOfLinesClass numberOfGodMethods: model ceil: 30.
	totalLinesInClasses := nbOfLinesClass totalLinesInClasses: model.
	totalLinesInMethods := nbOfLinesClass totalLinesInMethods: model. 
	
	 "Affichage des résultats"
    ^Transcript
        show: 'Average cyclomatic complexity for classes in ', modelName, ': ', avgCCforClasses asString; cr;
        show: 'Average cyclomatic complexity for methods in ', modelName, ': ', avgCCforMethods asString; cr;
        show: 'Number of classes with cyclomatic complexity greater than 3 in ', modelName, ': ', classesForCCgt3 asString; cr;
        show: 'Number of methods with cyclomatic complexity greater than 2 in ', modelName, ': ', methodsForCCgt2 asString; cr;
        show: 'Average lines by class in ', modelName, ': ', avgLinesByClass asString; cr;
        show: 'Average lines by method in ', modelName, ': ', avgLinesByMethod asString; cr;
        show: 'Median lines of classes in ', modelName, ': ', medianLinesOfClasses asString; cr;
        show: 'Median lines of methods in ', modelName, ': ', medianLinesOfMethods asString; cr;
        show: 'Number of God Classes in ', modelName, ': ', nbOfGC asString; cr;
        show: 'Number of God Methods in ', modelName, ': ', nbOfGM asString; cr;
        show: 'Total lines in classes in ', modelName, ': ', totalLinesInClasses asString; cr;
        show: 'Total lines in methods in ', modelName, ': ', totalLinesInMethods asString; cr.
]
