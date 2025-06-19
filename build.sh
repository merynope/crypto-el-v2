#!/bin/bash

set -e

# 1. Install build tools
echo "🔧 Installing system dependencies..."
apt-get update && apt-get install -y \
    cmake \
    build-essential \
    git \
    libssl-dev \
    python3-dev \
    curl \
    python3-venv

# 2. Set up virtual environment
echo "📦 Setting up Python virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# 3. Install pip & requirements
echo "🐍 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Clone and build liboqs
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

# 5. Set library path
echo "🔧 Exporting OQS library path..."
export LD_LIBRARY_PATH=$HOME/.local/lib:$LD_LIBRARY_PATH

# 6. Reinstall oqs so it finds compiled liboqs
echo "🔁 Reinstalling oqs Python wrapper..."
pip install --force-reinstall oqs

echo "✅ Build complete."
