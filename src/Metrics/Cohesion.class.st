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
        sumLCOM := sumLCOM + classLCOM.
    ].
    ^ numberOfClasses > 0
        ifTrue: [(sumLCOM / numberOfClasses) asFloat]
        ifFalse: [0 asFloat]

]
