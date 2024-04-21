#!/usr/bin/python3

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)

#Define the route for '/states' and specify
#   strict_slashes=False to handle trailing slashes
@app.route("/states", strict_slashes=False)
def states():
    """Display an HTML page with a list of all States.

    States are sorted by name.
    """
    #Fetch all state objects from the
    #   storage (Filestorage or DBStorage)
    state = storage.all("State")

    #Render the "9-states.html"'state=states)
