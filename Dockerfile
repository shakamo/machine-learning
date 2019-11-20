# https://gcr.io/kaggle-images/python
# FROM gcr.io/kaggle-images/python:latest
FROM gcr.io/kaggle-images/python:v69

# ライブラリの追加インストール
RUN pip install -U pip && \
    pip install fastprogress japanize-matplotlib
