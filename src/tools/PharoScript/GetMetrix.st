| metrixNestJs metrixLoopBackJs working workingNestJs workingLoopBackJs errorsCsvPath|
errorList := OrderedCollection new.
	    errorList add: {jsonFile basename. e}.
	    errorList add: {jsonFile basename. e}.
	CSVFile new generateCSVForError: 'pharoError.csv' data: errorList.