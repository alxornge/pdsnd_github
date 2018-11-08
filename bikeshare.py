import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv','philadelphia.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. Python code.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city=str(input('\nEnter a city '))
            if city.lower() not in ['chicago','new_york_city','washington','philadelphia']:
                raise ValueError
        except ValueError:
            print('Invalid input')
            continue
    # TO DO: get user input for month (all, january, february, ... , june)

        try:
            month=str(input('\nEnter a month '))
            if month.lower() not in ['all','january','february','march','april','may','june']:
                raise ValueError

        except ValueError:
            print('Invalid input')
            continue


    #Get user input for day of week (all, monday, tuesday, ... sunday)

        try:
            day=str(input('\nEnter a day '))
            if day.lower() not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
                raise ValueError
        except ValueError:
            print('Invalid input')
            continue


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
    filename=city.lower()+'.csv'
    df=pd.read_csv(filename)
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
    df['st_hour']=df['Start Time'].dt.hour
    if month.lower()!='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]

    if day.lower()!='all':
        df[df['day']==day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Display the most common month
    pop_month=df['month'].mode()[0]
    months=['january','february','march','april','may','june']
    print("\nThe most common month is {}" .format(months[pop_month-1]))

    #Display the most common day of week
    pop_day=df['day'].mode()[0]
    print("\nThe most common day of the week is {}" .format(pop_day))
    #Display the most common start hour
    pop_hr=df['st_hour'].mode()[0]
    print("\nThe most common start hour is {}" .format(pop_hr))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip. Part of the python project"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Display most commonly used start station
    pop_start=df['Start Station'].mode()[0]
    print("\nThe most commonly used start station is {}" .format(pop_start))
    #Display most commonly used end station
    pop_end=df['End Station'].mode()[0]
    print("\nThe most commonly used end station is {}" .format(pop_end))
    #Display most frequent combination of start station and end station trip
    stcomb=df['Start Station']+', '+df['End Station']
    frqcomb=stcomb.mode()[0]
    print("\nThe most frequent combinatation of start and end station is {}" .format(frqcomb))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    tot=df['Trip Duration'].sum()
    totdur=tot/3600
    print("\nTotal travel time is {}" .format(totdur),'hrs')
    # Display mean travel time
    mean=df['Trip Duration'].mean()
    totmean=mean/3600
    print("\nMean travel time is {}" .format(totmean),'hrs')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_type=df['User Type'].value_counts()
    print("\nFollowing is the distribution of user type {}".format(user_type))

    #Display counts of gender. Data file for Washington does not have Gender or Birth Year data
    if city.lower()!='washington':
        #Display earliest, most recent, and most common year of birth
        eyb=df['Birth Year'].min()
        print("\nThe earliest year of birth is {}" .format(eyb))
        ryb=df['Birth Year'].max()
        print("\nThe latest year of birth is {}" .format(ryb))
        cyb=df['Birth Year'].mode()[0]
        print("\nThe most common year of birth is {}" .format(cyb))
        gender=df['Gender'].value_counts()
        print("\nFollowing is the distribution of gender \n{}".format(gender))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        while True:
            preview=input('\nDo you want to see a preview of the raw dat file? ')
            if preview.lower()!='yes':
                break
            else:
                fnm=input('Please enter the name of the city for which you wish to preview the raw data')+'.csv'
                df=pd.read_csv(fnm)
                print(df.head())

        city, month, day = get_filters()

        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
