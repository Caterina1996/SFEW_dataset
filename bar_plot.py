#!/usr/bin/env pythonç

import matplotlib.pyplot as plt
import numpy as np
import numpy as np

#Plots number of samples per partition in a bar plot for the SFEW dataset

N = 7

classes_sfew=["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]
#Vectors obtained from ls command
samples_train=[172,49,76,176,142,151,93]
samples_test=[76, 23, 45, 62, 82, 68, 49]

ind = np.arange(N) 
width = 0.35       
plt.bar(ind, samples_train, width, label='train')
plt.bar(ind + width, samples_test, width,
    label='test')

plt.ylabel('Number of images',fontsize=13)
plt.title('Number of images per emotion in the SFEW dataset',fontsize=15.5)

plt.xticks(ind + width / 2, ("Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"),fontsize=11)

plt.legend(loc='best',fontsize=12)

plt.savefig("sfew_num_samples.png")
plt.show()


