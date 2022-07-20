from pymongo import MongoClient
from bs4 import BeautifulSoup

# client = MongoClient('localhost', 27017)
# # Access/Initiate Database
# db = client['test_database']
# # Access/Initiate Collection
# test_collection = db['test_collection']
# test_collection.delete_many({'name': 'Martha'})
# test_collection.insert_one({'name': 'Martha', 'city': 'Denver', 'state': 'CO'})
# # test_collection.update_one({'city': 'Denver'}, {'$set': {'name': 'Martha Clair'}})
# print(test_collection.find_one({'name': 'Martha'}))


if __name__ == '__main__':
    # This will need to be updated to reflect the actual path to the
    # ebay_shoes.html data file
    path = 'data/ebay_shoes.html'
    with open(path) as f:
        html_str = f.read()
    save_path = '.'
    soup = BeautifulSoup(html_str, 'lxml')
    
    shoes = soup.select('.img')

    shoe_list = []

    for tag in shoes:
        if 'src' in tag.attrs:
            shoe_list.append(tag)
    
    # print(shoe_list[1])

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    img_list = []

    for image in shoe_list:
        tag = image.select('img')[0]
        val = tag['src']
        img_list.append(val)


                