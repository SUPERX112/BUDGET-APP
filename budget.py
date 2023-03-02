class Category:
    def __init__(self,categories):
        self.name=categories
        self.__sum=0.0
        self.name2=''
        self.ledger=[]

    def deposit(self,value,description=''):
        d={}
        d["amount"]=value
        d["description"]=description
        self.ledger.append(d)
        self.__sum+=value

    def withdraw(self,value,description=''):
        if self.__sum-value>=0:
            d={}
            d["amount"]= -value
            d["description"]= description
            self.ledger.append(d)
            self.__sum-=value
            return True
        else:
            return False

    def transfer(self,value,description=''):
        if self.withdraw(value,f"Transfer to {description.name}"):
            description.deposit(value,f"Transfer from {self.name}")
            return True

        else:
            return False
        
    def get_balance(self):
        return self.__sum

    def check_funds(self,value):
        if self.__sum>=value:
            return True
        else:
            return False

    def __str__(self):
        line1=self.__line1()
        end=line1+'\n'
        for elem in self.ledger:
            b=str(elem['description'])
            end+= self.__f_name(b)
            end+= self.__space(elem['description'],elem['amount'])
            end+= self.__f_value(elem['amount'])
            end+='\n'
        end+=f'Total: {self.__sum}'
        return end
        
    def __line1(self):
        name=self.name
        line1=''
        space_name=len(name)
        space=30-space_name
        symbol=space/2
        symbol=int(symbol)
        for x in range(0,int(symbol)):
            line1+='*'
        line1+=f'{self.name}'
        for x in range(0,symbol):
            line1+='*'
        return line1

    def __space(self, nome, value):
            len1=len(self.__f_name(nome))
            len2=len(self.__f_value(value))
            space1=30-len1-len2
            space='' 
            for x in range (0,space1):
                space+=' '
            return space

    def __f_value(self,value):
        x=f'{value:.2f}'
        f_value=''
        if len(x)>7:
            for b in range(0,7):
                f_value+=x[b]
            return(f_value)
        else:
            return x

    def __f_name(self,name):
        x=len(name)
        f_name=''
        if x>23:
            for b in range(0,23):
                f_name+=name[b]
            return(f_name)
        else:
            return name

def create_spend_chart(categories):
    value_sum=[]
    name_tot=[]
    total=0
    graph='Percentage spent by category\n'

    #Add category withdrawal sums to value_sum
    for elem in categories:
        tot=0
        for value in elem.ledger:
            if value['amount']<0:
                tot+=round(value['amount'])
        value_sum.append(tot*-1)

    #create a total
    for elem in value_sum:
        total+=elem

    #create values ex. 100| o  o 
    count=len(value_sum)
    for value in range(10,-1,-1):
        graph+=value_f(value)
        count2=0
        for value2 in range (0,count):
            graph+=create_point(value,value_sum[count2],total)+'  '
            count2+=1
        graph+='\n'
    graph+='    ----------\n     '

    ##From here to line 164 there is the creation of vertical characters
    #I find the greatest value to iterate on and add spaces to not throw 'exception
    name=categories[0].name
    for elem in categories:
        L_name=len(name)
        if L_name<len(elem.name):
            name=elem.name
            
    for elem in categories:
        elem.name2=elem.name
        for i in range(0,len(name)-len(elem.name2)):
            elem.name2+=' '

    for i in range(0,len(name)):
        for elem in categories:
            name_tot.append(elem.name2[i])

    #count2 is equal to items in the list passed as arguments
    count2=0
    for elem in categories:
        count2+=1

    #count check when to wrap
    #count3 check the end of printing
    count=0
    count3=0
    for character in name_tot:
        graph+=character+'  '
        count+=1
        count3+=1
        if count3==len(name_tot):   #the end of printing
            break
        else:
            if count==count2:     # to wrap
                graph+='\n     '
                count=0

    return graph

def value_f(value):
    if value==10:
        return f'{value*10}| '
    elif value<10 and value >0:
        return f' {value*10}| '
    elif value==0:
        return f'  {value*10}| '

def create_point(index,value,total):
    value=((((value/total)*10)//1)*10)
    if index*10<=value:
        return 'o'
    else:
        return ' '
