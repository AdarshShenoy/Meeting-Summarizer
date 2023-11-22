#import torch
#import transformers

##FASTAI
from fastai.text.all import *

from blurr.text.data.all import *
from blurr.text.modeling.all import *

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

from huggingface_hub import from_pretrained_fastai


def summarize(text):
    repo_id = "AdShenoy/Bart_summarizer"

    #global flag
    #flag=0
    #fhand=open("Transcripts/transcript.txt", 'r')
    #tra=fhand.read()
    #text =tra

    learner_blurr = from_pretrained_fastai(repo_id)
    outputs = learner_blurr.blurr_generate(text, early_stopping=False, num_return_sequences=1, min_length=150, max_length=800)

    for idx, o in enumerate(outputs):
        print(f'=== Prediction {idx+1} ===\n{o}\n')

    op=""
    op=op+str(outputs[0])

    op= op[22:-2]
    print(op)
    #with open('Transcripts/summary.txt', 'w') as f:
    #    f.write(op)
    #f.close()
    #flag=1


text = "The past 12 months have been the worst for aviation fatalities so far this decade - with the total of number of people killed if airline crashes reaching 1,050 even before the Air Asia plane vanished. Two incidents involving Malaysia Airlines planes - one over eastern Ukraine and the other in the Indian Ocean - led to the deaths of 537 people, while an Air Algerie crash in Mali killed 116 and TransAsia Airways crash in Taiwan killed a further 49 people. The remaining 456 fatalities were largely in incidents involving small commercial planes or private aircraft operating on behalf of companies, governments or organisations. Despite 2014 having the highest number of fatalities so far this decade, the total number of crashes was in fact the lowest since the first commercial jet airliner took off in 1949 - totalling just 111 across the whole world over the past 12 months. The all-time deadliest year for aviation was 1972 when a staggering 2,429 people were killed in a total of 55 plane crashes - including the crash of Aeroflot Flight 217, which killed 174 people in Russia, and Convair 990 Coronado, which claimed 155 lives in Spain. However this years total death count of 1,212, including those presumed dead on board the missing Air Asia flight, marks a significant rise on the very low 265 fatalities in 2013 - which led to it being named the safest year in aviation since the end of the Second World War. Scroll down for videos. Deadly: The past 12 months have been the worst for aviation fatalities so far this decade - with the total of number of people killed if airline crashes reaching 1,158 even before the Air Asia plane (pictured) vanished. Fatal: Two incidents involving Malaysia Airlines planes - one over eastern Ukraine (pictured) and the other in the Indian Ocean - led to the deaths of 537 people. Surprising: Despite 2014 having the highest number of fatalities so far this decade, the total number of crashes was in fact the lowest since the first commercial jet airliner took off in 1949. 2014 has been a horrific year for Malaysia-based airlines, with 537 people dying on Malaysia Airlines planes, and a further 162 people missing and feared dead in this weeks Air Asia incident. In total more than half the people killed in aviation incidents this year had been flying on board Malaysia-registered planes."
summarize(text)    