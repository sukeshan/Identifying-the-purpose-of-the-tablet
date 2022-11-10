from OCR import ocr
from conditions import check1 ,check2 ,check3
from scraper import check_use
import numpy as np

def check(file:str ) -> str:
    r'''
    Arguments:-

    file : Image directory path in string format
    
    Return:-

    return  Output (String Format)

    '''
    call = ocr(file)
    call.drop_duplicates(subset = ['word'],inplace = True)
    filter_0 = call.sort_values(by = 'height').tail(15)['word'].values[::-1]
    filter_1 = [call[call.word == line] for line in list(set(filter_0)) if len(line)>=6 and check1 (line) !=0]

    if len(filter_1) ==0 : return 'Sorry given image is not accurate.'
    
    xmax = call.xmax.max()
    xmin = call.xmin.min()

    width_per = int((xmax-xmin)*25 /100)

    temp_hgt = 0
    filter_2 = ''
    for line in filter_1:
        if check2(line.word.values[0]) !=0:
            if line.width.values[0] > width_per and line.height.values[0] > temp_hgt:
                filter_2 = line
                temp_hgt = line.height.values[0]
                
    if len(filter_2) ==0 : return ('Sorry given image is not accurate.. ')

    return  check_use( check3(call ,filter_2 ,width_per) )