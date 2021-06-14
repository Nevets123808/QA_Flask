from app import db, Users, Games

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty', last_name ='Tooty')
testgame = Games(name = 'Bonestorm', genre = 'Action', price = 34.95)
db.session.add(testuser)
db.session.add(testgame)
db.session.commit()