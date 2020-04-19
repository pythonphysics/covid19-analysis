"""Graphical Analysis of COVID19 based on the countries."""
import datetime as dt

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

# Data extracted from John Hopkins github files
COUNTRY_TIME_SERIES_DATA = "~/covid19/covid-19/data/countries-aggregated.csv"

COVID19 = pd.read_csv(COUNTRY_TIME_SERIES_DATA, sep=",")

# Added an "Active", "Recovery Percentage -timeseries",
# "Death Percentage -timeseries" cases column for the
# countries time-series data
COVID19["Active"] = COVID19["Confirmed"] - (COVID19["Recovered"] +
                                            COVID19["Deaths"])

COVID19["Death_Percentage"] = round(
    (COVID19["Deaths"] / COVID19["Confirmed"]) * 100, 2)

COVID19["Recovery_Percentage"] = round(
    (COVID19["Recovered"] / COVID19["Confirmed"]) * 100, 2)


def country_graph(country):
    """
    A function which takes in one argument 'country' and returns
    the graph of the recovered and active cases for that country
    as well as the deathtoll and the recovered cases for the COVID-19
    time series data.
    """
    country_name = country
    country_data = COVID19[COVID19["Country"] == country]
    country_date = [
        dt.datetime.strptime(i, "%Y-%m-%d").date()
        for i in country_data["Date"]
    ]
    country_recovered = country_data["Recovered"]
    country_deaths = country_data["Deaths"]
    country_confirmed = country_data["Confirmed"]
    country_active = country_data["Active"]
    # Plots start below
    fig, AX = plt.subplots()
    AX.plot(country_date,
            country_confirmed,
            marker="*",
            linestyle=":",
            label="Confirmed")
    AX.plot(country_date,
            country_active,
            marker="x",
            linestyle="-.",
            label="Active")
    AX.plot(country_date,
            country_deaths,
            marker=".",
            linestyle="--",
            label="Deaths")
    AX.plot(country_date,
            country_recovered,
            marker="4",
            linestyle="-",
            label="Recovered")
    AX.legend()
    AX.set_xlabel("Date", size=16)
    AX.set_ylabel("Population", size=16)
    fig.suptitle(f"{country_name} COVID-19 Trend", size=20)

    # Formatting for the x-axis dates
    date_format = mdates.DateFormatter("%d-%b-%y")
    AX.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    AX.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    plt.show()


def country_statistics(country):
    """
    Function to calculate the time-series variation of the death
    percentage of countries, recovery percentage.
    """

    country_name = country
    country_data = COVID19[COVID19["Country"] == country]
    country_date = [
        dt.datetime.strptime(i, "%Y-%m-%d").date()
        for i in country_data["Date"]
    ]
    # country_recovered = country_data["Recovered"]
    # country_deaths = country_data["Deaths"]
    # country_confirmed = country_data["Confirmed"]
    # country_active = country_data["Active"]
    country_death_percentage = country_data["Death_Percentage"]
    country_recovery_percentage = country_data["Recovery_Percentage"]
    # Plotting Starts below
    fig, AX = plt.subplots()
    AX.plot(
        country_date,
        country_recovery_percentage,
        marker="x",
        linestyle="-.",
        label="Recovery Percentage",
    )
    AX.plot(
        country_date,
        country_death_percentage,
        marker="4",
        linestyle="-",
        label="Death percentage",
    )
    AX.legend()
    AX.set_xlabel("Date", size=16)
    AX.set_ylabel("Percentage Pop.", size=16)
    fig.suptitle(
        f"{country_name} COVID-19 Trend of Death and Recovery Percentage",
        size=20)

    # Formatting for the x-axis dates
    date_format = mdates.DateFormatter("%d-%b-%y")
    AX.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    AX.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    plt.show()


COUNTRIES = COVID19["Country"][0:185]
COUNTRIES2 = COVID19["Country"][184:370]
i = 0
j = 185
while i < 185 and j < 370:
    if COUNTRIES[i] == COUNTRIES2[j]:
        print(COUNTRIES[i])
        print(COUNTRIES2[j])
        print("Ok, Passed")
    else:
        print("Not Okay, No GO")
    i += 1
    j += 1
# for i in COUNTRIES:
#     for j in COUNTRIES2:
#         if (i == j):
#             print("ok")
#         else:
#             print("not ok")
# NAME_OF_COUNTRY = str(input("Which country would you like the graph of ?"))
# country_graph(NAME_OF_COUNTRY)
# country_statistics(NAME_OF_COUNTRY)

# Malaysian COVID-19 Cases data
MSIA_DATA = COVID19[COVID19["Country"] == "Malaysia"]

MSIA_DATE = [
    dt.datetime.strptime(i, "%Y-%m-%d").date() for i in MSIA_DATA["Date"]
]
MSIA_RECOVERED = MSIA_DATA["Recovered"]
MSIA_DEATHS = MSIA_DATA["Deaths"]
MSIA_CONFIRMED = MSIA_DATA["Confirmed"]
MSIA_ACTIVE = MSIA_DATA["Active"]

MSIA_DEATHS_LIST = list(MSIA_DEATHS)
MSIA_CONFIRMED_LIST = list(MSIA_CONFIRMED)
MSIA_RECOVERED_LIST = list(MSIA_RECOVERED)

# CUMMULATIVE_DEATH_PERCENTAGE = (MSIA_DEATHS_LIST[-1] /
# MSIA_CONFIRMED_LIST[-1]) * 100
# print(CUMMULATIVE_DEATH_PERCENTAGE)
