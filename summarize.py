from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline


def summarize(text):
    tokenizer = AutoTokenizer.from_pretrained("AdShenoy/Bart-samsum")
    model = AutoModelForSeq2SeqLM.from_pretrained("AdShenoy/Bart-samsum")


    #text = "The past 12 months have been the worst for aviation fatalities so far this decade - with the total of number of people killed if airline crashes reaching 1,050 even before the Air Asia plane vanished. Two incidents involving Malaysia Airlines planes - one over eastern Ukraine and the other in the Indian Ocean - led to the deaths of 537 people, while an Air Algerie crash in Mali killed 116 and TransAsia Airways crash in Taiwan killed a further 49 people. The remaining 456 fatalities were largely in incidents involving small commercial planes or private aircraft operating on behalf of companies, governments or organisations. Despite 2014 having the highest number of fatalities so far this decade, the total number of crashes was in fact the lowest since the first commercial jet airliner took off in 1949 - totalling just 111 across the whole world over the past 12 months. The all-time deadliest year for aviation was 1972 when a staggering 2,429 people were killed in a total of 55 plane crashes - including the crash of Aeroflot Flight 217, which killed 174 people in Russia, and Convair 990 Coronado, which claimed 155 lives in Spain. However this years total death count of 1,212, including those presumed dead on board the missing Air Asia flight, marks a significant rise on the very low 265 fatalities in 2013 - which led to it being named the safest year in aviation since the end of the Second World War. Scroll down for videos. Deadly: The past 12 months have been the worst for aviation fatalities so far this decade - with the total of number of people killed if airline crashes reaching 1,158 even before the Air Asia plane (pictured) vanished. Fatal: Two incidents involving Malaysia Airlines planes - one over eastern Ukraine (pictured) and the other in the Indian Ocean - led to the deaths of 537 people. Surprising: Despite 2014 having the highest number of fatalities so far this decade, the total number of crashes was in fact the lowest since the first commercial jet airliner took off in 1949. 2014 has been a horrific year for Malaysia-based airlines, with 537 people dying on Malaysia Airlines planes, and a further 162 people missing and feared dead in this weeks Air Asia incident. In total more than half the people killed in aviation incidents this year had been flying on board Malaysia-registered planes."

    generator = pipeline(task = "summarization",model=model, tokenizer=tokenizer,truncation = True)
    preds = generator(text)
    s=""
    s=s+str(preds)
    s=s.replace("{","")
    s=s.replace("[","")
    s=s.replace("}","")
    s=s.replace("]","")
    s=s.replace("[{\'summary_text\': \'","")
    s=s[17:]
    s = s.replace("\\n", "\n")

    return s
