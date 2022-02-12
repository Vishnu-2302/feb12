ricebags=600
oil=155
sugar=50
soap=40
icecreams=250
print('customer name     = vishnu')
print('customer number = 8106847763') 
rc=int(input('enter no of rice bag(s)(10kg) : '))
cq=int(input('enter no of oil packets            : '))
rq=int(input('enter no of   sugar packets    : '))
sq=int(input('enter no of soaps                     : '))
iq=int(input('enter no of ice cram packs     : '))
cc=input('enter coupon code: ') 
bill=(ricebags*rc)+(oil*cq)+(sugar*rq)+(soap*sq)+(icecreams*iq) 
if bill>5000: 
 if cc=='hi': 
    dis=bill*10/100 
    tax=bill*10/100
 elif cc=='bye':
    dis=bill*10/100
    tax=0 
if bill>3000:
 if cc=='hi': 
    disc=bill*8/100 
    tax=bill*10/100
 elif cc=='bye':
    dis=bill*8/100
    tax=0
if bill>2000: 
 if cc=='hi': 
    dis=bill*5/100 
    tax=bill*10/100
 elif cc=='bye':
    dis=bill*5/100
    tax=0
if bill>1000: 
 if cc=='hi': 
    dis=bill*3/100 
    tax=bill*10/100
 elif cc=='bye': 
    dis=bill*3/100 
    tax=0
else: 
 print('invalid coupon code')
print('amount                  : ',bill)
print('tax payed              : ',tax)
print('amount                  : ',bill+tax)
print('discount allowed : ',dis)
mainbill = (bill-dis)+tax 
print('total bill amount   : ',mainbill)
