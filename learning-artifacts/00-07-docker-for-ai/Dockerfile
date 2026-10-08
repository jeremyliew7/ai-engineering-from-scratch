# Local practice copy of phases/00-setup-and-tooling/07-docker-for-ai/code/Dockerfile.
# Keep completed build steps unchanged to reuse their cache.
# Official CUDA wheels are pinned to CPython 3.12 on Linux x86_64 with SHA-256.
# Resolve ordinary dependencies through USTC for these install commands only.
FROM --platform=linux/amd64 nvidia/cuda:12.4.1-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    git \
    curl \
    build-essential \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y --no-install-recommends \
    python3.12 \
    python3.12-venv \
    python3.12-dev \
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1

RUN curl -sSL https://raw.githubusercontent.com/pypa/get-pip/3b73145063be545b649ad9ca83ea8da5fc915a4f/public/get-pip.py -o /tmp/get-pip.py \
    && echo "a341e1a43e38001c551a1508a73ff23636a11970b61d901d9a1cad2a18f57055  /tmp/get-pip.py" | sha256sum -c - \
    && python /tmp/get-pip.py \
    && rm /tmp/get-pip.py \
    && update-alternatives --install /usr/bin/pip pip /usr/local/bin/pip3.12 1

RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel

RUN python -m pip install --no-cache-dir \
    "https://download.pytorch.org/whl/cu124/torch-2.6.0%2Bcu124-cp312-cp312-linux_x86_64.whl#sha256=a393b506844035c0dac2f30ea8478c343b8e95a429f06f3b3cadfc7f53adb597" \
    "https://download.pytorch.org/whl/cu124/torchvision-0.21.0%2Bcu124-cp312-cp312-linux_x86_64.whl#sha256=efb53ea0af7bf09b7b53e2a18b9be6d245f7d46a90b51d5cf97f37e9b929a991" \
    "https://download.pytorch.org/whl/cu124/torchaudio-2.6.0%2Bcu124-cp312-cp312-linux_x86_64.whl#sha256=3e5ffa69606171c74f3e2b969785ead50b782ca657e746aaee1ee7cc88dcfc08" \
    --index-url https://mirrors.ustc.edu.cn/pypi/simple

RUN python -m pip install --no-cache-dir \
    numpy \
    pandas \
    scikit-learn \
    matplotlib \
    jupyter \
    transformers \
    datasets \
    accelerate \
    safetensors \
    --index-url https://mirrors.ustc.edu.cn/pypi/simple

WORKDIR /workspace

VOLUME ["/workspace", "/models"]

EXPOSE 8888

CMD ["python"]
