This is a repository of VRChat usefull tools.

# Devices
You need these devices.
- obniz
  - https://store.obniz.com/ja/collections/frontpage/products/obniz
- 曲げセンサ
  - FS-L-0055-253-ST
    - https://www.switch-science.com/catalog/508/
- ブレッドボードやピンソケットはお好みで

# フロー
- 曲げセンサは曲がり具合によって抵抗値が変わります
- obniz で曲げセンサの抵抗値を計測
- そのデータをVRChatが起動しているPCへ送信

# アバター
Expressions parameters の設定をする

# VRChat との bind 設定
例えば、以下のようなファイルを VRChat 実行マシンの指定場所に置く。
```
{
    "id" : "avtr_65ce1c9d-fc2d-4535-afba-5dd3c4d519dd",
    "name" : "TarteTatin",
    "parameters" : [
        {
            "name" : "OscEars",
            "input" : {
                "address" : "/fingers/index",
                "type" : "Float"
            }
        }
    ]
}
```
name の OscEars が VRChat の Expressions parameters になり、
address の /fingers/index が OSC 側のパラメーター名となる


# Docker
docker build -t vrchat/osc .

docker run -it --rm -v ~/vrcha_neta:/app vrchat/osc /bin/bash
