import sys, urllib,json,requests,csv

with open('keyword_corpus.csv','w',newline='') as f:
    writer=csv.writer(f,dialect='excel')
    for num in range(99999):
        url="https://api.themoviedb.org/3/keyword/"+str(num)+"?api_key=27304d0cacd43611ff1d8050d749367f"
        r=requests.get(url)
        if(r.status_code==200):
            r=r.json()
            writer.writerow(r)