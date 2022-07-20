from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from pipeline import get_records, records_to_df
from os import path, getcwd
from PIL import Image
import numpy as np

def word_cloud(text, title, savefile):
    '''
    Create and save a wordcloud with given text
    '''
    # image_colors = ImageColorGenerator(mask)
    alien_mask = np.array(Image.open(path.join(d, "images/alien_head.jpg")))

    wordcloud = WordCloud(background_color='white', stopwords=ENGLISH_STOP_WORDS, mask=alien_mask).generate_from_text(text)
    plt.figure(figsize=(10, 6), facecolor='k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(title, fontdict={"fontsize": 22})
    plt.tight_layout()
    plt.savefig(savefile, bbox_inches='tight')
    plt.show()
    return 'cookie_monster'

if __name__ == '__main__':
    d = getcwd()
    ufo_path = 'data/ufo_first100records.json'
    rec = get_records(ufo_path)
    data =  records_to_df(rec)
    jt = ' '.join(data['text'])

    word_cloud(jt, "UFO Sightings", 'images/UFO_wordcloud.png')
