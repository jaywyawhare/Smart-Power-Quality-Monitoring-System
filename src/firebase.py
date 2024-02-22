import os

try:
    import pyrebase
    import dotenv
except:
    print("Install required libraries using pip install -r requirements.txt")

dotenv.load_dotenv()

config = {
    "apiKey": os.getenv("apiKey"),
    "authDomain": os.getenv("authDomain"),
    "databaseURL": os.getenv("databaseURL"),
    "storageBucket": os.getenv("storageBucket"),
    "messageSenderId": os.getenv("messageSenderId"),
    "appId": os.getenv("appId"),
    "measurementId": os.getenv("measurementId"),
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()


def upload_current_voltage(current: float, voltage: float) -> None:
    """
    This function uploads the current and voltage data to the firebase database

    Args:
    current (float): The current value to upload
    voltage (float): The voltage value to upload
    """
    data = {"current": current, "voltage": voltage}
    try:
        db.child("current_voltage_data").push(data)
        print("Data uploaded successfully.")
    except Exception as e:
        print(f"Error uploading data: {e}")
