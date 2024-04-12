import os,time
class menu:
  menu={"Water":250,"Tea":250,
        "Bavrege":500,"Yougrt":750,
        "Rice":3000,"Beans":2000,
        "Grilled Meat":5000,"Bacha":10000,
        "Grilled Fish":5000,"Fried Egg":1000,
        "Falfel Sandwich":750,"Grilled Chicken":10000,
        "Salad":2000,"Checkbeans":2000}
  def __init__(self):
    self.item=""
    self.total=0
    self.orders={}
    self.serviece=0
    
  def mangement(self):
    while True:
      intro=input("""
--------------------------------------------------------------------------

█▀▀█ █▀▀ █▀▀ ▀▀█▀▀ █▀▀█ █──█ █▀▀█ █▀▀█ █▀▀▄ ▀▀█▀▀ 　 █▀▄▀█ █▀▀ █▀▀▄ █──█ 
█▄▄▀ █▀▀ ▀▀█ ──█── █▄▄█ █──█ █▄▄▀ █▄▄█ █──█ ──█── 　 █─▀─█ █▀▀ █──█ █──█ 
▀─▀▀ ▀▀▀ ▀▀▀ ──▀── ▀──▀ ─▀▀▀ ▀─▀▀ ▀──▀ ▀──▀ ──▀── 　 ▀───▀ ▀▀▀ ▀──▀ ─▀▀▀
--------------------------------------------------------------------------    
    
1- Start.
2- Exit

Choose (1,2): """).strip()
      if intro=="1":
        self.show_items(self.menu)
        self.order()
        self.sum_total(self.orders)
        if self.ask_service():
          self.sum_serviece()
        self.clear_screan()
        print("Please wait...")
        time.sleep(2)
        print("Loading...")
        time.sleep(2)
        
        self.show_bill()
        
        break
      elif intro=="2":
        print("Exiting...")
        break
      else:
        self.clear_screan()
        print("Invaled input...")
      
     
  def clear_screan(self):
    os.system("cls"if os.name=="nt"else "clear")
  def show_items(self,items):
    num=0
    for key,value in items.items():
      num+=1
      print(f"{str(num).zfill(2)}-{key:20}{value}")
  def order(self):
    
    while True:
      try:
        item=input("\nPlease enter the item \nor only press enter if you want to finsh your order: ").strip().title()
        if item in self.menu and item:
          count=int(input(f"How many {item} do you want: ").strip())
          self.orders[item]=count
          
        else:
          
          ask=input("Do you want to finsh your order(y,n): ").strip().lower()
          if ask=="y":
            break
      except ValueError:
        print("You must write number.")
  def ask_service(self):
    ask=input("Do you want to pay tip (y,n): ").strip().lower()
    if ask=="y":
      return True
    return False
    
  def sum_serviece(self):
      try:
        ask=int(input("How much do you want to pay( 10, 12, 15): ").strip())
        self.serviece=(ask/100)*self.total
      except ValueError:
        print("Invaled input!!!")
        return self.sum_serviece()
      
  def sum_total(self,orders:dict):
    for item, num in orders.items():
      self.total+=(self.menu[item]*num)

  def show_bill(self):
    num=0
    print("\ntype"," "*20,"number"," "*20,"price\n")
    for item, value in self.orders.items():
      num+=1
      print(f"{str(num).zfill(2)}-{item:14}{value:12}    {self.menu[item]:24}")
    print("="*60)
    print("The tip is payed: ",self.serviece)
    print("The tottal price: ",self.total+self.serviece)
    
    
          
if __name__=="__main__":
  menu=menu()
  menu.mangement()
