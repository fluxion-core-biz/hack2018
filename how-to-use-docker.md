
# Dockerの使い方メモ

## DockerのInstall

1. Install
Win10の場合はDocker for windowsを入れればよい
<https://hub.docker.com/editions/community/docker-ce-desktop-windows>

WIn7の場合、Docker toolboxでVM上にLinuxが入り、その上でDocker-Machineが動く多層構造になるので、
デフォルト設定だとリソースが少なく足りなくなるかもしれない。

余裕があるなら、以下の様な感じで作り直しておくと良い。
(数値の部分は自分のPCのスペックに合わせて調整してください。)

```shell
docker-machine stop
docker-machine rm default
docker-machine create default --driver virtualbox --virtualbox-cpu-count "6" --virtualbox-disk-size "64000" --virtualbox-memory "32768"
```

## 初回だけ行うイメージのビルド、コンテナ生成

1. コンテナイメージをビルドする。
以下で*team-supp:00.01*という名前のイメージが生成される。
コロンの後ろはtag番号(レビジョンなど)を示す。
更新して行く時にはインクリメントすればよい。

```shell
cd <path/to/Dockerfile>
docker build -t team-supp:00.01 .
```

1. イメージからコンテナのインスタンスを生成して起動する。
以下でdocker create + docker startの2つの処理がまとめて行われ、*my-supp*という名前のコンテナが生成されます。
**2回目にコマンドを実行するとエラーになります**
**同名で別インスタンスを作ろうとするためですが、これを知らずに--name指定なしにrunを繰り返すと大量のコンテナがゴミとして残って行きます**
**作り直したい場合は別の名前で作るか、`docker rm <container-id>`で削除してから作りましょう。**

```shell
docker run -d --name my-supp -p 80:80 team-supp:00.01
docker run -d --name my-supp-light -p 80:80 team-supp:light-00.01
docker run -d --name my-supp-light -p 80:80 team-supp:light-00.03
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
Ctrl + c で抜けると同時に終了します。

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

- team-suppのデバッグメモ
/app/reload.triggerにtouchする(更新時刻を更新する)と、
uWSGIで自動検知してFlaskのRESTコード(main.py等)をLive状態のまま自動Reloadするようにしています。
更新と一緒にReloadしたいなら、以下の様に書けばよいです。

```shell
docker cp main.py my-supp:/app/. && docker exec my-supp /bin/touch /app/reload.trigger
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

## Azure Conteiner Registoryへのイメージ登録方法

1. terminalからログインする

```shell
docker login teamsupp.azurecr.io
Username: teamsupp
Password: Z/GPzmWp5Ox3dXhVSFrjMmcPde1F05Dp # (実際はPWは入力しても表示されません)
Login Succeeded
```

1. イメージにTagを付ける
`docker tag {ローカルにあるイメージ名:タグ} {ログイン先のAzureサーバー名}/{イメージ名}:{タグ}`
実行したら`docker images`コマンドで作成されたことを確認する。

```shell
docker tag team-supp:light-00.01 teamsupp.azurecr.io/team-supp:light-00.01
docker tag team-supp:light-00.02 teamsupp.azurecr.io/team-supp:light-00.02
docker images
```

1. 作成したイメージをPushする
`docker push {ログイン先のAzureサーバー名}/{イメージ名}:{タグ}`

```shell
docker push teamsupp.azurecr.io/team-supp:light-00.01
```
# Azure Container のDebug方法

```shell
az login
az container exec --resource-group teamsupp --name teamsuppv0001 --exec-command /bin/bash

az container exec --resource-group teamsupp --name teamsuppv0003 --exec-command /bin/bash

az container attach --resource-group teamsupp --name teamsuppv0003

az container logs --resource-group teamsupp --name teamsuppv0003
```

