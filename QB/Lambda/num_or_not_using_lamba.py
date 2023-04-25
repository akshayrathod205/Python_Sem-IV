
num = lambda q: q.replace('.','',1).isdigit()
is_num = lambda r: num(r[1:]) if r[0]=='-' else num(r)


print(is_num('26587') ,"\n", is_num('-12547') ,"\n", is_num('00') ,"\n", is_num('A001') ,"\n", is_num('-24587.11'))

