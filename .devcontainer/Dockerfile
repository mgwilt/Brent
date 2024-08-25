FROM mcr.microsoft.com/devcontainers/miniconda:1-3

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/

# Initialize conda and set up the environment
RUN /opt/conda/bin/conda init bash \
    && if [ -f "/tmp/conda-tmp/environment.yml" ]; then \
        umask 0002 && \
        ENV_NAME=$(grep -E '^name:' /tmp/conda-tmp/environment.yml | awk '{print $2}') && \
        /opt/conda/bin/conda env create -f /tmp/conda-tmp/environment.yml || \
        /opt/conda/bin/conda env update -n "$ENV_NAME" -f /tmp/conda-tmp/environment.yml; \
    fi \
    && rm -rf /tmp/conda-tmp

# Automatically activate the environment if environment.yml exists
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then \
        ENV_NAME=$(grep -E '^name:' /tmp/conda-tmp/environment.yml | awk '{print $2}') && \
        echo "conda activate $ENV_NAME" >> ~/.bashrc; \
    fi

# [Optional] Uncomment to install a different version of Python than the default
# RUN conda install -y python=3.6 \
#     && pip install --no-cache-dir pipx \
#     && pipx reinstall-all

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
