import os

import pyrebase
import dotenv

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


def upload_data(parameterType: str, parameter: float) -> None:
    """
    This function uploads the data to the firebase database

    Args:
    parameterType (str): The type of the parameter
    parameter (float): The value of the parameter
    """
    if parameterType == "voltage":
        try:
            db.child("voltage").push(parameter)
            print("Data uploaded successfully")
        except:
            raise ValueError("There was an error uploading the data")
    elif parameterType == "raw_value":
        try:
            db.child("raw_value").push(parameter)
            print("Data uploaded successfully")
        except:
            raise ValueError("There was an error uploading the data")
    else:
        raise ValueError("Invalid parameter type")

def download_data(parameterType: str) -> None:
    """
    This function downloads the data from the firebase database and saves it to an comma separated value file

    Args:
        parameterType (str): The type of the parameter to download

    Returns:
        None
    """

    if parameterType == "voltage":
        try:
            voltage_data = db.child("voltage").get()
            with open("voltage_data.csv", "w") as file:
                file.write("voltage\n")
                for data in voltage_data.each():
                    file.write(f"{data.val()},")
            print("Data downloaded successfully")
        except:
            raise ValueError("There was an error downloading the data")
    elif parameterType == "raw_value":
        try:
            raw_value_data = db.child("raw_value").get()
            with open("raw_value_data.csv", "w") as file:
                file.write("raw_value\n")
                for data in raw_value_data.each():
                    file.write(f"{data.val()},")
            print("Data downloaded successfully")
        except:
            raise ValueError("There was an error downloading the data")
    else:
        raise ValueError("Invalid parameter type")
