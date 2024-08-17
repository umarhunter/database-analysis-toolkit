import argparse
import logging
import yaml
import pandas as pd

from util import util

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
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
    parser.add_argument('--geospatial_analysis', type=str, choices=['True', 'False'], help='Enable or disable geospatial analysis')
    parser.add_argument('--geospatial_columns', type=str, nargs='+', help='Columns to apply geospatial analysis')
    parser.add_argument('--geospatial_threshold', type=float, help='Threshold for geospatial analysis')
    parser.add_argument('--fuzzy_matching', type=str, choices=['True', 'False'], help='Enable or disable fuzzy matching')
    parser.add_argument('--fuzzy_threshold', type=float, help='Threshold for fuzzy matching')
    parser.add_argument('--fuzzy_columns', type=str, nargs='+', help='Columns to apply fuzzy matching')
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

    input_file = config['input_file']
    output_file = config['output_file']
    sort_by_columns = config['sort_by_columns']
    geospatial_analysis = config['geospatial_analysis']
    geospatial_columns = config['geospatial_columns']
    geospatial_threshold = config['geospatial_threshold']
    fuzzy_matching = config['fuzzy_matching']
    fuzzy_threshold = config['fuzzy_threshold']
    fuzzy_columns = config['fuzzy_columns']

    print("Configuration:")
    print(config)

    df = pd.read_csv(input_file)
    logging.info(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns")


if __name__ == "__main__":
    main()
