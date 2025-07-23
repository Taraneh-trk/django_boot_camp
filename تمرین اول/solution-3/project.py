import csv ,re ,os
            

class menu:
    def __init__(self,filename):
        self.filename = filename
        self.contact_number = 0
        self.contact_number = self.num()
        while True:
            print('the correct format of phone has 11 numbers and the correct format of email is like "...@gmail.com" ')
            print('what do you want to do ?')
            print('1- add')
            print('2- remove')
            print('3- show')
            print('4- modify')
            print('5- sort')
            print('6- exit')
            try:
                choice = int(input('enter number of your choice : '))
            except:
                print('write the number of your choice')
                continue
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
                print('added succusfully')
                self.contact_number +=1
                break
            else:
                print('try again')

    def remove(self):
        name = input('enter name who you want to remove : ')
        d = []
        with open(self.filename,'r+') as f:
            reader = csv.DictReader(f)
            for i in reader:
                if i['name']==name :
                    continue
                d.append(i)
        with open(self.filename,'w') as f:
            writer = csv.DictWriter(f,fieldnames=['name','phone','email'])
            writer.writeheader()
            writer.writerows(d)
        print('removed succusfully')
        self.contact_number -=1
        
    def show(self):
        with open(self.filename,'r') as f:
            reader = csv.DictReader(f)
            j=1
            for i in reader:
                print()
                print(f" {j} -   name : {i['name']} , phone : {i['phone']} , email : {i['email']}") ; j+=1
                print()

    def modify(self):
        name_want_to_change,phone_want_to_change,email_want_to_change = input('enter (name phonenumber email) you want to change : ').split(' ')
        name,phone,email = input('enter (name phonenumber email) who you want to change to : ').split(' ')
        while True:
            if check(phone,email):
                d = []
                with open(self.filename,'r+') as f:
                    reader = csv.DictReader(f)
                    for i in reader:
                        if i['name']==name_want_to_change and i['phone']==phone_want_to_change and i['email']==email_want_to_change:
                            dict = {'name': name, 'phone': phone, 'email': email}
                            d.append(dict)
                            continue
                        d.append(i)
                with open(self.filename,'w') as f:
                    writer = csv.DictWriter(f,fieldnames=['name','phone','email'])
                    writer.writeheader()
                    writer.writerows(d)
                print('modified succusfully')
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
        print('sorted succusfully')
    
    def num(self):
        with open(self.filename,'r') as f:
            reader = csv.DictReader(f)
            for i in reader:
                self.contact_number+=1
        return self.contact_number

def check_phone(phone):
    if re.search('\d{11}',phone):
        return True
    return False

def check_email(email):
    if re.search('(\S+)@gmail\.com',email):
        return True
    return False

def check(phone , email):
    if check_phone(phone) and check_email(email):
        return True
    return False

def main():
    
    
    
    if os.path.exists('project.csv'):
        pass
    else:
        file = open('project.csv','a+')
        writer = csv.DictWriter(file,fieldnames=['name','phone','email'])
        writer.writeheader()
        file.close()
    m = menu('project.csv')

if __name__=="__main__":
    main()