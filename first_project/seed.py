import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random

from first_app.models import AccessRecord, Topic, WebPage
from django.contrib.auth.models import User
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()

    return t

def populate_access_records(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date_time()
        fake_name = fakegen.company()

        webpage = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

def populate_users(N=5):
    for entry in range(N):
        try:
            first_names = [fakegen.first_name_female(), fakegen.first_name_male()]
            last_names = [fakegen.last_name_female(), fakegen.last_name_male()]

            fake_first_name = random.choice(first_names)
            fake_last_name = random.choice(last_names)

            fake_email = fakegen.free_email()
            fake_password = fake_email

            user = User.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, username = fake_first_name, email = fake_email, password = fake_password)
        except IntegrityError:
            print ('Ignore')

if __name__ == '__main__':
    print('Populating script!')
    # populate_access_records(20)
    populate_users(2)
    print('Populating complete!')
