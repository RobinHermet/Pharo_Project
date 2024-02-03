Class {
	#name : #Coupling,
	#superclass : #Object,
	#category : #Metrics
}

{ #category : #'as yet unclassified' }
Coupling >> efferentCouplingByClass: model [
    | ECcoupling |
    ECcoupling := Dictionary new.
    
    model allModelClasses do: [ :class | 
        | referencesTypes |
        referencesTypes := Set new.
        
        "Ajouter les types des attributs"
        class attributes do: [ :attribute |
            referencesTypes add: attribute type ].
        
        "Ajouter les types référencés par les méthodes (ex: types de retour, paramètres)"
        class methods do: [ :method |
    		"Collecter les types des paramètres de la méthode"
    		method parameters do: [ :param |
        	referencesTypes add: param declaredType ].
    
    		"Ajouter le type de retour de la méthode, si disponible"
    		referencesTypes add: (method declaredType ifNotNil: [ :type | type ]).
		].
        
        ECcoupling at: class name put: referencesTypes size.
    ].
    
    ^ECcoupling

]
