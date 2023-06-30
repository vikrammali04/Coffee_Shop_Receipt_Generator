import sys

pro1={1:'Espresso',2:'Cappuccino',3:'Latte'}#product list
add1={1:'Milk', 2:'Cream' ,3:'Syrup'}#addons list
print("Dear sir / Ma'am Greetings of the day!! \nWhat do you want ? \nwe have")

#definig variables.
i1=[]
j1=[]
q1=[]       
bill1=[]

#class
class coffee():
    #Receipt Generator
    def receipt(i1,j1,q1):

        print('Jay Ambe Coffee house'.center(51,'-'))
        print('Customer invoice'.center(51,'-'))
        print('No.','Product'.ljust(13,' '),'Add-on'.ljust(8,' '),'Rate'.ljust(6,' '),'Quantity'.ljust(9,' '),'Amount'.ljust(8,' '))
        for i in range(len(i1)):
            print(i+1,'.',pro1[i1[i]].ljust(13,' '),add1[j1[i]].ljust(8,' '),
            str(bill1[i]/q1[i]).rjust(6,' '),str(q1[i]).rjust(6,' '),str(bill1[i]).rjust(8,' '))
        print('_'.center(51,'_'))
        print('Total :',sum(bill1))
        print('Thank You'.center(51,'-'))
        sys.exit()

    #Allowing user to enter more than one item
    def checknext():    
            t=input('Do You want something else..? y/n\n')
            if t=='y':
                coffee.main()
            elif t=='n':
                coffee.receipt(i1,j1,q1)
            else:
                print('Invalid entry !!\n')
                coffee.checknext()

    #main function
    def main():
        bill=0
        print('1 : Espresso\n2 : Cappuccino\n3 : Latte\n')
        i=int(input('Enter a choice\n'))
        print('1 : Milk\n2 : Cream\n3 : Syrup\n')
        j=int(input('Enter a choice\n\n'))
        q=int(input('Enter the quantity\n'))
        #Bill calculation
        if i<4 and j<4:
            q1.append(q)
            i1.append(i)
            j1.append(j)
            if i==1:
                if j==1:
                    bill+=60*q
                elif j==2:
                    bill+=75*q
                elif j==3:
                    bill+=100*q
            if i==2:
                if j==1:
                    bill+=80*q
                elif j==2:
                    bill+=90*q
                elif j==3:
                    bill+=125*q
            if i==3:
                if j==1:
                    bill+=100*q
                elif j==2:
                    bill+=125*q
                elif j==3:
                    bill+=150*q
                
        else:
            print('Enter a valid num')
            coffee.main()
        bill1.append(float(bill))
        coffee.checknext()
                    

if __name__=='__main__':
    coffee.main()

