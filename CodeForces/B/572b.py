#SE HACE UN DICCIONARIO DONDE LAS ORDENES QUE CUESTAN LO MISMO SE SUMAN
#LUEGO SE HACE UNA LISTA QUE LAS ORDENA Y AL FINAL NOMAS SE IMPRIMEN
n, s = map(int, input().split())
buy_dict, sell_dict = {}, {}
for _ in range(n):
    order = [val if i == 0 else int(val) for i, val in enumerate(input().split())]
    if order[0] == 'B':
        if order[1] in buy_dict:
            buy_dict[order[1]] += order[2]
        else:
            buy_dict[order[1]] = order[2]
    else:
        if order[1] in sell_dict:
            sell_dict[order[1]] += order[2]
        else:
            sell_dict[order[1]] = order[2]
buy_list = sorted([(k, v) for k, v in buy_dict.items()], reverse=True)
sell_list = sorted([(k, v) for k, v in sell_dict.items()])
sell_list = sorted(sell_list[:s], reverse=True)
len_s = len(sell_list)
len_b = len(buy_list)
for i in range(s):
    if i < len_s:
        print('S {} {}'.format(sell_list[i][0], sell_list[i][1]))
    else:
        break
for i in range(s):
    if i < len_b:
        print('B {} {}'.format(buy_list[i][0], buy_list[i][1]))
    else:
        break
