import argparse
import logging
import yaml

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
    parser.add_argument('--log_level', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='Logging level')
    parser.add_argument('--sort_by_columns', type=str, nargs='+', help='Columns to sort by')
    parser.add_argument('--geospatial_analysis', type=str, choices=['True', 'False'], help='Enable or disable geospatial analysis')
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
    if args.log_level:
        config['log_level'] = args.log_level
    if args.sort_by_columns:
        config['sort_by_columns'] = args.sort_by_columns
    if args.geospatial_analysis:
        config['geospatial_analysis'] = args.geospatial_analysis
    if args.fuzzy_matching:
        config['fuzzy_matching'] = args.fuzzy_matching
    if args.fuzzy_threshold:
        config['fuzzy_threshold'] = args.fuzzy_threshold
    if args.fuzzy_columns:
        config['fuzzy_columns'] = args.fuzzy_columns

    print("Configuration:")
    print(config)


if __name__ == "__main__":
    main()
