import matplotlib.pyplot as plt
import numpy as np
import pickle

def runningMeanFast(x, N):
    return np.convolve(x, np.ones((N,))/N)
    return np.convolve(x, np.ones((N,))/N)[(N-1):]

# run python audioAnalysis.py classifyFile -i ~/Downloads/audio.wav  --model svm --classifier data/svmSM
# from [0,1] to [-1,1]
pl=pickle.load(open('pl.pickle'))
#print type(pl), len(pl)
for i in range(len(pl)):
    pl[i] = 2*pl[i]-1

# rm noise
for i in range(len(pl)):
    if abs(pl[i])<.95:
        pl[i] = 0


#print list(runningMeanFast(range(100), 20))

plt.scatter(range(0,len(pl)),pl, color='#000000', s=1)

# average
newpl = [0]*len(pl)
n = 50
for i in range(len(pl)):
    c = 0
    for j in range(-n,n+1):
        if i+j>=0 and i+j<len(pl):
            newpl[i] += pl[i+j]
            c+=1
    newpl[i]=newpl[i]/c
pl = newpl

ads = []
frm = None
sign = 1
for i in range(len(pl)):
    if sign == 1 and pl[i]<0:
        frm = i
        sign = -1
    elif sign == -1 and pl[i]>0:
        if frm:
            mn = float('inf')
            for j in range(frm, i):
                mn = min(mn, pl[j])
            #print frm,i,(i-frm)/60.
            comment = '#'
            if mn < -.2:
                comment = ''
                ads.append([frm, i])
            print comment+'play ~/Downloads/audio.wav trim %d %d # %f' % (frm, i-frm, mn)
        sign = 1
print ads

plt.scatter(range(0,len(pl)),pl, color='blue', s=1)
plt.scatter(range(0,len(pl)),[0]*len(pl), color='red', s=1)
#avg = runningMeanFast(pl, 200)
#plt.scatter(range(0,len(avg)),avg, color='blue', s=1)
plt.savefig('/tmp/fig.png')
