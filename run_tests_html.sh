#!/bin/bash

# Ensure script fails if any command fails
set -e

# Create reports directory if it doesn't exist
mkdir -p reports

# Run pytest with proper PYTHONPATH and HTML report
PYTHONPATH=$(pwd) pytest tests/ --html=reports/report.html --self-contained-html -v
