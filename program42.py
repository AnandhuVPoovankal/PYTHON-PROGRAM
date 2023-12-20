import csv
field=['No',         'Company',          'Model']
cars=[{'No':1,  'Company':'TATA',      'Model':'SAFARI'},
      {'No':2,  'Company': 'MARUTHI',   'Model': 'SWIFT'},
      {'No':3,  'Company': 'CHEVROLET', 'Model': 'CRUZE'},
      {'No':4,  'Company': 'Toyota',     'Model': 'Fortuner'}]
r=open('b.csv','w')
write=csv.DictWriter(r,fieldnames=field)
write.writeheader()
write.writerows(cars)
r.close()

c=open('b.csv',newline='')
d=csv.reader(c)
for i in d:
    print(' '.join(i))

