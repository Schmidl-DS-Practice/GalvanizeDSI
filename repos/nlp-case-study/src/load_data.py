from bs4 import BeautifulSoup
import pandas as pd
import json
import re

def get_records():
    records = []
    with open('data/ufo_first100records.json') as f:
        for i in f:
            records.append(json.loads(i))
    return records

def parse_records(records):
    parse_records = []

    for record in records:
        mid_list = []
        soup = BeautifulSoup(record['html'], 'html.parser')
        lst_td = soup.find_all('td')
        for j in lst_td:
            mid_list.append(j.text)
        parse_records.append(mid_list)
    return parse_records


def headers_split(header):
    occured = re.search(r"Occurred : (.*?)  ", header).group(1)
    reported = re.search(r"Reported: (.*?)Posted", header).group(1)
    posted = re.search(r"Posted: (.*?)Location", header).group(1)
    location = re.search(r"Location: (.*?)Shape", header).group(1)
    return occured, reported, posted, location


def data_split(records):
    occurs, reporteds, posteds, locations, texts = [],[],[],[],[]
    for i in range(len(records)):
        soup = BeautifulSoup(records[i]['html'], 'html.parser')
        lst_td = soup.find_all('td')
        header = lst_td[0].text
        occured, reported, posted, location = headers_split(header)
        text = lst_td[1].text
        occurs.append(occured)
        reporteds.append(reported)
        posteds.append(posted)
        locations.append(location)
        texts.append(text)
        pd_dict = {'occured': occurs, 'reported' : reporteds,
        'posted' : posteds, 'location' : locations, 'text' : texts}
    return pd.DataFrame(pd_dict)

if __name__ == '__main__':


    records = get_records()
    df = data_split(records)

    # soup = BeautifulSoup(records[0]['html'], 'html.parser')
    # lst_td = soup.find_all('td')
    # split_ = []
    # for i in lst_td:
    #     split_.append((i.text).split(':'))

    # for z in lst_td:
    #     print((z.text).split('Occurred'))
    # print(split_[1][0])
    # parse_records = parse_records(records)
    # re.search(r"Occurred : (.*?)  ", parse_records[0]).group(1)
    df.to_csv('data/df.csv')


