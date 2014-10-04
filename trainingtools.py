import itertools,json,sys,numpy,math,operator

global dataDir
dataDir = 'data/'


def assemble_vectors(subject_num,tasks,trials, readings):

    label=-1 # so hacky.... we have to iterate trial AND start on trial 0......sorry

    X = []
    y = []

    for task in tasks:
        label+=1
        for trial in trials:
            for reading in readings:
                X.append(loadVector('subject'+str(subject_num),task,trial,reading))
                y.append(label)
    return X,y



def score_predictions(predictions,y):
    correct = 0
    for index,prediction in enumerate(predictions):
        if prediction == y[index]:
            correct+=1
    return float(correct)/len(y)


## helper functions


def loadVector(subject,task,trial,reading):
    rootDir = dataDir + "%s/%s/%s/"%(task,subject,'trial'+str(trial))
    reading = str(float(reading)).replace('.','-') # turn reading into the format of the filenames
    dic = json.load(open(rootDir + "%s.json"%reading,'rb'))
    B = dic['binnedPowerSpec']
    return [0 if math.isnan(v) else v for v in B['y']]


def testset(trainer,corpus):
    return [x for x in corpus if x != trainer]

