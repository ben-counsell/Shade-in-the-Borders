from flask import Blueprint, render_template, request, redirect
from models.fabric import Fabric
from models.frame import Frame
from models.order import Order
from app import db

fabric_blueprint = Blueprint('fabric', __name__)
frame_blueprint = Blueprint('frame', __name__)
order_blueprint = Blueprint('order', __name__)

