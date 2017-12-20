import re
rex = r"a.d"   # 正则表达式文本
original_str = "and"  # 原始文本
pattern = re.compile(rex)  # 正则表达式对象
m = pattern.match(original_str)  # 匹配对象
print(m) 

c=re.match(r"a.d", "and")
print(c)


re.match(r"a.c", "abc").group()
'abc'
re.match(r"a.c", "abcef").group()
'abc'
re.match(r"1\.2", "1.2").group()
'1.2'
re.match(r"a[0-9]b", "a2b").group()
'a2b'
re.match(r"a[0-9]b", "a5b11").group()
'a5b'
re.match(r"a[.*?]b", "a.b").group()
'a.b'
re.match(r"abc[^\w]", "abc!123").group()
#'abc!