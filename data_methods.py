import csv
import sys
import pandas as pd


def write_expense(input_data):
    with open('database.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(input_data)  # Use writer.writerow for a single row


df = pd.read_csv("database.csv")

def view_by_categ(user_month, user_year):
    df1 = df[
        (pd.to_datetime(df['Date']).dt.year == int(user_year)) &
        (pd.to_datetime(df['Date']).dt.strftime('%B') == str(user_month))
    ]

    if len(df1.Date.value_counts()) > 0:
        gdf1 = df1.groupby(['Category'])['Amount'].sum().to_string()
        return gdf1
    else:
        return "There is no data\n available for this time period"


def view_by_date(user_month, user_year):
    df1 = df[
        (pd.to_datetime(df['Date']).dt.year == int(user_year)) &
        (pd.to_datetime(df['Date']).dt.strftime('%B') == str(user_month))
        ]

    if len(df1.Date.value_counts()) > 0:
        gdf1 = df1.groupby(['Date'])['Amount'].sum().to_string()
        return gdf1
    else:
        return "There is no available\n data for this time period"


def view_total():
    total = df["Amount"].sum()
    return total
