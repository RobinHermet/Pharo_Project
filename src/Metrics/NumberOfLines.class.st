Class {
	#name : #NumberOfLines,
	#superclass : #Object,
	#category : #Metrics
}

{ #category : #accessing }
NumberOfLines >> averageLinesByClass: model [
    | totalLines numberOfClasses |
    totalLines := self totalLinesInClasses: model.
	 numberOfClasses := model allModelClasses size.
	^(totalLines / numberOfClasses) asFloat 

]

{ #category : #accessing }
NumberOfLines >> test: model [ 
	^2
]

{ #category : #accessing }
NumberOfLines >> totalLinesInClasses: model [
    | totalLines |
    totalLines := 0.
    model allModelClasses do: [:class | 
       totalLines := totalLines + class numberOfLinesOfCode].
    ^totalLines 
]
