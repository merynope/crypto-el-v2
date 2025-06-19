#!/usr/bin/env bash

# Exit on error
set -e

# Install system dependencies
apt-get update && apt-get install -y cmake build-essential git

# Build liboqs
git clone --depth=1 https://github.com/open-quantum-safe/liboqs
cmake -S liboqs -B liboqs/build -DBUILD_SHARED_LIBS=ON
cmake --build liboqs/build --target install

# Set environment so liboqs-python finds liboqs
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export OQS_INSTALL_PATH=/usr/local

# Install Python dependencies
pip install --upgrade pip
pip install pycryptodome streamlit
pip install git+https://github.com/open-quantum-safe/liboqs-python.git
