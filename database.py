from sqlalchemy import create_engine,text
from config_secret import DB_URL

# Create the engine
engine = create_engine(DB_URL)

def load_items_from_menu():
    with engine.connect() as connection:
        result=connection.execute(text("select * from menu limit 10;"))
        menu_list=[]
        for row in result.all():
            menu_list.append(row._asdict())
        return menu_list
def load_jobs_from_careers():
    with engine.connect() as connection:
        result=connection.execute(text("select * from careers;"))
        job_list=[]
        for row in result.all():
            job_list.append(row._asdict())
        return job_list
def load_job_from_db(id):
    with engine.connect() as connection:
        result = connection.execute(text("select * from careers where job_id = :val"), {'val': id})
        rows=result.all()
        if len(rows)==0:
            return None
        else:
            return rows[0]._asdict()
    
    