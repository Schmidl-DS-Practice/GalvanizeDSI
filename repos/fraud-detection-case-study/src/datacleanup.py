import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from string import punctuation
import re
import json # to work with json file format
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)
plt.rcParams['figure.dpi'] = 300

class Clean(object):
    def __init__(self, data):
        self.data = data
        self.unusable_columns = ['object_id', 'org_twitter', 'org_facebook', 
                                    'previous_payouts', 'ticket_types', 'acct_type', 'gts',
                                    'email_domain', 'country','venue_country', 'venue_state',]

    def clean(self):
        self._target()
        self._drop()
        self._dummies()
        self._fillna()
        self._clean_descrip()
        self._clean_org_descrip()
        self._join_text_cols()
        self._text_fraud_proba()
        y = self.data.pop('fraud')
        return self.data, y

    def _fillna(self):
        self.data = self.data.fillna(0, axis=1)
        return self
    
    def _target(self): 
        self.data['fraud'] = np.where((self.data['acct_type']=='premium'),0,1)
        return self
    
    def _drop(self):
        self.data = self.data.drop(self.unusable_columns, axis=1, inplace=True)
        return self

    def _dummies(self):
        self.data = pd.get_dummies(data=data, columns=['currency', 'delivery_method',
                                                         'payout_type','user_type', 
                                                         'channels', 'listed'])                                             
        return self
    
    def _fraud_orgs(self):
        # self.data['fraud_org'] = np.where(self.data['org_name']=='')
        pass 

    def _clean_descrip(self):
        self.souped_list = []
        temp_lst = []
        for i in range(self.data.shape[0]):
            soup = (BeautifulSoup(self.data['description'].iloc[i], 'html.parser'))
            temp_lst.append(soup.find_all('strong'))
            temp_lst.append(soup.find_all('font'))
            temp_lst = temp_lst[0] + temp_lst[1]
            self.souped_list.append(str(temp_lst))
            temp_lst = []
        # Remove all 'html' labels
        for i in range(len(self.souped_list)):
            self.souped_list[i] = re.sub(r'\<.*?\>', '', self.souped_list[i])
            self.souped_list[i] = re.sub(r'\s+', ' ', self.souped_list[i], flags=re.I)
        # remove given punctuation marks from a each string
        for i in range(len(self.souped_list)):
            for character in punctuation:
                self.souped_list[i] = self.souped_list[i].replace(character,'')
        # Lowercase all, Remove all stop words, Remove words less than 3 characters long
        stop_words = set(stopwords.words('english'))
        for i in range(len(self.souped_list)):
            self.souped_list[i] = ' '.join([w for w in self.souped_list[i].split() if len(w) > 3])
            self.souped_list[i] = self.souped_list[i].lower()
            self.souped_list[i] = ' '.join([w for w in self.souped_list[i].split() if w not in stop_words])
            self.souped_list[i] = ' '.join(set(self.souped_list[i].split()))
        # Lemmatize all words in the corpus
        lemmatizer = WordNetLemmatizer()
        for i in range(len(self.souped_list)):
            self.souped_list[i] = ' '.join([lemmatizer.lemmatize(w) for w in self.souped_list[i].split()])
        self.data['description_clean'] = self.souped_list
        return self
        
    def _clean_org_descrip(self):
        self.org_souped_list = []
        for i in range(self.data.shape[0]):
            org_soup = (BeautifulSoup(self.data['org_desc'].iloc[i], 'html.parser'))
            self.org_souped_list.append(org_soup)
        for i in range(len(self.org_souped_list)):
            self.org_souped_list[i] = str(self.org_souped_list[i])
            self.org_souped_list[i] = re.sub(r'\<.*?\>', '', self.org_souped_list[i])  
            self.org_souped_list[i] = re.sub(r'\s+', ' ', self.org_souped_list[i], flags=re.I) 
        # remove given punctuation marks from a each string
        for i in range(len(self.org_souped_list)):
            for character in punctuation:
                self.org_souped_list[i] = self.org_souped_list[i].replace(character,'')
        # Lowercase all, Remove all stop words, Remove words less than 3 characters long
        stop_words = set(stopwords.words('english'))
        for i in range(len(self.org_souped_list)):
            self.org_souped_list[i] = ' '.join([w for w in self.org_souped_list[i].split() if len(w) > 3])
            self.org_souped_list[i] = self.org_souped_list[i].lower()
            self.org_souped_list[i] = ' '.join([w for w in self.org_souped_list[i].split() if w not in stop_words])
            self.org_souped_list[i] = ' '.join(set(self.org_souped_list[i].split()))
        # Lemmatize all words in the corpus
        lemmatizer = WordNetLemmatizer()
        for i in range(len(self.org_souped_list)):
            self.org_souped_list[i] = ' '.join([lemmatizer.lemmatize(w) for w in self.org_souped_list[i].split()])
        self.data['org_desc_clean'] = self.org_souped_list
        return self
    
    def _join_text_cols(self):
        cols = ['description_clean', 'name', 'org_desc_clean', 'org_name', 
                'payee_name', 'venue_address', 'venue_name']  
        for col in cols:
            self.data[col] = self.data[col].astype(str)
                
        self.data['all_text'] = self.data[cols].agg(' '.join, axis=1)
        return self


    def _text_fraud_proba(self):
        documents = self.data['all_text']
        labels = self.data['fraud']
        # Create the Tf-Idf of the text from previous extraction
        tfidfconverter = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7)
        X = tfidfconverter.fit_transform(documents).toarray()
        # Training and Test sets
        X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=.2, random_state=42)
        classifier = RandomForestClassifier(n_estimators=1000, bootstrap=True, max_features='sqrt', random_state=42)
        classifier.fit(X_train, y_train) 
        # Predict on Train
        tr_y_pred = classifier.predict(X_train)
        tr_y_pred_proba = classifier.predict_proba(X_train)[:, 1]
        # Predict on Test
        y_pred = classifier.predict(X_test)
        y_pred_proba = classifier.predict_proba(X_test)[:, 1]
        # Get results for text probability column
        result_pred_proba = classifier.predict_proba(X)[:, 1]
        self.data['text_probability'] = result_pred_proba
        cols = ['description_clean', 'name', 'org_desc_clean', 'org_name', 
                'payee_name', 'venue_address', 'venue_name', 'all_text','description','org_desc']  
        self.data.drop(cols, axis=1, inplace=True)
        return self

def _update_dt(df, cols):
    '''
    Changes datetime format from UNIX to mm/dd/year
    Returns updated dataframe
    '''
    for col in cols:
        df[col] = pd.to_datetime(df[col], unit='s').dt.date
    return df

    
#read data
data = pd.read_json('../data/data.json')
clean = Clean(data)
X, y  = clean.clean()
print(X.head(1))
#convert date columns to datetime
# date_cols = ['approx_payout_date','event_created', 'event_end', 'event_published','event_start']
# data = update_dt(data, date_cols)
#consolidate important columns into a new dataframe
#X = data[['sale_duration','sale_duration2','delivery_method',
#             'has_analytics','payout_type','fb_published','currency','channels',
#             'user_type','num_payouts','user_age','fraud']]
