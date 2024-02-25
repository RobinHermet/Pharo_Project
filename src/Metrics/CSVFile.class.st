Class {
	#name : #CSVFile,
	#superclass : #Object,
	#category : #Metrics
}

{ #category : #'as yet unclassified' }
CSVFile >> generateCSVForData: path data: data [
| fichierCSV |
fichierCSV := path asFileReference.
		fichierCSV writeStreamDo: [ :writeStream |
    | csvWriter |
    csvWriter := NeoCSVWriter on: writeStream.
    csvWriter writeHeader: #('Projet' 'Average cyclomatic complexity for classes' 'Average cyclomatic complexity for methods' 'Number of classes with cyclomatic complexity greater than 3' 'Number of methods with cyclomatic complexity greater than 2' 'Average lines by class' 'Average lines by method' 'Median lines of classes' 'Median lines of methods' 'Number of God Classes (more than 50 lines)'  'Number of God Methods (more than 30 lines' 'Total lines in classes' 'Total lines in methods' 'Proportion of commented methods (%)' 'Proportion of commented classes (%)' 'Average LCOM');

	nextPutAll: data].
]

{ #category : #'as yet unclassified' }
CSVFile >> generateCSVForError: path data: data [
| fichierCSV |
fichierCSV := path asFileReference.
		fichierCSV writeStreamDo: [ :writeStream |
    | csvWriter |
    csvWriter := NeoCSVWriter on: writeStream.
    csvWriter writeHeader: #('Projet' 'Error');

	nextPutAll: data].
]
