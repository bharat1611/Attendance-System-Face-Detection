import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtimerecog-default-rtdb.firebaseio.com/"
})

# Will create Students Directory reference in RealTime DB
ref = db.reference('Students')

data = {
    "2001":
        {
            "name": "Bill Gates",
            "major": "Computer Science",
            "starting_year": 2001,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-01-05 22:09:00"
        }
}

for key, value in data.items():
    ref.child(key).set(value)