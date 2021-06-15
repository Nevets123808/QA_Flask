from app import db, Customers, Products, Sales
db.create_all()

Jimmy = Customers(name = 'Jimmy')
db.session.add(Jimmy)
db.session.commit()

BS = Products(name = 'BoneStorm', price =33)
db.session.add(BS)
db.session.commit()

sale = Sales(buyer = Jimmy, item = BS)
db.session.add(sale)
db.session.commit()

