## shamsi > gregorian
# jalali_to_gregorian()

import pandas as pd
def isleapyear(yr):
    data1 = [1,5,9,13,17,21,26,30]
    data2 = [1,5,9,13,17,22,26,30]
    num = yr % 33
    if yr >= 1343 :
        if num in data1:
            return True
        else:
            return False
    elif yr <= 1342:
        if numin data2:
            return True
        else:
            return False


dmyj = [21,9,1351]
basej = [1,1,1300]
baseg = [3,21,1921]
baseg_str = str(baseg[0]) + "/" + str(baseg[1]) + "/" + str(baseg[2])

if dmyj[0] >= 32:
    print('wrong day entry! please note that day count should not be greater that 31')
elif dmyj[1] >= 13:
    print('wrong month entry! please note that month count should not be greater that 12')
else:
    deltadays = dmyj[0] - basej[0]
    if dmyj[1] >= 8:
        dmyj[1] -= 7
        deltadays += 186  # 6 * 31
        deltadays += (dmyj[1] * 30)
    elif dmyj[1] <= 7:
        deltadays += ((dmyj[1]-1) * 31)
    for year in range(basej[2], dmyj[2]):
        if isleapyear(year):
            deltadays +=366
        else:
            deltadays += 365

    enddate = pd.to_datetime(baseg_str) + pd.DateOffset(days=deltadays)
    print(str(enddate)[:10])



