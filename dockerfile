#Pythonのベースイメージを指定
FROM python

#必要なライブラリをインストール
RUN apt-get update
RUN pip install --upgrade pip

#作業ディレクトリを指定
WORKDIR /app