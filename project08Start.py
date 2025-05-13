###############################################################################
# Tasks
# 1 - Create a training set
# 2 - Train a 'dumb' rule-based classifier
# 3 - Create a test set
# 4 - Apply rule-based classifier to test set
# 5 - Report accuracy of classifier
###############################################################################

###############################################################################
# CONSTANTS
# For use as dictionary keys in training/testing sets and sums
# DONE - Do not modify.
###############################################################################
attributeList = []
attributeList.append("ID")
attributeList.append("radius")
attributeList.append("texture")
attributeList.append("perimeter")
attributeList.append("area")
attributeList.append("smoothness")
attributeList.append("compactness")
attributeList.append("concavity")
attributeList.append("concave")
attributeList.append("symmetry")
attributeList.append("fractal")
attributeList.append("class")



###############################################################################
# 1. Create a training set
# - Read in file
# - Create a dictionary for each line
# - Add this dictionary to a list
#
# makeTrainingSet
# parameters: 
#     - filename: name of the data file containing the training data records
#
# returns: trainingSet: a list of training records (each record is a dict,
#                       that contains attribute values for that record.)
###############################################################################
def makeTrainingSet(filename):
    # DONE - Do not modify.
    trainingSet = []
    # Read in file
    for line in open(filename,'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        linelist = line.split(',')
        # Create a dictionary for the line
        # ( assigns each attribute of the record (each item in the linelist)
        #   to an element of the dictionary, using the constant keys )
        record = {}
        for i in range(len(attributeList)):
              if(i==11): #class label is a character, not a float
                  record[attributeList[i]] = linelist[31].strip() 
              else:
                  record[attributeList[i]] = float(linelist[i])
        # Add the dictionary to a list
        trainingSet.append(record)        

    return trainingSet

###############################################################################
# 2. Train 'Dumb' Classifier
# trainClassifier
# parameters:
#     - trainingSet: a list of training records (each record is a dict,
#                     that contains attribute values for that record.)
#
# returns: a dictionary of midpoints between the averages of each attribute's
#           values for benign and malignant tumors
###############################################################################
def trainClassifier(trainingSet):
    pass

    # TODO
    
    # A. initialize dictionaries for sums of attribute values
    #    and initialize record counts


    # B. process each record in the training set
    #    calculating sums and counts as we go


    # C. calculate averages 


    # D. calcualte midpoints for our classifier


#    return classifier


###############################################################################
# 3. Create a test set
# - Read in file
# - Create a dictionary for each line
# - Initialize each record's predicted class to '0'
# - Add this dictionary to a list
#
# makeTestSet
# parameters: 
#     - filename: name of the data file containing the test data records
#
# returns: testSet: a list of test records (each record is a dict,
#                       that contains attribute values for that record
#                       and where the predicted class is set to 0. 
###############################################################################
def makeTestSet(filename):

    # DONE - Do not modify.
    testset = makeTrainingSet(filename)

    for record in testset:
        record["predicted"] = 0

    return testset


###############################################################################
# 4. Classify test set
#
# classifyTestRecords
# parameters:
#      - testSet: a list of records in the test set, where each record
#                 is a dictionary containing values for each attribute
#      - classifier: a dictionary of midpoint values for each attribute
#
# returns: testSet with the predicted class set to either 2 (benign) or 4 (malignant)
#
# for each record, if the majority of attributes are greater than midpoint
# then predict the record as malignant
###############################################################################
def classifyTestRecords(testSet, classifier):
    pass
    # TODO
    
    # For each record in testset

        # initialize malignant and benign votes to zero

        # for each attribute of the record
            # if attribute value is greater than midpoint then
            # add one to malignant vote. Otherwise, add one to benign vote

        # if malignant vote greater than or equal to benign vote then
        # predicted class of record is malignant (set predicted class value)
        # otherwise, the predicted class is benign
            
#    return testSet


###############################################################################
# 5. Report Accuracy
# reportAccuracy
# parameters:
#      - testSet: a list of records in the test set, where each record
#                 is a dictionary containing values for each attribute
#                 and both the predicted and actual class values are set
#
# returns: None
#
# prints out the number correct / total and accuracy as a percentage
###############################################################################
def reportAccuracy(testSet):
    pass
    # TODO

    # For each record in the test set, compare the actual class (CLASS)
    # and the predicted class ("predicted") to calculate a count of correctly
    # classified records.  Use this to calculate accuracy.

###############################################################################
def dumpStats(classifier,benignAverages,malignantAverages):
    pass
# TODO
# print out the averages and classifier cutoff for each of the 9 categories
# format string to reproduce the table in the demo is
# print '%28s %12.3f %12.3f %12.3f'%(key,malignanAvg[key],classifier[key],benignAvg[key])


def checkSomePatients(testDataRecordsList, classifier):
    pass
# TODO
# starts a prompting loop. Prompts for a patient ID
# for each value, prints out the patient's value, the classifier cutoff and the diagnosis
# prints out the final diagnosis

    
###############################################################################
# main - starts the program
###############################################################################
def main():
    # TODO
    print "Reading in training data..."
    trainingSet = []
    trainingFile = "cancerTrainingData.txt"
    trainingSet = makeTrainingSet(trainingFile)
    print "Done reading training data.\n"

    print "Training classifier..."    
    # add call to appropriate function
    print "Done training classifier.\n"

    print "Present Classifier Stats"
    # add call to appropriate function

    print "Reading in test data..."
    testFile = "cancerTestingData.txt"
    testSet = makeTestSet(testFile)
    print "Done reading test data.\n"

    print "Classifying records..."
    # add call to appropriate function

    print "Done classifying.\n"
    # add call to appropriate function

    print "Check some Patients"
    # add call to appropriate function    

    print "Program finished."
    
main()
