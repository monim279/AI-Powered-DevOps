# Automation Scripts for DevOps

This repository contains Python scripts designed to automate the generation of configuration files for DevOps tasks. These scripts leverage the Llama model to produce configurations with best practices and provide additional guidance for setup.

## Scripts Overview

### [generate_dockerfile.py](day-3/local-llms-ollama/generate_dockerfile.py)

- **Purpose:** Automatically generates Dockerfiles for various programming languages using best practices.
- **Features:**
  - Generates Dockerfiles with essential components such as base image, dependencies, working directory, source code addition, and application execution.
  - Supports multiple programming languages.
- **Usage:**
  1. Ensure Python and the necessary dependencies are installed.
  2. Run the script:
     ```bash
     python day-3/local-llms-ollama/generate_dockerfile.py
     ```
  3. Enter the programming language for which you need a Dockerfile.
  4. The script outputs a Dockerfile tailored to the specified language.

### [generate_gcp_terraform.py](terraform/generate_gcp_terraform.py)

- **Purpose:** Generates Terraform configuration files for GCP resources with best practices and provides unique setup tips.
- **Features:**
  - Supports generating configurations for various GCP resources such as VMs, security groups, and VPCs.
  - Provides unique setup tips based on the generated configuration.
- **Usage:**
  1. Ensure Python, the Ollama library, Terraform, and gcloud CLI tools are installed.
  2. Run the script:
     ```bash
     python terraform/generate_gcp_terraform.py
     ```
  3. Enter the type of GCP resource you want to generate a configuration for (e.g., vm, security group, vpc).
  4. The script outputs the Terraform configuration and provides unique tips for setting up the resource.

## Requirements

- Python 3.x
- Ollama library
- Terraform and gcloud CLI tools installed

## Notes

- Ensure you have the necessary permissions and IAM roles to create and manage GCP resources.
- Review the generated configurations and customize them as needed for your specific use case.
- The scripts are designed to streamline DevOps workflows by automating repetitive tasks and ensuring adherence to best practices.
