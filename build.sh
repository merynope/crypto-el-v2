#!/bin/bash

set -e

# Install system dependencies (Render doesn't have these by default)
echo "🔧 Installing build dependencies..."
apt-get update && apt-get install -y \
    cmake \
    build-essential \
    git \
    libssl-dev \
    python3-dev \
    curl

# Clone and build liboqs
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

# Set environment variables so the oqs-python package can find the shared library
echo "🔧 Exporting OQS library path..."
export LD_LIBRARY_PATH=$HOME/.local/lib:$LD_LIBRARY_PATH

cd ../..

# Optional: install oqs-python again now that the C lib is available
echo "🐍 Reinstalling oqs-python..."
pip install --force-reinstall oqs

echo "✅ Build script completed successfully."
