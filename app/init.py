from core.oodb import Oodb as Db


data=[]
data.append({
    'id':'int | primary',
    'firstname':'string',
    'middlename':'string',
    'lastname':'string',
    'address':'string',
    'email':'email',
    'phone':'int(15)',
    'date_created':'date'
})


Bank_data=[]
Bank_data.append({
    'account':'int | primary',
    'user id':'int | ref(Person.id)',
    'account_type':'string',
    'account_balance':'int',
    'date_created':'date',
})

Obj = Db('root','', 'localhost', 'Sample')
Obj.set_class("Person", data)
Obj.set_class("Bank", Bank_data)


