import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import json
import re

ufo_first100_file_path = 'data/ufo_first100records.json'
ufo_path = 'data/ufodata.json'

def get_records(file_path=ufo_first100_file_path):
    # TODO: this doesn't scale well and doesn't help with looking at the data.
    # Possible solutions: load into pandas dataframe or mongodb, maybe both.
    records = []
    with open(file_path) as f:
        for i in f:
            records.append(json.loads(i))
    return records


def extract_val(header, reg):
    reg = re.search(reg, header)
    if reg:
        return reg.group(1)
    else:
        return None

def headers_split(header):
    occured = extract_val(header, r"Occurred : (.*?)  ")
    reported = extract_val(header, r"Reported: (.*?)Posted")
    posted = extract_val(header, r"Posted: (.*?)Location")
    location = extract_val(header, r"Location: (.*?)Shape")
    shape = extract_val(header, r"Shape: (.*?)Duration")
    duration = extract_val(header,r"Duration:(.*?)$")
    if location:
        splitter = location.split(", ")
        if len(splitter) > 1:
            city = splitter[0]
            state = splitter[1]
        else:
            city, state = ' ', ' '
    else:
        city , state = ' ', ' '
    return occured, reported, posted, location, shape, duration, city, state


def records_to_df(records, max_iters = 10000):
    occurs, reporteds, posteds, locations = [], [], [], []
    shapes, durations, citys, states, texts = [], [], [], [], []
    for i in range(min(len(records), max_iters)):
        soup = BeautifulSoup(records[i]['html'], 'html.parser')
        lst_td = soup.find_all('td')
        if(len(lst_td) == 0):
            continue
        header = lst_td[0].text
        occured, reported, posted, location, shape, duration, city, state = headers_split(
            header)
        if(len(lst_td) > 1):
            text = lst_td[1].text
        else:
            text = ' '
        occurs.append(occured)
        reporteds.append(reported)
        posteds.append(posted)
        locations.append(location)
        shapes.append(shape)
        durations.append(duration)
        citys.append(city)
        states.append(state)
        texts.append(text)
    pd_dict = {'occured': occurs, 'reported': reporteds,
                'posted': posteds, 'location': locations, 'shape': shapes,
                'duration': durations, 'city' : citys, 'state' : states, 'text': texts}
    df = pd.DataFrame(pd_dict)
    #df[['city', 'state']] = df['location'].str.split(", ", expand = True)
    return pd.DataFrame(pd_dict)


def get_df(path=ufo_first100_file_path, max_iters = 1000):
    records = get_records(path)
    return records_to_df(records, max_iters)

if __name__ == '__main__':
    records = get_records(ufo_path)
    df = records_to_df(records, max_iters = 1000)
    print(df.head(15))
    print(df.columns)
    # print(df.head())
    print(df)
