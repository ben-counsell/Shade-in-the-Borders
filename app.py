from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/shade_in_the_borders'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from seed import seed
app.cli.add_command(seed)

from models.fabric import Fabric
from models.frame import Frame
from models.order import Order

@app.route('/')
def home_page():
    return 'hiya'