
FROM jupyter/base-notebook:python-3.10

RUN pip install --upgrade pip && \
    pip install sbi
