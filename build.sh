#!/bin/bash

set -e  # Exit immediately if a command fails

# Variables
INSTALL_PREFIX="$HOME/.local"

# Step 1: Clone and build liboqs
git clone --recursive https://github.com/open-quantum-safe/liboqs.git
cd liboqs
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=$INSTALL_PREFIX ..
make -j$(nproc)
make install
cd ../..

# Step 2: Set environment variables so liboqs-python can find liboqs
export CMAKE_PREFIX_PATH=$INSTALL_PREFIX
export LIBRARY_PATH=$INSTALL_PREFIX/lib
export LD_LIBRARY_PATH=$INSTALL_PREFIX/lib
export CPATH=$INSTALL_PREFIX/include

# Step 3: Install liboqs-python
git clone https://github.com/open-quantum-safe/liboqs-python.git
cd liboqs-python
python3 -m pip install .
cd ..

# Step 4: Install remaining Python dependencies
pip install -r requirements.txt
