from encode import Encode

text = '送你上飞机'
code = Encode(text)
code.encode()
res_encode = code.res_encode
code2 = Encode(res_encode)
code2.decode()
print(f'原始文字：{text}')
print(f'加密后：{code.res_encode}')
print(f'解密后：{code2.res_decode}')