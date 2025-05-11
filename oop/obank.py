import pickle

class Bank:
    bank_record = {}

    def __init__(self):
        self.bank_record= self.load()

    def id_create(self, id):
        # add validation for id (negative check and existance check)
        if self.verifications(id):
            print("id already created")
        else:
            print("Account:" + str(id) + " created")
            self.bank_record[id] = 0  
            self.save()

    def deposit(self,id,money):
        # add validation for id (existance check), money (negative check)
         if self.verifications(id):     
            print("Deposit " +str(money) + " into account " + str(id))
            self.bank_record[id] = self.bank_record[id] + money
            self.save()
         else:
             print("id false")

    def withdraw(self,id,withdraw):
        # validation for id (existance) and withdraw (negative check)
        if self.verifications(id):
            print("Trying to withdraw money " + str(withdraw) + " from account " + str(id))
            if self.bank_record[id]<withdraw:
                print ('Not Enough Fund')
            else:
                self.bank_record[id]=self.bank_record[id]-withdraw
                self.save()
        else:
            print("id false" )

    def show_account(self, id):
        if self.verifications(id):
            print("your money in the bank is: " + str(self.bank_record[id]))
        else:
            print("id false")

    def verifications(self, id):
        if id in self.bank_record:
            return True
        else :
            return False
        
    def save(self, filename='bank_record.pkl'):
        with open(filename, 'wb') as file:
            pickle.dump(self.bank_record, file)
        print("Bank record saved!")

    def load(self, filename='bank_record.pkl'):
        try:
            with open(filename, 'rb') as file:
                # Check if file is empty
                if file.read(1):
                    file.seek(0)
                    return pickle.load(file)
                else:
                    return {}  # Return an empty dictionary if file is empty
        except FileNotFoundError:
            print("File not found. Returning an empty dictionary.")
            return {}
        except EOFError:
            print("File is empty. Returning an empty dictionary.")
            return {}
        except pickle.UnpicklingError:
            print("File is corrupted or not a valid pickle file.")
            return {}
    
    def run_bank(self):
        id=int(input("whats your id"))
        while True:
            p = int(input("to deposit,enter 1 ; to withdraw,press 2;to show amount,press 3;to exit,press 4 "))
            if p == 1:
                x=int(input("what is the amount you want to deposit?") )
                
                self.deposit(id,x)
            if p==2:
                y=int(input ('what is the amount you want to withdraw'))
                self.withdraw(id,y)
            if p==3:
                self.show_account(id)
            if p ==4:
                return      

class XBank(Bank) :  
    def id_create(self, id):
        print("this is from XBank")
        return super().id_create(id)
    def deposit(self, id, money):
        print("this is from XBank")
        return super().deposit(id, money)
    def withdraw(self, id, withdraw):
        print("this is from XBank")
        return super().withdraw(id, withdraw)
    def show_account(self, id):
        print("this is from XBank")
        return super().show_account(id)
    def run_bank(self):
        print("this is from XBank")
        return super().run_bank()









# Tests
obank=XBank()
obank.id_create(123)
obank.show_account(123)

# Test duplicate id creation
obank.id_create(123)

obank.deposit(123, 100)
obank.show_account(123)

# None exist ID verfication
obank.deposit(321, 100)
obank.withdraw(321, 100)

obank.withdraw(123, 1000)
obank.withdraw(123, 99)
obank.show_account(123)

#XBank=XBank()
#XBank.id_create