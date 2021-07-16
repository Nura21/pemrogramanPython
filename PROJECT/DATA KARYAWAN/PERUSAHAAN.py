def perusahaan():
    print("\nPEMASUKKAN DATA PERUSAHAAN")
    sales=input("\nMasukkan data Sales : Rp")
    COGS=input("\nMasukkan data COGS : Rp")
    Grossprofit =int(sales)-int(COGS)
    print("Grossprofit : Rp"+str(Grossprofit))
    Operating(Grossprofit)

def Operating(Grossprofit):
    Operating_expenses=input("\nMasukkan data Operating Expenses : Rp")
    Income_from_operations=int(Grossprofit)-int(Operating_expenses)
    print("Income from Operations : Rp"+str(Income_from_operations))
    Income(Income_from_operations)
    return Income_from_operations
    
def Income(Income_from_operations):
    Other_revenuesandgains=input("\nMasukkan data Other Revenues and Gains : Rp")
    Other_expensesandloses=input("\nMasukkan data Other Expenses and Losses : Rp")
    Net_income_loss=(int(Income_from_operations)+int(Other_revenuesandgains))-int(Other_expensesandloses)
    print("Net Income/Loss : Rp"+str(Net_income_loss))
    return Net_income_loss
    
def pemrosesan_data():
    perusahaan()
    