#!/bin/bash

# This script downloads a dataset from Kaggle and unzips it.

# Ensure there are at least two arguments
if [ "$#" -lt 2 ]; then
    echo "Usage: ./download_dataset.sh <kaggle command> ..."
    exit 1
fi

# Save the current directory
CURRENT_DIR=$(pwd)

# Set the download directory to '/kaggle/input'
DOWNLOAD_DIR="/kaggle/input"

# Navigate to the download directory and create it if it doesn't exist
mkdir -p $DOWNLOAD_DIR
cd $DOWNLOAD_DIR

# Execute Kaggle command
"$@"

# Extract the dataset name from the fifth argument
NAME=$(basename ${5})

# Unzip and remove the zip file
ZIP_FILE="${NAME}.zip"
if [ -f "$ZIP_FILE" ]; then
    unzip "$ZIP_FILE" -d $NAME
    rm "$ZIP_FILE"
fi

# Return to the original directory
cd $CURRENT_DIR
