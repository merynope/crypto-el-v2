#!/usr/bin/env bash
set -e

echo "🚀 Installing system dependencies..."
apt-get update && apt-get install -y cmake build-essential git

echo "📦 Cloning and building liboqs..."
git clone --depth=1 https://github.com/open-quantum-safe/liboqs
cmake -S liboqs -B liboqs/build -DBUILD_SHARED_LIBS=ON
cmake --build liboqs/build --target install

echo "🐍 Setting up liboqs environment..."
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export OQS_INSTALL_PATH=/usr/local

echo "📥 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🔐 Installing liboqs-python from GitHub..."
pip install git+https://github.com/open-quantum-safe/liboqs-python

echo "✅ Build complete!"
