#!/bin/bash
set -e

# Install CMake locally (Render doesn't support sudo)
mkdir -p $HOME/cmake
cd $HOME/cmake
curl -LO https://github.com/Kitware/CMake/releases/download/v3.27.9/cmake-3.27.9-linux-x86_64.tar.gz
tar -xzf cmake-3.27.9-linux-x86_64.tar.gz
export PATH=$HOME/cmake/cmake-3.27.9-linux-x86_64/bin:$PATH

# Back to project root
cd $RENDER_PROJECT_ROOT

# Clone and build liboqs
git clone --recursive https://github.com/open-quantum-safe/liboqs.git
cd liboqs
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local ..
make -j$(nproc)
make install
cd ../..

# Set environment for oqs-python build
export CMAKE_PREFIX_PATH=$HOME/.local
export LIBRARY_PATH=$HOME/.local/lib
export LD_LIBRARY_PATH=$HOME/.local/lib
export CPATH=$HOME/.local/include

# Install liboqs-python
git clone https://github.com/open-quantum-safe/liboqs-python.git
cd liboqs-python
python3 -m pip install .
cd ..

# Install other Python dependencies
pip install -r requirements.txt
