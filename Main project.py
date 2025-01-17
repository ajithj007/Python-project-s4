import csv
import pandas as pd
import matplotlib.pyplot as plt

fname = "expenses.csv"

def main():
    createcsv()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Log an Expense")
        print("2. Analyze Data")
        print("3. Visualize Data")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            expense()
        elif choice == "2":
            andata()
        elif choice == "3":
            vdata()
        elif choice == "4":
            print("Thankyou!! .....Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def createcsv():
    try:
       file=open(fname,"r")
       file.close()

    except:
        with open(fname, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Rent): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description (optional): ")

    with open(fname, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense logged successfully!")


def andata():

    df = pd.read_csv(fname)
    print("\n--- Summary Statistics ---")
    print(df.groupby("Category")["Amount"].sum())
    print("\n--- Total Expenses ---")
    print(f"₹{df['Amount'].sum()}")

def vdata():
    df = pd.read_csv(fname)
    datotals=df.groupby("Date")["Amount"].sum()
    cattotals = df.groupby("Category")["Amount"].sum()

    print("1.Category VS Amount chart")
    print("2.Date VS Amount chart")
    x=input("Enter Type:")
    if(x=="1"):
        plt.bar(cattotals.index,cattotals.values, label="Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.show()
    elif(x=="2"):
        plt.bar(datotals.index,datotals.values,label="Expenses by date")
        plt.xlabel("Date")
        plt.ylabel("Total Amount")
        plt.show()

if __name__ == "__main__":
    main()