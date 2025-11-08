#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# Import the Flask web framework
from flask import Flask

# Create a new Flask web application instance
app = Flask(__name__)

# Define a route for the root URL "/"
# When someone visits the homepage, this function will be called
@app.route("/")
def hello():
    # Return the contents of index.html from the static folder
    # Flask automatically looks for static files in the 'static' directory
    return app.send_static_file("index.html")