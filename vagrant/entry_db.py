from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

myFirstRestaurant = Restaurant(name = "Pizza Palace")

session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()

cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)

session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()

newEmployee = Employee(name = "Rebecca Allen")

session.add(newEmployee)
session.commit()
session.query(Employee).all()

rebeccaAddress = Address(street = "512 Sycamore Road", zip = "02001", employee = newEmployee)

session.add(rebeccaAddress)
session.commit()
session.query(Address).all()

firstResult = session.query(Restaurant).first()
firstResult.name

session.query(Restaurant).all()

items = session.query(MenuItem).all()
for item in items:
    print item.name

#### Quiz
employees = session.query(Employee).all()

# Print the name of each employee
for employee in employees:
    print employee.name

## CRUD Update
veggieBurger = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"

UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 10).one()
print UrbanVeggieBurger.price

UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()

for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()

for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"


#### Quiz

rebecca = session.query(Employee).filter_by(name = "Rebecca Allen").one()

RebeccasAddress = session.query(Address).filter_by(employee_id = rebecca.id).one()

RebeccasAddress.street = "281 Summer Circle"

RebeccasAddress.zip = "00189"

session.add(RebeccasAddress)
session.commit()

# CRUD Delete
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print spinach.restaurant.name

session.delete(spinach)
session.commit()
spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()


#### Quiz

mark = session.query(Employee).filter_by(name = "Mark Gonzalez").one()

session.delete(mark)
session.commit()

