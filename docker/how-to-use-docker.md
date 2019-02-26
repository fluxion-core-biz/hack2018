
# Dockerの使い方メモ

## 初回だけ行うイメージのビルド、コンテナ生成

1. コンテナイメージをビルドする。
以下で*team-supp*という名前のイメージが生成される。

```shell
cd <path/to/Dockerfile>
docker build -t team-supp .
```

1. イメージからコンテナのインスタンスを生成して起動する。
以下でdocker create + docker startの2つの処理がまとめて行われ、*my-supp*という名前のコンテナが生成されます。
**2回目以降同じコマンドを実行するとエラーになります**
**同名で別インスタンスを作ろうとするためですが、これを知らずに--name指定なしにrunを繰り返すと大量のコンテナがゴミとして残って行きます**

```shell
docker run -d --name my-supp -p 80:80 team-supp
```

## 開発サイクルではコンテナの起動、停止で運用する

- 状態確認
以下で動いているコンテナがないか確認できます

```shell
docker ps -a
```

- 起動
以下で*my-supp*という名前で作ったコンテナを起動できます

```shell
docker start -a my-supp
```

上記コマンドは起動と同時にアタッチ(出力に接続)しているので、
抜ける場合はCtrl + cでコマンドプロンプトに戻れば良いです。

- 停止
以下で停止できます。シャットダウンだと思えば良いです。
再起動する時は、再度起動コマンドをたたけばよいです。

```shell
docker stop my-supp
```

- コンテナにログインしてデバッグしたい
以下で実行中のコンテナにログインできます。

```shell
docker exec -it my-supp /bin/bash
```

使い終わったら`exit`と入力すれば抜けられます。
上記は入出力を接続してコンテナ内でshellを実行しているだけなので、
exitしてもコンテナ自体は終了しません (動き続けます)。


- main.pyを差し替えたい場合の例
以下で自分のPC(ホストマシン)からコンテナにファイルコピーができます。
PCで編集してからアップしたい場合はこの様にすればできます。

```shell
cd <path/to/main.py>
docker cp main.py my-supp:/app/.
```

- Diskがいっぱいになってきて消したい場合
まずコンテナ(インスタンス)を消します。
イメージから生成したコンテナが1つでもあると、元になっているイメージは消せません。
当たり前ですが、保存やサルベージしていない変更は消えるので注意。

```shell
docker ps -a
docker rm <container-id>
```

```shell
docker images
docker rmi <image-id>
```

