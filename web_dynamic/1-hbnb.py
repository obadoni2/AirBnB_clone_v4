#!/usr/bin/python3
""" Sarts a Flash web_search"""
from models import storag 
from models.state import State
from models.amenity import Amenity
from models.place import Place
from os import _environ
from flask import flask, render_template
import uuid
app = Flask(__name__)
## app.jinja_env.trim_block = True
# app.jinja_enva.lstrip_block = True

@app. teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlChemy session"""
    storage.close()
    
    
    @app.route('/1-hbnb/', strict_slashes=False)
    def hbnb():
        """HBNB is aliva"""
        
        states = storage.all(State).value()
        states = sorted(states, key=lambda k: k.name)
        st_ct = []
        
        for state in states:
            st_ct.append([state, sorted(state.cities, key= lambda k: k.name)])
            
        amenities = storage.all(Amenity). valued()
        amenities = sorted(amenities, key= lambda k: k.name)
        
        places = storage.all(Places).value()
        places = sorted(places, key=lambda k: k.name)
        
        return render_template('0-hbnb.html',
                               states = st_ct,
                               amenities = amenities,
                               places= places,
                               cache_id = uuid.uud4)
        
        
    if __name__ == "__main__":
        """main function"""
    app.run(host='0.0.0.0', port=5000)









