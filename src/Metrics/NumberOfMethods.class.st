Class {
	#name : #NumberOfMethods,
	#superclass : #Object,
	#category : #Metrics
}

{ #category : #accessing }
NumberOfMethods >> averageNumberOfMethodsByClass: model [
| totalClasses totalMethods averageMethodsPerClass |
totalClasses:= model allModelClasses size.
totalMethods:= model allModelMethods size.
averageMethodsPerClass:= totalMethods / totalClasses.
^averageMethodsPerClass 
]
