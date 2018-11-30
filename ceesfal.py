import xlrd
import xlwt

book = xlrd.open_workbook("nrkompanii.xls")
arkusz = book.sheet_by_name("Arkusz1")

bk = xlwt.Workbook(encoding="utf-8")
ark1 = bk.add_sheet("google")

tab = []
for i in range(94):
    tab.append(arkusz.cell(i, 0).value)
    tab.append(arkusz.cell(i, 1).value)
    tab.append(int(arkusz.cell(i, 2).value))
tab2 = []
x = 0
for i in range(280):
    if i % 3 == 0:
        x = tab[i]+" "+tab[i+1]+","+tab[i]+",,"+tab[i+1]+",,,,,,,,,,,,,,,,,,,,,,,Kompania ::: * My Contacts,Mobile,"+str(tab[i+2])
        tab2.append(x)

ark1.write(0, 0, "Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Group Membership,Phone 1 - Type,Phone 1 - Value")
for k in range(94):
   ark1.write(k+1, 0, tab2[k])

bk.save("test.xls")
