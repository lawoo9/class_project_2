from Flask import Flask
from sqlalchemy import create_engine
from models.models import *
from models.models import ChlamydiaGonorrhea, CongenitalSyphilis, Base,  HepatitisBinfected 
app = Flask(__name__) 
app.secret_Key = 'somessecretekeythatonlyishouldknow'
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+mysqlconnector://root:course123@localhost/sti data' 
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
Base.metadata.create_all(engine)
@app.route('/')
def index():
    return 'Hello World'
if __name__ == '__main__':
 app.run(debug=True)