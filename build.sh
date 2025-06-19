#!/bin/bash

set -e

# 1. Install dependencies
echo "🔧 Installing build dependencies..."
apt-get update && apt-get install -y \
    cmake \
    build-essential \
    git \
    libssl-dev \
    python3-dev \
    curl

# 2. Clone and build liboqs
echo "📥 Cloning liboqs..."
git clone --recursive https://github.com/open-quantum-safe/liboqs.git
cd liboqs
mkdir build && cd build

echo "🔨 Building liboqs with selective KEM support..."
cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local \
      -DOQS_USE_OPENSSL=OFF \
      -DOQS_DIST_BUILD=ON \
      -DOQS_ENABLE_KEM_BIKE=OFF \
      -DOQS_ENABLE_KEM_FRODO=OFF \
      -DOQS_ENABLE_SIG_PICNIC=OFF \
      ..

make -j$(nproc)
make install
cd ../..

# 3. Set env var so oqs-python finds the lib
echo "🔧 Exporting OQS library path..."
export LD_LIBRARY_PATH=$HOME/.local/lib:$LD_LIBRARY_PATH

# 4. Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# 5. Install oqs-python again so it finds the compiled C library
pip install --force-reinstall oqs

echo "✅ Build complete."
