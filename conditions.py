from typing import *

def check1(line:str )-> int:
    r'''
    Arguments:-

    line : Ocr extracted sentences (string format)
    
    Return:-

    return 0 if the word found in the line else return 1 
     '''
    regexs =  ['mfg.dt','mfg','mfd','mfg.date','b.no','batch.no','bno','exipiry','exp','exp.dt','exp.date','exp.','incl','include','inc','inc.','max']

    for regex in regexs:
        if regex in line.lower():return 0

    return 1
#-----------------------------------------===============================================-------------------------------------------------================================
def check2(line : str)-> int:
    r'''
    Arguments:-

    line : Ocr extracted sentences (string format)
    
    Return:-
    
    return 0 if the count variable is less than or equal to 6 else return 1 
     '''
    regexs =['ta','ab','bl','le','et','ts','tab','abl','ble','let','ets','tabl','able','blet','lets','table','ablet','blets','tablet','ablets','cap','aps' ,'psu','sul','ule','les','caps','apsu','psul','sule','ules','capsu','apsul','psule','sules','capsul','apsule','psules','capsule','apsules','capsules']
    count = 0

    for regex in regexs:
        if regex in line.lower():count+=1
    if count>= 6:return 1 

    return 0
#-----------------------------------------===============================================-------------------------------------------------================================
def check3(call ,target : str ,width_per : int) -> str:
    r'''
    Arguments:-

    call : DataFrame return by OCR (DataFrame Format)
    target : Output of the check2 function (string format)
    width_per : 25% of image width (integer format)

    Return:-
    
    return Output (String Format)
     '''
    tar_ind = target.index.values[0]
    tar_height = target.height.values[0]
    
    ch3_1 = call[(call.height >= (tar_height-3)  ) & ( call.height <=(tar_height+7)) & (call.width > width_per )].drop(target.index.values[0]) # filter by height and width
    
    if len(ch3_1) ==0: return target.word.values[0] 

    ch3_2 = ch3_1[(ch3_1.index >= tar_ind-4)  & (ch3_1.index <= tar_ind)] # Filter by index values
    ch3_2 = ch3_2.append(target).sort_index() # Append the target and sort it by index value 

    return ' '.join(list(ch3_2.word.values))
