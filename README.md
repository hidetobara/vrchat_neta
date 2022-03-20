This is a repository of VRChat usefull tools.

# Devices
You need these devices.
- obniz
  - https://store.obniz.com/ja/collections/frontpage/products/obniz
- �Ȃ��Z���T
  - FS-L-0055-253-ST
    - https://www.switch-science.com/catalog/508/
- �u���b�h�{�[�h��s���\�P�b�g�͂��D�݂�

# �t���[
- �Ȃ��Z���T�͋Ȃ����ɂ���Ē�R�l���ς��܂�
- obniz �ŋȂ��Z���T�̒�R�l���v��
- ���̃f�[�^��VRChat���N�����Ă���PC�֑��M

# �A�o�^�[
Expressions parameters �̐ݒ������

# VRChat �Ƃ� bind �ݒ�
�Ⴆ�΁A�ȉ��̂悤�ȃt�@�C���� VRChat ���s�}�V���̎w��ꏊ�ɒu���B
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
name �� OscEars �� VRChat �� Expressions parameters �ɂȂ�A
address �� /fingers/index �� OSC ���̃p�����[�^�[���ƂȂ�


# Docker
docker build -t vrchat/osc .

docker run -it --rm -v ~/vrcha_neta:/app vrchat/osc /bin/bash
