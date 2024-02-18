Class {
	#name : #Comments,
	#superclass : #Object,
	#category : #Metrics
}

{ #category : #'as yet unclassified' }
Comments >> proportionOfCommentedMethods: model [
    | commentedMethods |
	commentedMethods := model allModelMethods select: [ :eachMethod |
    eachMethod comments notNil and: [ eachMethod comments isEmpty not ].
].
^(commentedMethods size / model allModelMethods size).
]
