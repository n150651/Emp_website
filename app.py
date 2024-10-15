from flask import Flask,render_template
import database
app=Flask(__name__)

# def load_items_from_menu():
#     with engine.connect() as connection:
#         result=connection.execute(text("select * from menu limit 10 ;"))
#         menu_list=[]
#         for row in result.all():
#             menu_list.append(row._asdict())
#         return menu_list
        
    


@app.route('/')
def home():
    menu_items=database.load_items_from_menu()
    return render_template('home.html',menu=menu_items)
@app.route('/careers')
def careers():
    job_list=database.load_jobs_from_careers()
    return render_template('careers.html',job_list=job_list)
@app.route('/careers/<job_id>')
def job_show(job_id):
    job=database.load_job_from_db(job_id)
    return render_template('job_desc.html',job=job)
    
    

if __name__=='__main__':
    app.run(debug=True)