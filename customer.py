from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models import Customer

# Here we create our connection
def create_connection():
    engine = create_engine('sqlite:///test.db')

    # Here we created our table
    Customer.__table__.create(engine,checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    print('Connected')
    return session

# Two methods for inserting data

    #1st insert data individually
def insert_data(session=None):
    data ={"id":122, "name":"Honey","email":"honey@gmail.com"}
    data_obj=Customer(**data)
    session.add(data_obj)
    print('DATA ADDED SUCESSFULLY')
    session.commit()

    #2nd insert many data at a same time
def insert_many(sessioon=None):
    data =[{"id":122, "name":"Honey","email":"honey@gmail.com"},
           {"id":123, "name":"Gurmeet","email":"gur@gmail.com"}
    ]
    session.bulk_insert_mappings(mapper=Customer,mappings=data)
    print('DATA ADDED SUCESSFULLY')
    session.commit()

# This is how we can see our data
def fetch(session = None):
    users = session.query(Customer).all()
    for i in users:
	    print(i.id,i.name,i.email)

# This is the process of updating data 
def update_data(session = None):
   user_to_update = session.query(Customer).filter_by(id = 101).first()
   user_to_update.name = "Pulsar"
   print('DATA UPDATED SUCESSFULLY')
   session.commit()

# This is the process of deleting data
def delete_data(session = None):
    user_to_delete = session.query(Customer).filter_by(id = 104).first()
    session.delete(user_to_delete)
    print('DATA DELETED SUCESSFULLY')
    session.commit()
    
if __name__=="__main__":
    # Here we call our function
    session=create_connection()
    # insert_data(session)
    # insert_many(session)
    # update_data(session)
    # delete_data(session)
    # fetch(session)