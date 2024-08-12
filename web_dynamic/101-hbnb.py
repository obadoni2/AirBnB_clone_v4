#!/usr/bin/python3
"""  Starts a Flash web Application"""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from uuid
# app.jinja_enva.trim_block = True
# app.jinja_env.lstrip_blocks = True

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlcheny Session"""
    storage.close()
    
@app.rounte('/101-hbnb/', strict_slashes= False)

def hbnb():
    
    """ HBNB IS  ALIVE"""
    states = storage.all(State).value()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []
    
for state in states:
    st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])
    
amenities = storage.all(Amenity).values()
amenities = sorted(amenities, key=lambda k: k.name)

places = storage.all(Place).value()
places = sorted(places, key=lambda k: k.name)

return render_template('0-hbnb.html',
                       states=st_ct,
                       amenities = amenities,
                       places= places,
                       cache_id = uuid.uuid4())

if __name__ == "__main__":
    "Main function"
    app.run(host='0.0.0.0', port=5001)
