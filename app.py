from flask import Flask, render_template
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

from controllers.lampshade_controller import fabric_blueprint, frame_blueprint, order_blueprint

app.register_blueprint(fabric_blueprint)
app.register_blueprint(frame_blueprint)
app.register_blueprint(order_blueprint)

@app.route('/')
def home_page():
    return render_template('home.jinja')