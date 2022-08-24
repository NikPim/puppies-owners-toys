from models import db, Puppy, Owner, Toy

rufus = Puppy.query.filter_by(name = 'Rufus').first()
print(rufus.owner[0].name)
