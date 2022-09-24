from dputils import scrape
import pandas as pd
#get the data as soup obj
#create the setup dictionaries 
#pass the dictionaries into extract_many()
#repeat step 1 to 3 till data is coming
#check and save data into the file


def getdata(q):
    
    t = {'tag':'div', 'attrs':{'class':'_1YokD2 _3Mn1Gg'}}
    rep_items = {'tag':'div', 'attrs':{'class':'_1AtVbE col-12-12'}}
    title = {'tag':'div', 'attrs':{'class':'_4rR01T'}}
    price = {'tag':'div','attrs':{'class':'_30jeq3 _1_WHN1'}}
    link = {'tag':'a','attrs':{'class':'_1fQZEK'},'output':'href'}
    
    pos = 1
    all_data = []
    while True:
        url = f'https://www.flipkart.com/search?q={q}&page={pos}'
        print(url)
        soup = scrape.get_webpage_data(url)
        data = scrape.extract_many( soup, target=t, items=rep_items,title=title,price=price, link=link )
        if isinstance(data, list):
            if len(data) > 0:
                pos += 1
                all_data.extend(data)
            else:
                break
        else:
            break
    return all_data


# use
laptops = getdata('laptops')
pd.DataFrame(laptops).to_csv('laptop_data.csv')

