# Retail PySpark Project

## Overview

This project is a PySpark-based data processing application designed for retail analytics. It demonstrates how to build scalable data pipelines using Apache Spark for processing large retail datasets. The application reads customer and order data, performs transformations such as filtering closed orders, joining datasets, and aggregating results by state.

## Features

- **Data Ingestion**: Reads CSV files for customers and orders with predefined schemas
- **Data Transformation**: Filters closed orders, joins customer and order data
- **Data Aggregation**: Counts orders by state
- **Environment Configuration**: Supports multiple environments (LOCAL, TEST, PROD) with different configurations
- **Logging**: Integrated Log4j logging for Spark applications
- **Testing**: Comprehensive unit tests using pytest with Spark fixtures
- **CI/CD**: Jenkins pipeline for automated testing, packaging, and deployment

## Prerequisites

- Python 3.11.2 or higher
- Java 8 or higher (required for PySpark)
- Apache Spark (automatically handled via PySpark dependency)
- Pipenv for dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd retail_pyspark_project
   ```

2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

## Configuration

The project uses configuration files located in the `configs/` directory:

- `application.conf`: Contains file paths for data sources
- `pyspark.conf`: Contains Spark configuration settings

### Environment Configurations

The application supports three environments:

- **LOCAL**: For local development with local Spark master
- **TEST**: For testing with distributed Spark settings
- **PROD**: For production deployment

Each environment has specific configurations in the conf files.

## Usage

### Running the Application

To run the main application, specify the environment as a command-line argument:

```bash
python application_main.py LOCAL
```

Replace `LOCAL` with `TEST` or `PROD` based on your environment.

### Expected Output

The application will:
1. Create a Spark session
2. Read customers and orders data
3. Filter orders with status 'CLOSED'
4. Join orders with customer data on customer_id
5. Aggregate and count orders by state
6. Display the results

## Testing

The project includes comprehensive tests using pytest.

### Running Tests

```bash
pipenv run pytest
```

### Test Structure

- `retail_proj_test.py`: Contains test cases for data reading, filtering, and aggregation
- `conftest.py`: Provides pytest fixtures for Spark session and expected results
- Tests validate data counts, transformations, and configuration loading

### Test Markers

- `transformation`: Marks tests related to data transformations
- `slow`: For slow-running tests
- `latest`: For testing the latest features

## CI/CD

The project includes a Jenkins pipeline (`jenkinsfile`) that:

1. Sets up a Python virtual environment
2. Installs dependencies via Pipenv
3. Runs the test suite
4. Packages the application (excluding virtual environment)
5. Prepares for deployment

### Jenkins Setup Requirements

- Java installed at `/opt/bitnami/java`
- Credentials stored as 'labcreds'

## Project Structure

```
retail_pyspark_project/
├── application_main.py          # Main application entry point
├── conftest.py                  # Pytest fixtures
├── jenkinsfile                  # CI/CD pipeline configuration
├── log4j.properties             # Logging configuration
├── Pipfile                      # Dependency management
├── pytest.ini                   # Pytest configuration
├── retail_proj_test.py          # Test suite
├── configs/
│   ├── application.conf         # Application configurations
│   └── pyspark.conf             # PySpark configurations
├── data/
│   ├── customers.csv            # Sample customer data
│   ├── orders.csv               # Sample order data
│   └── expected_results/        # Expected test results
└── lib/
    ├── ConfigReader.py          # Configuration reading utilities
    ├── DataManipulation.py      # Data transformation functions
    ├── DataReader.py            # Data ingestion functions
    ├── logger.py                # Logging utilities
    └── Utils.py                 # Spark session utilities
```

## Key Components

### Core Modules

- **DataReader.py**: Handles reading CSV files with proper schemas
- **DataManipulation.py**: Contains data transformation logic
- **Utils.py**: Manages Spark session creation
- **ConfigReader.py**: Loads configuration from files
- **logger.py**: Provides logging functionality using Log4j

### Data Flow

1. **Ingestion**: Read customers and orders CSV files
2. **Filtering**: Remove orders that are not closed
3. **Joining**: Combine order and customer data
4. **Aggregation**: Count orders per state
5. **Output**: Display aggregated results

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues, please open an issue in the repository or contact the development team.