# Utiliser une image de base Ubuntu avec CUDA préinstallé
FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    wget \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installer Miniconda
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh && \
    $CONDA_DIR/bin/conda clean -tipsy

# Ajouter Conda au PATH
ENV PATH=$CONDA_DIR/bin:$PATH

# Créer et activer un environnement Conda avec Python 3.8
RUN conda create -n myenv python=3.8 -y
RUN echo "source activate myenv" > ~/.bashrc
ENV CONDA_DEFAULT_ENV=myenv
ENV PATH=$CONDA_DIR/envs/$CONDA_DEFAULT_ENV/bin:$PATH

# Installer Pytorch avec le support GPU, FastAPI, Ludwig, et autres dépendances
RUN conda install pytorch torchvision torchaudio cudatoolkit=11.8 -c pytorch -y
RUN pip install fastapi uvicorn ludwig pandas

# Copier les fichiers de l'application
COPY . /app
WORKDIR /app

# Exposer le port pour FastAPI
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
