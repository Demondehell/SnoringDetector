
import json
from sklearn import datasets
from sklearn.model_selection import KFold
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pickle as  cPickle
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
    
from sklearn.metrics import confusion_matrix
            
            
#snoring detection

#mfcc, delta_mfccs, delta2_mfccs size are (13*44)
#
#
json_path = "D:/Work/BioMed/Snoring Detection/Snoring Dataset/data.json"
f = open(json_path)

data = json.load(f)


X_temp = np.array(data['mfcc'])
X=[]
for i in range(len(X_temp)):
    X.append(list(np.concatenate(X_temp[i]). flat))

X= np.array(X)
Y = np.array(data['Label'])

X_train, X_test, y_train, y_test  = train_test_split (X,Y, test_size = 0.25)
#X_train, X_val, y_train, y_val  = train_test_split (X,Y, test_size = 0.2)

#input_shape = (X_train.shape[1], X_train.shape[2])

# print("Start Trainng")

# mlp = MLPClassifier(hidden_layer_sizes=(8,8,8), activation='relu', solver='adam', max_iter=500)
# mlp.fit(X_train,y_train)


# print("Trainng finished")
# predict_train = mlp.predict(X_train)
# predict_test = mlp.predict(X_test)
# print(mean_squared_error(y_train,predict_train))
# print(mean_squared_error(y_test,predict_test))

kf = KFold(n_splits=10,random_state =1, shuffle=True)
kf.get_n_splits(X)


X_train_Best=[]
X_test_Best=[]

y_train_Best=[]
y_test_Best=[]

ypred_Train_Best=[]
ypred_Test_Best=[]

train_index_best = []
test_index_best = []
#MSE_Best = 0
MSE__Train_Best = 0
MSE__Test_Best = 0
# #************* Cross validation **********************************************
cnt = 0
for train_index, test_index in kf.split(X):

    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = Y[train_index], Y[test_index]
    
 
#     #***** multi layer perceptron 3 layer each layer 3 node
    mlp = MLPClassifier(hidden_layer_sizes=(8,8,8), activation='relu', solver='adam', max_iter=500)
    mlp.fit(X_train,y_train)
    
    predict_train = mlp.predict(X_train)
    predict_test = mlp.predict(X_test)
    
    
    MSE_train =  mean_squared_error(y_train,predict_train)
    MSE_Test = mean_squared_error(y_test,predict_test)
    
    print(str(MSE__Test_Best) + " , " + str(MSE_Test ))
    if (cnt == 0):
        X_train_Best = X_train
        X_test_Best = X_test
        
        y_train_Best = y_train
        y_test_Best = y_test
        
        ypred_Train_Best = predict_train
        ypred_Test_Best = predict_test
        
        train_index_best = train_index
        test_index_best = test_index
        
        MSE__Train_Best = MSE_train
        MSE__Test_Best = MSE_Test
        
        # save the classifier
        with open('D:/Work/BioMed/Snoring Detection/Model/Snoring_MLP.pkl', 'wb') as fid:
            cPickle.dump(mlp, fid)    
    
     
        cnt= 1
    else:
          if (MSE_Test < MSE__Test_Best):
              print("Updated")
              X_train_Best=[]
              X_test_Best=[]
              
              y_train_Best=[]
              y_test_Best=[]
              
              ypred_Train_Best=[]
              ypred_Test_Best=[]
              
              train_index_best = []
              test_index_best = []
              
              X_train_Best = X_train
              X_test_Best = X_test
              y_train_Best = y_train
              y_test_Best = y_test
              ypred_Train_Best = predict_train
              ypred_Test_Best = predict_test
              train_index_best = train_index
              test_index_best = test_index
              MSE__Train_Best = MSE_train
              MSE__Test_Best =  MSE_Test
              with open('D:/Work/BioMed/Snoring Detection/Model/Snoring_MLP_500iter.pkl', 'wb') as fid:
                  cPickle.dump(mlp, fid)    
        
    print(mean_squared_error(y_train,predict_train))
    print("MSE Train "+ str(MSE__Train_Best))
    print("MSE Test "+ str(MSE__Test_Best))
    print("****************************************************")
    
    
print("Best MSE Train " + str(MSE__Train_Best))
print("Best MSE Test " + str(MSE__Test_Best)) 
    

Best_train_index = train_index_best
Best_test_index = test_index_best    

Best_train_Result = ypred_Train_Best
Best_test_Result = ypred_Test_Best
    
#plot_confusion_matrix(y_test_Best, ypred_Test_Best)

print(confusion_matrix(y_test_Best, ypred_Test_Best))