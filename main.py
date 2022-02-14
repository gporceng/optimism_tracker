import matplotlib
import pandas
import datetime as date

def main():
    print("Welcome to the Optimism Tracker.\nPlease select your choice from below using the terminal.")
    print("--------------------------\n")
    cur_date = date.datetime.now()

    print("Todays date is ", cur_date.month,"-", cur_date.day, "-" , cur_date.year, "\n")

if __name__ == "__main__":
    main()
