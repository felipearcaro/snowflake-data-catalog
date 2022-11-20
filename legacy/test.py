a = [('mysql', 'subs"criberb', "10'99batchalternateaddress", 'Stores alternate addresses of 1099-MISC batches', 'batchId', 'Id of the batch', 'int', 'NO', None, 10)]

for i in a:
    b = tuple(j.replace("'","").replace('"','') if isinstance(j,str) else j for j in i)

print(b)



