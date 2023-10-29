
import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from faker import Faker
import random
from courses.models import Courses,Brand,Review


#def seed_brand(n):
    #fake = Faker()
    #images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']

    #for x in range(n):
        #Brand.objects.create(
            #name = fake.name() , 
            #image = f'brand/{images[random.randint(0,12)]}'
        #)
    #print(f'{n} Brands Was Created Successfuly ...')


def seed_cours(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    

    for x in range(n):
        Courses.objects.create(
            name = fake.name() ,
            description=fake.text(max_nb_chars=20) , 
            price = random.uniform(10.5,200) , 
            subtitle=fake.text(max_nb_chars=20) , 
            image = f'courses/{images[random.randint(0,12)]}',
            
            
        )
    print(f'{n} cours Was Created Successfuly ...')



#seed_brand(100)
seed_cours(1000)