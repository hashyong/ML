import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MON_DATA = { 1 : 'january',
             2 : 'february',
             3 : 'march',
             4 : 'april',
             5 : 'may',
             6 : 'june'}

WEEK_DATA = { 1 : 'monday',
              2 : 'tuesday',
              3 : 'wednesday',
              4 : 'thursday',
              5 : 'friday',
              6 : 'saturday',
              0 : 'sunday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    bRet = True
    while bRet:
      city = input("Enter your input: chicago, new york city, washington \n")
      cityList = ["chicago", "new york city", "washington"]
      if city in cityList:
        bRet = False

    # TO DO: get user input for month (all, january, february, ... , june)
    bRet = True
    while bRet:
      month = input("Enter your input: all, january, february, march, april, may, june \n")
      monthList = ["all", "january", "february", "march", "april", "may", "june"]
      if month in monthList:
        bRet = False

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    bRet = True
    while bRet:
      day = input("Enter your input: all, monday, tuesday, ... sunday \n")
      dayList = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
      if day in dayList:
        bRet = False


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    index = 0

    if month == 'january':
        index = 1
    elif month == 'february':
        index = 2
    elif month == 'march':
        index = 3
    elif month == 'april':
        index = 4
    elif month == 'may':
        index = 5

    if month != 'all':
        res = df.mul(df['Start Time'].apply(lambda x: time.strptime(x,'%Y-%m-%d %H:%M:%S').tm_mon == index), axis=0)
        df = res.loc[res["Trip Duration"] != 0]

    if day == 'monday':
        index = 1
    elif day == 'tuesday':
        index = 2
    elif day == 'wednesday':
        index = 3
    elif day == 'thursday':
        index = 4
    elif day == 'friday':
        index = 5
    elif day == 'saturday':
        index = 6
    elif day == 'sunday':
        index = 0

    if day != 'all':
        res = df.mul(df['Start Time'].apply(lambda x: time.strptime(x,'%Y-%m-%d %H:%M:%S').tm_wday == index), axis=0)
        df = res.loc[res["Trip Duration"] != 0]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    res = df['Start Time'].apply(lambda x: time.strptime(x,'%Y-%m-%d %H:%M:%S').tm_mon).value_counts()
    maxMonth = res.max()
    monIndex = res.loc[res == maxMonth].index.values[0]

    print("display the most common month:" + MON_DATA[monIndex])


    # TO DO: display the most common day of week
    res = df['Start Time'].apply(lambda x: time.strptime(x,'%Y-%m-%d %H:%M:%S').tm_wday).value_counts()
    maxWeek = res.max()
    weekIndex = res.loc[res == maxWeek].index.values[0]

    print("display the most common day of week:" + WEEK_DATA[weekIndex])

    # TO DO: display the most common start hour
    res = df['Start Time'].apply(lambda x: time.strptime(x,'%Y-%m-%d %H:%M:%S').tm_hour).value_counts()
    maxHour = res.max()
    hourIndex = res.loc[res == maxHour].index.values[0]

    print("display the most common start hour:" + str(hourIndex))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    res = df['Start Station'].value_counts()
    maxStart = res.max()
    startIndex = res.loc[res == maxStart].index.values[0]

    print("display most commonly used start station:" + startIndex)


    # TO DO: display most commonly used end station
    res = df['End Station'].value_counts()
    maxEnd = res.max()
    endIndex = res.loc[res == maxEnd].index.values[0]

    print("display most commonly used end station:" + endIndex)


    # TO DO: display most frequent combination of start station and end station trip
    res = (df['Start Station'] + df['End Station']).value_counts()
    maxCom = res.max()
    maxIndex = res.loc[res == maxCom].index.values[0]

    print("display most frequent combination of start station and end station trip:" + maxIndex)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    res = df['Trip Duration'].apply(lambda x:int(x)).describe()

    # TO DO: display total travel time
    print("display total travel time:%.1f" % res["count"])

    # TO DO: display mean travel time
    print("display mean travel time:%.1f" % res["mean"])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    res = df['User Type'].value_counts()
    print("Display counts of user types:" + str(res.count()))

    # TO DO: Display counts of gender
    res = df['Gender'].value_counts()
    print("Display counts of gender:" + str(res.count()))


    # TO DO: Display earliest, most recent, and most common year of birth
    res = df['Birth Year'].apply(lambda x:float(x)).describe()

    resNew = df['Birth Year'].value_counts()
    maxCom = resNew.max()
    maxIndex = resNew.loc[resNew == maxCom].index.values[0]

    print("Display earliest, most recent, and most common year of birth: %.1f, %.1f, %s" % (res["min"], res["max"], maxIndex))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
