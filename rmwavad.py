import matplotlib.pyplot as plt
import numpy as np
import pickle

def runningMeanFast(x, N):
    return np.convolve(x, np.ones((N,))/N)
    return np.convolve(x, np.ones((N,))/N)[(N-1):]

# run python audioAnalysis.py classifyFile -i ~/Downloads/audio.wav  --model svm --classifier data/svmSM
pl=pickle.load(open('/media/me/TOSHIBA EXT/tmp/pl.pickle'))
plt.scatter(range(0,len(pl)),pl, color='#000000', s=1)
avg = runningMeanFast(pl, 200)
plt.scatter(range(0,len(avg)),avg, color='blue', s=1)
plt.savefig('/tmp/fig.png')
