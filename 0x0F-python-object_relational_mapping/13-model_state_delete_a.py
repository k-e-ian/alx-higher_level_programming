#!/usr/bin/python3
'''
# Deletes all State objects with a name containing
# the letter a from the database hbtn_0e_6_usa.
# Usage: ./13-model_state_delete_a.py <mysql username> /
#                                     <mysql password> /
#                                     <database name>
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).filter(State.name.ilike("%a%")).all()

    for result in results:
        session.delete(result)

    session.commit()
