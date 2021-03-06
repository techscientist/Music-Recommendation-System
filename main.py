import numpy as np
import parse
import utils
import similarity_functions as sf
np.set_printoptions(threshold='nan')

def main(load=True, setno):
    training, test, metadata = parse.load(setno)
    if not load:
        ratingMatrix = utils.constructRatingMatrix(training, metadata)
        similarity = sf.cosineMatrix(ratingMatrix)
        np.savetxt('similarity%s.txt' % (setno), similarity)
        print "similarity done"
        prediction = utils.predictRating(similarity, ratingMatrix)
        np.savetxt('prediction%s.txt' % (setno), prediction)
        print "prediction done"
    else:
        with open('similarity.txt') as f:
            similarity = np.loadtxt(f)
        with open('prediction.txt') as f:
            prediction = np.loadtxt(f)
    
    import pdb; pdb.set_trace()
    #import pdb; pdb.set_trace();
    predictionOnTest = prediction[test[:, 0].astype(int) - 1, test[:, 1].astype(int)-1]
    error = predictionOnTest - test[:, 2]
    return np.abs(error).mean()

if __name__ == '__main__':
    for i in xrange(1, 6):
        print main(False, setno=i)
