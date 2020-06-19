import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

infile = open("DS_Senti_Class.pickle",'rb')
new_dict = pickle.load(infile)
infile.close()
#print(new_dict)
labels=[]
sentiments=[]
for k,v in new_dict.items():
	sentiments.append([v[0]])
	labels.append(v[1])

labels=np.array(labels)
print(labels)

tfidf = open("TFIDFMAtrix.pickle",'rb')
features = pickle.load(tfidf)
infile.close()
#print(features)

features=np.array(features)
#print(features.shape)
for i in range(0,178):
	features=np.delete(features, 1, 0)
#print(features.shape)
#print(labels.shape)

features=np.append(features, sentiments, axis=1)
#print(features.shape)

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

model = RandomForestClassifier()
model.fit(train_features, train_labels)
#model.fit(features, labels)
result=model.predict(test_features)

answer=result==test_labels

#print(test_features.shape)
count=0
for each in answer:
	if each==True:
		count=count+1
print(count," corectly classified")

fp=0
for i in range(0,result.size):
	if test_labels[i]==False and result[i]==True:
		fp=fp+1

fn=0
for i in range(0,result.size):
	if test_labels[i]==True and result[i]==False:
		fn=fn+1

print(fp," fp")
print(fn," fn")

tn=0
for i in range(0,result.size):
	if test_labels[i]==False and result[i]==False:
		tn=tn+1

print(tn," tn")

tp=0
for i in range(0,result.size):
	if test_labels[i]==True and result[i]==True:
		tp=tp+1

print(tp," tp")