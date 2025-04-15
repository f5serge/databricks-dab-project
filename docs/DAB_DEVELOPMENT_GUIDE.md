# Databricks Asset Bundle (DAB) Development Guide

This guide provides detailed instructions for developing and deploying the Databricks Asset Bundle project.

## Prerequisites

- Databricks CLI v0.244 or later
- Python 3.11+
- Access to the Databricks workspace
- Git

## Getting Started

### Install Databricks CLI

```bash
pip install databricks-cli
```

### Authenticate with Databricks

```bash
databricks configure
```

You'll be prompted to enter:
- Databricks host (e.g., https://adb-xxxxxxxxxx.xx.azuredatabricks.net/)
- Authentication method (token, Azure CLI, etc.)

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

## Project Structure Overview

- `databricks.yml`: Main DAB configuration
- `resources/`: Workflows and other resources
- `notebooks/`: Databricks notebooks
- `src/common/python_base_package/`: Common Python code

## Development Workflow

### 1. Understanding Databricks Asset Bundles

DAB provides a way to:
- Define resources (jobs, clusters, notebooks) as code
- Version control these resources
- Deploy them consistently across environments
- Share code between projects

### 2. Local Development

#### Python Package Development

1. Navigate to the Python package directory:
   ```bash
   cd src/common/python_base_package
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```

3. Install in development mode:
   ```bash
   pip install -e .
   ```

4. Make your changes to the package code

#### Testing Changes Locally

1. Write unit tests for your package code
2. Run the tests:
   ```bash
   # If using pytest (recommended)
   pytest
   ```

### 3. Notebook Development

Notebooks can be developed in:

1. **Databricks Workspace**: Create/modify notebooks in the Databricks UI, then download them to your local project
2. **Local IDE**: Create/modify notebooks locally, then use the CLI to upload them

```bash
# For local development, you can use Databricks Connect (separate setup required)
```

### 4. Deploying to Development

To deploy all changes to the development environment:

```bash
databricks bundle deploy --target dev
```

This will:
- Build and upload the Python package
- Upload notebooks
- Create/update jobs and other resources

### 5. Testing in Development

After deploying to development:

1. Run jobs manually to verify functionality:
   ```bash
   databricks bundle run sample_job
   ```

2. Check job execution logs in the Databricks workspace

### 6. Deploying to Production

When ready to deploy to production:

```bash
databricks bundle deploy --target prod
```

## Advanced Topics

### Environment Variables

Use environment variables for sensitive information:

```bash
export DATABRICKS_HOST=https://adb-xxxxxxx.xx.azuredatabricks.net
export DATABRICKS_TOKEN=dapi1234567890
```

### CI/CD Integration

For CI/CD pipelines (e.g., GitHub Actions, Azure DevOps):

1. Set up secrets/variables in your CI system
2. Create workflow files for automated deployment

Example GitHub Actions workflow:
```yaml
name: Deploy Databricks Assets

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install databricks-cli
      - name: Deploy to Development
        env:
          DATABRICKS_HOST: ${{ secrets.DATABRICKS_HOST }}
          DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN }}
        run: |
          databricks bundle deploy --target dev
```

### Working with Multiple Targets

You can define multiple deployment targets in `databricks.yml`:

```yaml
targets:
  dev:
    # Configuration for development
  test:
    # Configuration for testing
  prod:
    # Configuration for production
```

Deploy to a specific target:
```bash
databricks bundle deploy --target test
```

### Troubleshooting

1. **Validation Issues**:
   ```bash
   databricks bundle validate
   ```

2. **Configuration Issues**:
   Check your `databricks.yml` file for syntax errors

3. **Deployment Failures**:
   - Check CLI output for errors
   - Look at workspace logs
   - Verify permissions

## Best Practices

1. **Version Control**: Keep all code, configurations, and notebooks in version control
2. **Modular Design**: Structure the Python package in a modular way
3. **Documentation**: Document all functions, modules, and workflows
4. **Testing**: Write tests for all critical code paths
5. **CI/CD**: Automate deployments
6. **Multi-Environment**: Use the same code across all environments
7. **Secret Management**: Never store secrets in code
8. **Code Review**: Review all changes before deployment to production

## Resources

- [Databricks CLI Documentation](https://docs.databricks.com/dev-tools/cli/index.html)
- [Databricks Asset Bundles Documentation](https://docs.databricks.com/dev-tools/bundles/index.html)
- [Databricks Connect](https://docs.databricks.com/dev-tools/databricks-connect.html) 