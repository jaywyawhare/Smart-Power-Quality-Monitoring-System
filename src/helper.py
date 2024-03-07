import concurrent.futures
import numpy as np
from scipy.signal import savgol_filter


def load_data(file_path:str)->np.ndarray:
    """
    This function loads the data from the file path provided

    Args:
        file_path (str): The path to the file

    Returns:
        np.ndarray: The data from the file
    """
    try:
        data = []
        with open(file_path, "r") as file:
            for line in file:
                data.append(float(line))
        return np.array(data)
    except:
        raise ValueError("There was an error loading the data")

def adjust_negative_values(data: np.ndarray) -> np.ndarray:
    """
    Adjust negative values in the data array.

    Args:
        data (np.ndarray): Input data array.

    Returns:
        np.ndarray: Adjusted data array.
    """
    
    adjusted_data = data.copy()
    zero_crossings = [(data[i-1] * data[i]) <= 0 for i in range(1, len(data))]
    zero_crossing_indices = [i for i, is_crossing in enumerate(zero_crossings) if is_crossing]

    peak_value = 0

    for i in range(1, len(zero_crossing_indices)):
        cycle = adjusted_data[zero_crossing_indices[i-1]:zero_crossing_indices[i]]

        if max(cycle) > peak_value:
            peak_value = max(cycle)

        min_value = min(cycle)

        if abs(min_value) > 0.25:
            for j in range(zero_crossing_indices[i-1], zero_crossing_indices[i]):
                if adjusted_data[j] < 0:
                    adjusted_data[j] = adjusted_data[j] * 3.33 * peak_value

    return adjusted_data

def smooth_data(data: np.ndarray, window_length: int = 11, polyorder: int = 3) -> np.ndarray:
    """
    Smooth the data using the Savitzky-Golay filter.

    Args:
        data (np.ndarray): Input data array.
        window_length (int): Length of the filter window.
        polyorder (int): Order of the polynomial used to fit the samples.

    Returns:
        np.ndarray: Smoothed data array.
    """
    return savgol_filter(data, window_length, polyorder)

def generate_graph(data: np.ndarray, title: str = "Data", x_label: str = "Time", y_label: str = "Value") -> None:
    """
    Generate a graph of the data.

    Args:
        data (np.ndarray): Data to graph.
        title (str): Title of the graph.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.

    Returns:
        None
    """
    import matplotlib.pyplot as plt

    plt.plot(data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.show()