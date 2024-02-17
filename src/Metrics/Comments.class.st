Class {
	#name : #Comments,
	#superclass : #Object,
	#category : #Metrics
}

{ #category : #'as yet unclassified' }
Comments >> proportionOfCommentedClasses: model [
    | commentedClasses |
	commentedClasses := model allModelClasses select: [ :eachClass |
    eachClass comments notNil and: [ eachClass comments isEmpty not ].
].
^((commentedClasses size / model allModelClasses size)*100 asFloat roundTo: 0.01).
]

{ #category : #'as yet unclassified' }
Comments >> proportionOfCommentedMethods: model [
    | commentedMethods |
	commentedMethods := model allModelMethods select: [ :eachMethod |
    eachMethod comments notNil and: [ eachMethod comments isEmpty not ].
].
^((commentedMethods size / model allModelMethods size)*100 asFloat roundTo: 0.01).
]
