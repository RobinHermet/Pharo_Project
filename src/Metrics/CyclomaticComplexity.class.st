Class {
	#name : #CyclomaticComplexity,
	#superclass : #Object,
	#category : #Metrics
}

{ #category : #sorting }
CyclomaticComplexity >> getAverageCyclomaticComplexityForClasses: model [
| complexitySum numberOfClasses complexitySumInClass moyenne |
complexitySum := 0.
numberOfClasses := 0.
complexitySumInClass := 0.
model allClasses do: [:class | 
	class allMethods do: [ :method |
		method cyclomaticComplexity > 0 ifTrue: [
        complexitySumInClass  := complexitySumInClass + method cyclomaticComplexity.
		 ].
    ].
		complexitySumInClass > 0 ifTrue: [ 
			numberOfClasses := numberOfClasses + 1.
			complexitySum := complexitySum + complexitySumInClass.
			 ].
		complexitySumInClass := 0.
].

moyenne := (complexitySum / numberOfClasses) asFloat.
^moyenne
]

{ #category : #sorting }
CyclomaticComplexity >> getAverageCyclomaticComplexityForMethods: model [
| complexitySum numberOfMethods moyenne |
complexitySum := 0.
numberOfMethods := 0.
model allMethods do: [:method | 
    method cyclomaticComplexity > 0 ifTrue: [
        complexitySum := complexitySum + method cyclomaticComplexity.
			numberOfMethods := numberOfMethods + 1
    ].
].

moyenne := (complexitySum / numberOfMethods) asFloat.
^moyenne
]
