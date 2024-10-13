from sqlalchemy import create_engine,text
from config_secret import DB_URL

# Create the engine
engine = create_engine(DB_URL)

# Use the with clause to manage the connection
with engine.connect() as connection:
    # Check if the connection was successful
    if connection:
        print("connection was successful")
        result=connection.execute(text("select * from menu linit 10;"))
        print(result.all())
    else:
        print("Connection failed")

# No need to explicitly close the connection, it's handled by the with clause
