Class {
	#name : #CyclomaticComplexity,
	#superclass : #Object,
	#category : #Metrics
}

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
