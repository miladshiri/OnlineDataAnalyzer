import pandas as pd
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import accuracy_score
import json
from django.core.files.base import ContentFile
import pickle
import hashlib
import random
import time
from django.conf import settings


def prepare_data(data_json, has_label, label):
    data_df = pd.read_json(data_json)
    labels = []
    if has_label:
        labels = data_df.iloc[:, label]
        data_df = data_df.drop(columns=data_df.columns[label])
    return data_df, labels


def train_the_model(train_obj):
    data_df, labels = prepare_data(train_obj.data.data_json, train_obj.has_label, train_obj.label)
    if train_obj.machine.method == settings.SVC:
        ml_model = SVC(kernel=train_obj.machine.kernel)
        ml_model.fit(data_df, labels)
    elif train_obj.machine.method == settings.KNN:
        ml_model = NearestNeighbors(n_neighbors=train_obj.machine.neighbors)
        ml_model.fit(data_df, labels)

    model_file = pickle.dumps(ml_model)
    fid = ContentFile(model_file)
    name = str(train_obj.name) + str(time.time()) + str(random.randint(0, 1000))
    file_name = hashlib.md5(name.encode('utf-8')).hexdigest()
    train_obj.trained_model.save(file_name, fid)
    train_obj.is_trained = True
    train_obj.save()


def predict_data(predict_obj):
    data_df, labels = prepare_data(predict_obj.data.data_json, predict_obj.has_label, predict_obj.label)
    train_obj = predict_obj.train
    ml_model = pickle.load(open(train_obj.trained_model.path, 'rb'))

    if train_obj.machine.method == settings.SVC:
        predictions = ml_model.predict(data_df)

    predict_obj.predictions = str(pd.DataFrame(predictions).to_json())
    predict_obj.save()


def model_accuracy(predict_obj):
    data_df, labels = prepare_data(predict_obj.data.data_json, predict_obj.has_label, predict_obj.label)
    predictions = pd.read_json(predict_obj.predictions)
    return accuracy_score(labels, predictions.sort_index())

