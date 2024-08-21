import argparse
import logging
import yaml
import pandas as pd

from util import util
from modules.data_loader import load_data
from modules.geospatial_analysis import perform_geospatial_analysis
from modules.fuzzy_matching import perform_fuzzy_matching

# We can use the logging module to log messages to a file and/or the console
logging.basicConfig(
    level=logging.INFO,  # Set the minimum logging level (e.g., INFO, DEBUG, ERROR)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Set the logging format
    datefmt='%Y-%m-%d %H:%M:%S',  # Set the date format in log messages
    handlers=[
        logging.FileHandler("logs/logfile.log"),  # Log to a file named "logfile.log"
        logging.StreamHandler()  # Optional, for logging to the console
    ]
)


def load_config(config_file):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)


def parse_args():
    parser = argparse.ArgumentParser(description="Database Analysis Script")
    parser.add_argument('--config', type=str, default='config/config.yaml', help='Path to the config file')
    parser.add_argument('--input_file', type=str, help='Path to the input CSV file')
    parser.add_argument('--output_file', type=str, help='Path to the output file')
    parser.add_argument('--sort_by_columns', type=str, nargs='+', help='Columns to sort by')
    parser.add_argument('--geospatial_analysis', type=str, choices=['True', 'False'],
                        help='Enable or disable geospatial analysis')
    parser.add_argument('--geospatial_columns', type=str, nargs='+', help='Columns to apply geospatial analysis')
    parser.add_argument('--geospatial_threshold', type=float, help='Threshold for geospatial analysis')
    parser.add_argument('--fuzzy_matching', type=str, choices=['True', 'False'],
                        help='Enable or disable fuzzy matching')
    parser.add_argument('--fuzzy_threshold', type=float, help='Threshold for fuzzy matching')
    parser.add_argument('--fuzzy_columns', type=str, nargs='+', help='Columns to apply fuzzy matching')
    parser.add_argument('--fuzzy_matching_algorithm', type=str,
                        choices=['WRatio', 'ratio', 'partial_ratio', 'token_sort_ratio', 'semantic'],
                        help='Fuzzy matching algorithm to use')
    return parser.parse_args()


def main():
    args = parse_args()
    config = load_config(args.config)

    # Override config with command-line arguments if provided
    if args.input_file:
        config['input_file'] = args.input_file
    if args.output_file:
        config['output_file'] = args.output_file
    if args.sort_by_columns:
        config['sort_by_columns'] = args.sort_by_columns
    if args.geospatial_analysis:
        config['geospatial_analysis'] = args.geospatial_analysis
    if args.geospatial_columns:
        config['geospatial_columns'] = args.geospatial_columns
    if args.geospatial_threshold:
        config['geospatial_threshold'] = args.geospatial_threshold
    if args.fuzzy_matching:
        config['fuzzy_matching'] = args.fuzzy_matching
    if args.fuzzy_threshold:
        config['fuzzy_threshold'] = args.fuzzy_threshold
    if args.fuzzy_columns:
        config['fuzzy_columns'] = args.fuzzy_columns
    if args.fuzzy_matching_algorithm:
        config['fuzzy_matching_algorithm'] = args.fuzzy_matching_algorithm

    input_file = config['input_file_name']
    output_file = config['output_file_name']
    sort_by_columns = config['sort_by_columns']
    geospatial_analysis = config['geospatial_analysis']
    geospatial_columns = config['geospatial_columns']
    geospatial_threshold = config['geospatial_threshold']
    fuzzy_matching = config['fuzzy_matching']
    fuzzy_threshold = config['fuzzy_threshold']
    fuzzy_columns = config['fuzzy_columns']
    fuzzy_algorithm = config['fuzzy_matching_algorithm']

    print("Configuration:")
    print(config)

    df = load_data(input_file)
    logging.info(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns")

    if geospatial_analysis:
        geo_df = perform_geospatial_analysis(df, sort_by_columns, geospatial_columns, geospatial_threshold)
        file_name = 'geospatial_analysis_' + output_file
        util.save_file(geo_df, file_name)
        logging.info(f"Successfully wrote {geo_df.shape[0]} rows to {file_name}")

    if fuzzy_matching:
        fuzz_df = perform_fuzzy_matching(df, sort_by_columns, fuzzy_columns, fuzzy_threshold, algorithm=fuzzy_algorithm)
        file_name = 'fuzzy_matching_' + output_file
        util.save_file(fuzz_df, file_name)
        logging.info(f"Successfully wrote {fuzz_df.shape[0]} rows to {file_name}")


if __name__ == "__main__":
    main()
