from setuptools import find_packages, setup

# Load variables from the bundle
version = "0.1.0"  # Default version if not specified in the bundle

try:
    from databricks.sdk.runtime import spark  # More explicit import

    version = spark.conf.get("bundle.var.python_package_version")
except ImportError:  # Be explicit about what we're catching
    pass

setup(
    name="common",
    version=version,
    description="Common utilities for Databricks DAB project",
    author="Data Engineering Team",
    packages=find_packages(exclude=["tests"]),
    install_requires=["pyspark", "delta-spark"],
    zip_safe=False,
)
