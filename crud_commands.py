from dojo_ninjas_app.models import *



 

# Query: Create 3 new dojos
Dojo.objects.create(name='San Jose Dojo', city='San Jose', state='CA')
Dojo.objects.create(name='Dallas Dojo', city='Dallas', state='TX')
Dojo.objects.create(name='Bellevue Dojo', city='Bellevue', state='WA')

# Query: Delete the 3 dojos you just created
Dojo.objects.get(id=1).delete()
Dojo.objects.get(id=2).delete()
Dojo.objects.get(id=3).delete()

# Query: Create 3 more dojos
Dojo.objects.create(name='San Jose Dojo', city='San Jose', state='CA')
Dojo.objects.create(name='Dallas Dojo', city='Dallas', state='TX')
Dojo.objects.create(name='Bellevue Dojo', city='Bellevue', state='WA')

# Query: Create 3 ninjas that belong to the first dojo
Ninja.objects.create(dojo_id=Dojo.objects.get(id=4), first_name='Edgar', last_name='Mallory')
Ninja.objects.create(dojo_id=Dojo.objects.get(id=4), first_name='Jake', last_name='Jailbird')
Ninja.objects.create(dojo_id=Dojo.objects.get(id=4), first_name='Johnny', last_name='Bravo')

# Query: Create 3 ninjas that belong to the second dojo
Ninja.objects.create(dojo_id=Dojo.objects.get(id=5), first_name='Spongebob', last_name='Squarepants')
Ninja.objects.create(dojo_id=Dojo.objects.get(id=5), first_name='Sandy', last_name='Cheeks')
Ninja.objects.create(dojo_id=Dojo.objects.get(id=5), first_name='Patrick', last_name='Star')

# Query: Create 3 ninjas that belong to the third dojo
Ninja.objects.create(dojo_id=Dojo.objects.get(id=6), first_name='Poppin', last_name='Fresh')
Ninja.objects.create(dojo_id=Dojo.objects.get(id=6), first_name='Larry', last_name='Oats')
Ninja.objects.create(dojo_id=Dojo.objects.get(id=6), first_name='Joy', last_name='Butterworth')

# Query: Retrieve all the ninjas from the first dojo
Dojo.objects.first().ninjas.all()

# Query: Retrieve all the ninjas from the last dojo
Dojo.objects.last().ninjas.all()

# Query: Retrieve the last ninja's dojo
Ninja.objects.last().dojo_id

# Add a new text field called "desc" to your Dojo class

# Create and run the migration files to update the table in your database. If# needed, provide a default value of "old dojo"
# Query: Create a new dojo
Dojo.objects.create(name='Tulsa Dojo', city='Tulsa', state='OK', desc="The newest and coolest dojo")