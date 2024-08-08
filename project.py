import csv ,re
            

class menu:
    def __init__(self,filename):
        self.filename = filename
        while True:
            print('what do you want to do ?')
            print('1- add')
            print('2- remove')
            print('3- show')
            print('4- modify')
            print('5- sort')
            print('6- exit')
            choice = int(input('enter number of your choice : '))
            if choice==1:
                self.add()
            elif choice==2:
                self.remove()
            elif choice==3:
                self.show()
            elif choice==4:
                self.modify()
            elif choice==5:
                self.sort()
            elif choice==6:
                exit()
    
    def add(self):
        while True:
            name,phone,email = input('enter (name phonenumber email) : ').split(' ')
            if check(phone,email):
                with open(self.filename,'a') as f:
                    writer = csv.DictWriter(f,fieldnames=['name','phone','email'])
                    writer.writerow({'name':name,'phone':phone,'email':email})
                break
            else:
                print('try again')

    def remove(self):
        name,phone,email = input('enter (name phonenumber email) who you want to remove : ').split(' ')
        d = []
        with open(self.filename,'r+') as f:
            reader = csv.DictReader(f)
            for i in reader:
                if i['name']==name and i['phone']==phone and i['email']==email:
                    continue
                d.append(i)
        with open(self.filename,'w') as f:
            writer = csv.DictWriter(f,fieldnames=['name','phone','email'])
            writer.writeheader()
            writer.writerows(d)
        
    def show(self):
        with open(self.filename,'r') as f:
            reader = csv.DictReader(f)
            j=1
            for i in reader:
                print()
                print(f" {j} -   name : {i['name']} , phone : {i['phone']} , email : {i['email']}") ; j+=1
                print()

    def modify(self):
        name_want_to_change = input('enter name you want to change : ')
        name,phone,email = input('enter (name phonenumber email) who you want to change to : ').split(' ')
        while True:
            if check(phone,email):
                d = []
                with open(self.filename,'r+') as f:
                    reader = csv.DictReader(f)
                    for i in reader:
                        if i['name']==name_want_to_change:
                            dict = {'name': name, 'phone': phone, 'email': email}
                            d.append(dict)
                            continue
                        d.append(i)
                with open(self.filename,'w') as f:
                    writer = csv.DictWriter(f,fieldnames=['name','phone','email'])
                    writer.writeheader()
                    writer.writerows(d)
                break
            else:
                print('try again')

    def sort(self):
        d = []
        with open(self.filename,'r+') as f:
            reader = csv.DictReader(f)
            for i in reader:
                d.append(i)
        d = sorted(d,key=lambda x : x['name'])
        with open(self.filename,'w') as f:
            writer = csv.DictWriter(f,fieldnames=['name','phone','email'])
            writer.writeheader()
            writer.writerows(d)


def check(phone,email):
    if re.search('\d{11}',phone) and re.search('(\S+)@gmail\.com',email):
        return True
    return False


file = open('project.csv','a')
writer = csv.DictWriter(file,fieldnames=['name','phone','email'])
file.close()
m = menu('project.csv')