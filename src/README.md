# DAB Databricks Common Package

This Python package provides common utilities, transformations, and ingestion modules for use across Databricks notebooks and workflows for the DAB project.

## Package Structure

```
common/
├── __init__.py
├── utils/              # Utility modules
│   ├── __init__.py
│   └── logging.py
├── transforms/         # Data transformation modules
│   └── __init__.py
└── ingestion/          # Data ingestion modules
    └── __init__.py
```

## Installation

The package is automatically built and installed by the Databricks Asset Bundle (DAB) system when deploying the project. However, for local development, you can install it in development mode:

```bash
# From the python_base_package directory
pip install -e .
```

## Usage

### In Databricks Notebooks

Import and use the package modules in your Databricks notebooks:

```python
from common.utils.logging import info, error

# Log information
info("Processing started")

# Log errors
try:
    # Your processing code
    pass
except Exception as e:
    error(f"Error during processing: {str(e)}")
    raise
```

### Local Development

For local development and testing, you can use the package the same way after installing it in your development environment.

## Module Documentation

### Utils

#### logging

Provides standardized logging functions that work both in Databricks and local environments:

- `info(message, extra=None)`: Log an informational message
- `error(message, extra=None)`: Log an error message

### Adding New Modules

To add a new module:

1. Create a new Python file in the appropriate directory (utils, transforms, or ingestion)
2. Import it in the corresponding `__init__.py` file if you want to make it directly importable
3. Add any necessary tests
4. Update this documentation

## Development Guidelines

1. **Documentation**: Document all functions with docstrings following Google or NumPy style
2. **Type Hints**: Use type hints for better IDE support and code clarity
3. **Error Handling**: Implement proper error handling and logging
4. **Testing**: Write unit tests for all functionality
5. **Code Style**: Follow PEP 8 guidelines
6. **Dependencies**: Minimize dependencies and document any new requirements

## Versioning

The package follows semantic versioning:

- **MAJOR**: Incompatible API changes
- **MINOR**: Added functionality in a backward-compatible manner
- **PATCH**: Backward-compatible bug fixes

## Building and Testing

To build the package manually:

```bash
# From the python_base_package directory
python setup.py bdist_wheel
```

This will create a wheel file in the `dist/` directory.

## License

For internal use only.
