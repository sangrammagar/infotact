CREATE TABLE bikes (
  bike_id TEXT PRIMARY KEY,
  status TEXT,
  last_serviced_date DATE
);

CREATE TABLE rides (
  ride_id SERIAL PRIMARY KEY,
  bike_id TEXT,
  ride_duration INTEGER,
  distance_km FLOAT,
  avg_vibration FLOAT,
  ride_date DATE
);
