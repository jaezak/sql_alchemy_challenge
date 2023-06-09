import numpy as np

import datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from sqlalchemy.ext.declarative import declarative_base


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
con = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# Import the dependencies.
from sqlalchemy import create_engine, inspect
from sqlalchemy import Column, Integer, String, Float, Date

from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarating class definitions to produce Table objects
Base = declarative_base()
inspector = inspect(engine)
inspector.get_table_names()

#Set class variables
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

#Save references to the table. Join measurement and station keys.
# View all of the classes that automap found
Base.classes.keys()
class measure(Base):
    __tablename__ = "measurement"
    extend_existing=True
    id = Column(Integer, primary_key=True)
    station = Column(String)
    date = Column(Date)
    prcp = Column(Float)
    tobs = Column(Float)

# Get the table names using `inspect()`.
inspector = inspect(engine)
inspector.get_table_names()


#----------------------------#
# 1. Start at the homepage. List all the available routes.
from flask import Flask, jsonify
# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def home():
    return "Hello there!"

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/api/v1.0/stations<br/>"
        f"//api/v1.0/tobs<br/>"
        f"/api/api/v1.0/<start<br/>"
        f"/api/api/v1.0/<start>/<end><br/>")


#----------------------------#
# 2. /api/v1.0/precipitation
# Convert the query results from your precipitation analysis
# (i.e. retrieve only the last 12 months of data) to a dictionary 
@app.route("/api/v1.0/precipitation>")
def precipitation_data():
    most_recent = session.query(Measurement.date).order_by((Measurement.date)).first()
    add_year = datetime.datetime.strptime("2017-08-23", "%Y-%m-%d") + datetime.timedelta(days=365)
    scores = session.query(Measurement.date, func.avg(Measurement.prcp)).\
        filter(Measurement.date >= add_year).\
        group_by(Measurement.date).all()


    precip_data = [
        {date: prcp for date, prcp in scores}]

    return jsonify(precip_data)

#----------------------------#
# 3. /api/v1.0/stations
#station_list = [{'Stations': station_list}]
#def stations():
    #"""Return the stations data as json"""

    #return jsonify(station_list)

#----------------------------#
# 4. /api/v1.0/tobs
#Query the dates and temperature observations of the most-active station for the previous year of data.
#Return a JSON list of temperature observations for the previous year.
@app.route("/api/api/v1.0/stations<")
station_list = session.query(measurement.station, func.count(measurement.station)).\
    group_by(measurement.station).\
    order_by(func.count(measurement.station).desc()).all()

#----------------------------#
# 5. 
#Return a JSON list of :
    # the minimum temperature, the average temperature, and the maximum temperature
    #  for a specified start or start-end range.

# For a specified start, calculate:
    # TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

# For a specified start date and end date, calculate:
        # TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
@app.route("/api/v1.0/<start>")
@app.route("api/v1.0/<start>/<end>")
def precipitation_data():
    temp_list = session.query(measurement.station, func.min(measurement.tobs), func.max(measurement.tobs),
                              func.avg(measurement.tobs)).filter(measurement.station == most_active[0]).all()
    temp_data = [{


}]



if __name__ == '__main__':
    app.run(debug=True)

