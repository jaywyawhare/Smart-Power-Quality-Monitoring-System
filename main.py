import os
import argparse
from src.firebase import upload_data, download_data
from src.input import get_values
from src.helper import load_data, adjust_negative_values, smooth_data, generate_graph

while True:
    parser = argparse.ArgumentParser(description="Smart energy meter")
    parser.add_argument(
        "-u",
        "--upload",
        action="store",
        dest="parameter",
        help="Upload data to the firebase database",
    )
    parser.add_argument(
        "-d",
        "--download",
        action="store_true",
        help="Download data from the firebase database",
    )
    parser.add_argument(
        "-p",
        "--parameter",
        action="store",
        dest="parameter",
        help="The parameter to upload to the firebase database",
    )
    parser.add_argument(
        "-f",
        "--file",
        action="store",
        dest="file_path",
        help="The file path to download the data to",
    )
    # downloaded data will be then loaded and preprocess which include adjust negative values and smooth data
    # then user can generate graph of the data
    parser.add_argument(
        "-g",
        "--graph",
        action="store",
        dest="file_path",
        help="Generate graph of the downloaded data",
    )
    parser.add_argument("-s", "--smooth", action="store_true", help="Smooth the data")
    parser.add_argument(
        "-a", "--adjust", action="store_true", help="Adjust negative values in the data"
    )

    args = parser.parse_args()

    if args.upload:
        if args.parameter:
            upload_data(args.parameter, get_values(args.parameter))
        else:
            raise ValueError("The parameter is required")
    elif args.download:
        if args.parameter:
            download_data(args.parameter)
        else:
            raise ValueError("The parameter is required")
    else:
        raise ValueError("Invalid command")

    if args.graph:
        if args.file_path:
            data = load_data(args.file_path)
            if args.adjust:
                data = adjust_negative_values(data)
            if args.smooth:
                data = smooth_data(data)
            generate_graph(data)

    os.system("clear")
    print("Data processed successfully")
    break
