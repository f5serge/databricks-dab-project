# Databricks DAB Project

This is a Databricks Asset Bundle (DAB) project that includes workflows, notebooks, and a base Python package for data engineering on the Databricks platform.

## Project Structure

```
databricks-dab-project/
├── databricks.yml           # Main DAB configuration file
├── resources/               # DAB resources (workflows, etc.)
│   └── sample_workflow.yml  # Sample workflow definition
├── src/                     # Source code
│   ├── common/              # Reusable Python package shared across notebooks
│   │   ├── __init__.py
│   │   ├── utils/           # Utility modules
│   │   ├── transforms/      # Data transformation modules
│   │   └── ingestion/       # Data ingestion modules
│   └── setup.py             # Package setup file
├── notebooks/               # Databricks notebooks
│   ├── bronze/              # Bronze layer notebooks
│   ├── silver/              # Silver layer notebooks
│   └── gold/                # Gold layer notebooks
└── docs/                    # Documentation
```

## Setup Local Development Environment

1. Install the Databricks CLI v2

Follow the instructions in the [Databricks CLI documentation](https://docs.databricks.com/aws/en/dev-tools/cli/install)

```bash
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh

# Verify installation
databricks version
```

2. Configure Databricks CLI

```bash
databricks configure
```

3. Set up a Python development environment

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

# Install development requirements
cd src/common/python_base_package
pip install -e .
```

## Building and Deploying the Package

The base Python package is automatically built and deployed when you deploy the DAB project:

```bash
# Deploy to development environment
databricks bundle deploy --target dev

# Deploy to production environment
databricks bundle deploy --target prod
```

## Running Workflows

After deployment, you can run workflows using the Databricks CLI:

```bash
# Run the sample workflow
databricks bundle run sample_job
```

## Development Workflow

1. Make changes to the Python package or notebooks
2. Test your changes locally when possible
3. Deploy to the development environment
4. Run tests in the development environment
5. When ready, deploy to production

## Best Practices

- Keep the Python package modular and focused on reusable functionality
- Use proper logging in all notebooks and package code
- Document all functions and modules
- Follow a consistent notebook structure with clearly marked sections
- Use parameter widgets in notebooks for better flexibility
- Write unit tests for package code
- Use Delta tables for data storage
- Follow medallion architecture patterns (bronze/silver/gold)

## Troubleshooting

If you encounter issues with the package, check the logs in the Databricks workspace or try running individual notebooks for debugging.

For CLI issues, use `databricks bundle validate` to check your configuration files. 