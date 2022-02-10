import json
from datetime import datetime
now = datetime.now()
date_jkt = int(now.strftime("%d"))
date_time = now.strftime("%d %b %Y")


def nganu():
    now = datetime.now()
    print(date_jkt)
    f = open('data.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    # idx = 0
    for idx in range(len(data)):
        if data[idx][date_jkt] == "P":
            print(data[idx][0])
        else:
            continue

    # Closing file
    f.close()

def yang_masuk(absen):
    # st=[]
    st='Bagian CBP '+date_time+'\n\n'
    num=0
    for idx in range(len(absen)):
        if absen[idx][date_jkt] == "P":
            # st.append(str(num+1)+". "+absen[idx][0]+"(WFO)\n")
            st+=str(num+1)+". "+absen[idx][0]+" (WFO)\n"
            num+=1
        else:
            continue
    print(st)
    return st+"\nSehat selalu semua!"