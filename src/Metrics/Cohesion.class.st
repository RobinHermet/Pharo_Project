Class {
	#name : #Cohesion,
	#superclass : #Object,
	#category : #Metrics
}

{ #category : #'as yet unclassified' }
Cohesion >> averageLCOM: model [
    | sumLCOM numberOfClasses classLCOM |
    sumLCOM := 0. 
    numberOfClasses := model allModelClasses size.
    model allModelClasses do: [:class |
        classLCOM := class calculateLCOM2 ifNil: [0].
        ^Transcript show: 'LCOM2 for ', class name, ': ', classLCOM asString; cr;
        show: (sumLCOM := sumLCOM + classLCOM).
    ].
    Transcript show: 'Sum LCOM: ', sumLCOM asString; cr.
    Transcript show: 'Number of classes: ', numberOfClasses asString; cr.
    ^ numberOfClasses > 0
        ifTrue: [(sumLCOM / numberOfClasses) asFloat]
        ifFalse: [0 asFloat]

]
