#!/bin/bash

if [ -d "../reports" ]; then
    echo "Cleaning CSV reports..."

    rm ../reports/*.csv

    if [ $? -eq 0 ]; then
        echo "All CSV files were deleted successfully."
    else
        echo "No CSV to delete."
    fi
else
    echo "Directory 'reports' was not found."
fi