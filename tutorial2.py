from trainingtools import assemble_vectors, score_predictions
from sklearn import svm, cross_validation

# list of all readings in each trial (number == seconds from start)
readings = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5]


def cv_calibration_data(subject_number, gesture_pair):

    # training set
    train_X,train_y = assemble_vectors(subject_number,gesture_pair,[0,1,2,3,4,5], readings)

    # fit SVM
    clf = svm.LinearSVC().fit(train_X,train_y)

    # cross-validate
    cv_score = cross_validation.cross_val_score(clf,train_X,train_y, cv=7).mean()
    print(subject_number, gesture_pair, cv_score)

cv_calibration_data(0,['pass','color'])
cv_calibration_data(12,['song','sport'])
