from typing import *
from drug_ocr.paddleocr import PaddleOCR
import pandas as pd 
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

global oc_r
oc_r = PaddleOCR(use_angle_cls=True, lang='en')

def ocr(img: str) ->pd.DataFrame:
    
    r'''
    Arguments:-
    path : Image directory path in string format or image in ndarray 
    
    Return:-
    return  DataFrame with columns of ['xmin','xmax','ymin','ymax','width','height' ,'word']

    '''

    res = oc_r.ocr(img, cls=True)

    lis = []
    for i in range(len(res[0])):
        word = str(res[0][i][1][0])
        xmin = min(res[0][i][0][0][0] ,res[0][i][0][3][0]) # [0][i][0]
        xmax = max(res[0][i][0][1][0] ,res[0][i][0][2][0])
        ymin = min(res[0][i][0][0][1] ,res[0][i][0][1][1])
        ymax = max(res[0][i][0][2][1] ,res[0][i][0][3][1])
        lis.append((int(xmin) ,int(xmax) ,int(ymin) ,int(ymax) ,int(xmax-xmin) ,int(ymax-ymin) ,word.lower()))

    df = pd.DataFrame(lis , columns = ['xmin','xmax','ymin','ymax','width','height' ,'word'] )
    return df 