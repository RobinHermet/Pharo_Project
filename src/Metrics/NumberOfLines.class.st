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
NumberOfLines >> averageLinesByMethod: model [
    | totalLines numberOfMethods |
    totalLines := self totalLinesInMethods: model.
	 numberOfMethods := model allModelMethods size.
	^(totalLines / numberOfMethods) asFloat 
]

{ #category : #accessing }
NumberOfLines >> medianLinesOfClasses: model [ 
	| linesPerClass sortedLines middleIndex median |
    
    linesPerClass := model allModelClasses collect: [:eachClass | eachClass numberOfLinesOfCode ifNil: [0]].
    sortedLines := linesPerClass asSortedCollection.
    
    middleIndex := sortedLines size // 2.
    
    median := (sortedLines size \\ 2) = 0
        ifTrue: [(sortedLines at: middleIndex) + (sortedLines at: middleIndex + 1) / 2]
        ifFalse: [sortedLines at: middleIndex + 1].
    
    ^median asInteger 
]

{ #category : #accessing }
NumberOfLines >> medianLinesOfMethods: model [ 
	| linesPerMethod sortedLines middleIndex median |
    
    linesPerMethod := model allModelMethods collect: [:eachClass | eachClass numberOfLinesOfCode ifNil: [0]].
    sortedLines := linesPerMethod asSortedCollection.
    
    middleIndex := sortedLines size // 2.
    
    median := (sortedLines size \\ 2) = 0
        ifTrue: [(sortedLines at: middleIndex) + (sortedLines at: middleIndex + 1) / 2]
        ifFalse: [sortedLines at: middleIndex + 1].
    
    ^median asInteger 
]

{ #category : #accessing }
NumberOfLines >> numberOfGodClasses: model ceil: aCeil [ 
	| godClassesCount |
    
    godClassesCount := model allModelClasses count: [:eachClass | 
        (eachClass numberOfLinesOfCode ifNil: [0]) > aCeil].
    
    ^godClassesCount
]

{ #category : #accessing }
NumberOfLines >> numberOfGodMethods: model ceil: aCeil [ 
	| godMethodsCount |
    
    godMethodsCount := model allModelMethods count: [:eachMethod | 
        (eachMethod numberOfLinesOfCode ifNil: [0]) > aCeil].
    
    ^godMethodsCount
]

{ #category : #accessing }
NumberOfLines >> totalLinesInClasses: model [
    | totalLines |
    totalLines := 0.
    model allModelClasses do: [:class | 
       totalLines := totalLines + class numberOfLinesOfCode].
    ^totalLines 
]

{ #category : #accessing }
NumberOfLines >> totalLinesInMethods: model [
    | totalLines |
    totalLines := 0.
    model allModelMethods do: [:method | 
       totalLines := totalLines + method numberOfLinesOfCode].
    ^totalLines 
]
