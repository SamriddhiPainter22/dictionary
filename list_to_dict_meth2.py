def Convert_dict(a):
    init=iter(list1)
    res_dct=dict(zip(init,init))
    return res_dct

    #driver code
list1=['X',1,'Y',2,'Z',3]
print(Convert_dict(list1))