#MtucX
# coding: utf-8
from binascii import unhexlify

decrypt = ""
key = 334688979656405361773
key2 = 783340156742833416191

cryptotext = """025452037205229131300
128922268479958795704
507343151027440334004
313628318349495303097
740609869255617681333
743928343077804788556
405219023562734491540
211783513258751189510
649941440719152320279
106298250239853604423""".strip().split('\n')

for i in cryptotext:
  decrypt += "%2X" % pow(int(i), key, key2)
print unhexlify(decrypt)