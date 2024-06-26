
# Database Analysis

## Overview

Database Consistency Checker is a Python Jupyter notebook designed to ensure data integrity by identifying inconsistencies between two flat files. One of these files serves as the database for an organization or corporation. The tool logs any inconsistencies found, facilitating easy identification and correction of data issues.

## Features

- **Data Integrity Checks**: Compares two flat files and logs inconsistencies.
- **Detailed Logging**: Generates a comprehensive log of all inconsistencies found.
- **User-Friendly Interface**: Easy-to-use Jupyter notebook interface.
- **Customizable**: Easily adaptable for different data formats and validation rules.

## Installation

Follow these steps to set up your environment and run the Jupyter notebook:

### Prerequisites

- Python 3.7 or later
- Jupyter Notebook
- Virtual Environment (recommended)

### Setting Up the Environment

1. **Clone the Repository**

    ```bash
    git clone https://github.com/umarhunter/database_analysis.git
    ```

2. **Enter the Repo**
   ```bash
   cd database-consistency-checker
   ```
   
3. **Create a Virtual Environment**

    It's recommended to use a virtual environment to manage dependencies. 

    ```bash
    python3 -m venv env
    ```

4. **Activate the Virtual Environment**

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

5. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Setting Up Jupyter

1. **Install Jupyter**

    If you don't already have Jupyter installed, you can install it using pip:

    ```bash
    pip install notebook
    ```

2. **Start Jupyter Notebook**

    Navigate to the project directory and start Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

3. **Open the Notebook**

    In the Jupyter interface, open `Database_Consistency_Checker.ipynb`.

## Usage

1. **Prepare Your Files**

    Ensure you have the two flat files ready. One file should be the reference database, and the other should be the data you want to compare against the database.

2. **Run the Notebook**

    Follow the instructions within the notebook to load your files and execute the data consistency checks.

3. **Review the Logs**

    The notebook will output a log file detailing any inconsistencies found between the two files. Review this log to identify and correct data issues.

## Project Structure

```
database-consistency-checker/
│
├── Database_Consistency_Checker.ipynb  # Main Jupyter notebook
├── requirements.txt                   # Project dependencies
├── data/                              # Directory to store your flat files
│   ├── reference_file.csv             # Example reference file
│   └── target_file.csv                # Example target file
└── logs/                              # Directory to store log files
```

## Author

This project is created and maintained by Umarhunter.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
