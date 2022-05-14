from json import dumps
from faker import Faker
import collections
import json

def fake_person_generator(length, fake):
    for x in range(length):  # xrange in Python 2.7
        yield {'created_at': fake.date(),
               'time': fake.time(),
               'favorite_count': fake.random_int(),
               'favorited':fake.boolean(),
               'followers_count': fake.random_int(),
               #'lang': fake.lang(),
               'quotecount': fake.random_int(),
               'replycount':fake.random_int(),
               'retweetedcount':fake.random_int(),
               'retweeted': fake.boolean(),
               'status_count': fake.boolean(),
               'text': fake.text(),
               'tweet_id': fake.uuid4(),
               'user_id':fake.uuid4(),
               'favourites_count': fake.random_int(),
               'friends_count': fake.random_int(),
               'location': fake.country(),
               'username': fake.user_name(),
               'screen_name': fake.name(),
                'listed_count':fake.random_int(),
                #'source': fake.website_url,
                'is_quote_status': fake.boolean(),
               'truncated': fake.boolean(),
                'verified':fake.boolean(),
               'protected':fake.boolean(),
                'time_zone': fake.timezone()
               }


database = []
filename = '1M_Tweets'
length = 1000000
fake = Faker()
fpg = fake_person_generator(length, fake)
with open('%s.json' % filename, 'w') as output:
    output.write('[')  # to made json file valid according to JSON format
    for person in fpg:
        json.dump(person, output)
    output.write(']')  # to made json file valid according to JSON format
print ("Done.")