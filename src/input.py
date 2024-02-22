import time
import Adafruit_ADS1x15 as ADS
from Adafruit_IO import Client
import os
import math
import dotenv

dotenv.load_dotenv()

adc = ADS.ADS1115()
aio = Client(os.getenv("ADAFRUIT_IO_USERNAME"), os.getenv("ADAFRUIT_IO_KEY"))

GAIN = 1
samples = 10
precision = 4


def read_adc(channel: int) -> int:
    """
    This function reads the analog input from the specified channel and returns the absolute value of the reading

    Args:
    channel (int): The channel to read from

    Returns:
    int: The absolute value of the reading
    """
    return abs(adc.read_adc(channel, gain=GAIN))


def calculate_current_voltage() -> tuple:
    """
    This function calculates the current and voltage values from the analog inputs and returns them as a tuple

    Returns:
    tuple: The current and voltage values
    """
    maxIValue = maxVValue = 0
    datai = [read_adc(0) for _ in range(samples)]
    datav = [read_adc(1) for _ in range(samples)]

    for value in datai:
        if value > maxIValue:
            maxIValue = value

    for value in datav:
        if value > maxVValue:
            maxVValue = value
            print("New maxv value:", maxVValue)

    IrmsA0 = round(maxIValue / 2047 * 30, precision)
    ampsA0 = round(IrmsA0 / math.sqrt(2), precision)

    VrmsA1 = round(maxVValue * 1100 / 2047, precision)
    voltsA1 = round(VrmsA1 / math.sqrt(2), precision)

    return ampsA0, voltsA1
