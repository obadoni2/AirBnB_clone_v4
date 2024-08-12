#!/usr/bin/python3
""" STARTS a flash web APPlication"""
from models import storage
from models.state import state
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(_name_)
#app.jinja_env. trim_block = true
#app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext

def close_db(error):
    """REMOVE the current SQLAlChemy"""
    storage.close()
    
    
    @app.route('/0-hbnb/', strict_slashes=False)
    def hbnb():
        """HBNB is alivel"""
        states = storage.all(State). value()
        states = sorted(states, key= lambda k: k.name)
        st_ct  = []
        
        for state in states:
            st_ct.append([state, sorted(state.cities, key=lambda k: k.name)]) 
            
        ammenities = storage.all(Amenity).value()
        amenities = sorted(amenities)
        
        places= storage.all(Place).value()
        place = sorted(places, key =lambda k:k.name)
        
        return render_template('0-hbnb.html',
                               states=st_ct,
                               amenities=amenities,
                               places=places,
                               cache_id=uuid.uuid4())
        
    if __name__ == "__main__":
        """ main Function"""
    app.run(host='0.0.0.0', port=5001)
                               
        
        
        
