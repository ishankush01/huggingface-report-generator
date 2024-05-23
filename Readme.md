# Hugging Face Report Generator

This repository contains a Python script and Docker setup to generate a report of the top 10 downloaded models from the Hugging Face model hub.

## Instructions

### Clone the Repository

```sh
git clone https://github.com/ishankush01/huggingface-report-generator.git
cd huggingface-report-generator
```

### Build the Docker Image

```sh
docker build -t huggingface-report-generator .
```

### Run the Docker Container

```sh
docker run --rm -v /$(pwd):/app huggingface-report-generator
```

### Check the Generated Report

After the container stops, you should see a file named `top_models_report.txt` in your current directory. This file contains the list of the top 10 downloaded models from Hugging Face.

