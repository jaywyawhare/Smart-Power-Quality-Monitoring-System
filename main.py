from src.firebase import upload_current_voltage
from src.input import calculate_current_voltage

while True:
    current, voltage = calculate_current_voltage()
    upload_current_voltage(current, voltage)