#!/usr/bin/env bash
set -e

# System dependencies
apt-get update && apt-get install -y cmake build-essential git

# Clone and build liboqs
git clone --depth=1 https://github.com/open-quantum-safe/liboqs
cmake -S liboqs -B liboqs/build -DBUILD_SHARED_LIBS=ON
cmake --build liboqs/build --target install

# Set path for dynamic linking
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export OQS_INSTALL_PATH=/usr/local

# Install Python deps
pip install --upgrade pip
pip install -r requirements.txt

# Install liboqs-python from GitHub
pip install git+https://github.com/open-quantum-safe/liboqs-python
