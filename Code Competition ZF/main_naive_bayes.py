# -*- coding: utf-8 -*-

#Solution: Naive Bayes (classification)

import os
from sklearn.naive_bayes import GaussianNB

#help_functions
def get_directory(path_in_folder):
    """
    returns the path of the file independent from
    the direction of the folder
    (path_in_folder is the path behind freeMove_DES folder)
    Input like this: type_in\\path\\like_that
    """
    current_directory = os.getcwd()

    parent_directory =  os.path.split(os.path.split(current_directory)[0])[0] + "\\"
    file_path = os.path.join(parent_directory,path_in_folder)
    return file_path

#data


#model

gnb = GaussianNB()


#train


#test with accuracy


#prediction