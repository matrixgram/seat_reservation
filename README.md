# Python Backend
This package contains the application's backend, based on Python.

User -> Browser -> View (React) -> Controller(flask) -> Model -> Database(sqlite)

## Files:
- *ERD.jpg* is Entity Relationship Diagram.
- * sample_data.xlsx* is sample data for test our application.

## Run
For run project:
```bash
git clone  https://github.com/TheMerphin/TechLabs-Seat-Booking-Tool.git
cd TechLabs-Seat-Booking-Tool/python-backend
docker image build -t booking .
docker run  --rm -p 5000:5000  booking 
```
