import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.adafruit_ads1x15 import Mode

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.mode = Mode.CONTINUOUS
sample_rate = 860
ads.data_rate = sample_rate

channel = AnalogIn(ads, ADS.P0)


def get_values(param:str)->float:
    """
    Get the values from the sensor

    Args:
    param (str): The parameter to get the values for.

    Returns:
    float: The value of the parameter.
    """
    if param == 'voltage':
        return channel.voltage
    elif param == 'raw_value':
        return channel.value
    else:
        raise ValueError('Invalid parameter')