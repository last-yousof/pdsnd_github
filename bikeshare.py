import time
import pandas as pd
import numpy as np
import csv

# List of cities
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# List of months
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

# List of weekdays
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! The cities are Chicago, New York & Washington')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Please specify city (chicago, new york city, washington)')
    city=input().lower()
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        print('You entered an invalid city, please specify city (chicago, new york city, washington)')
        city=input().lower()
    

    # TO DO: get user input for month (all, january, february, ... , june)
    print('Please specify month (all, january, february, ... , june)')
    month=input().lower()
    while month != 'all' and month != 'january' and month != 'febuary' and month != 'march' and month != 'april' and month != 'may' and  month != 'june':
        print('You entered an invalid month, please specify month (all, january, february, ... , june)')
        month=input().lower()
        
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Please specify day (all, monday, tuesday, ... sunday)')
    day=input().lower()
    while day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday':
        print('you entered an invalid day, please specify day (all, monday, tuesday, ... sunday)')
        day=input().lower()


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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel in the cities"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month from the specified data is: " + MONTH_DATA[common_month].title())

    
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of the week from the specified data is: " + common_day_of_week)
    

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour of the day from the specified data is: " + str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station from the specified data is: " + common_start_station)
    

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station from the specified data is: " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given specified data is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given specified data is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the given specified data is: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':    
    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given specified data is: \n" + str(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth from the given specified data is: {}\n'.format(earliest_birth))
        print('Most recent birth from the given specified data is: {}\n'.format(most_recent_birth))
        print('Most common birth from the given specified data is: {}\n'.format(most_common_birth) )

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

        
        
def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data specified by month and day
    """
    next = 0
    while True:
        view_raw_data=input('Would you like to view next five rows of raw data? Enter yes or no.\n').lower()

        while view_raw_data != 'yes' and view_raw_data != 'no':
            view_raw_data=input('You have entered invalid answer, would you like to view next five rows of raw data? Enter yes or no.\n')    
        
        if view_raw_data== 'yes':
            #printing rows
            print(df.iloc[next:next+5])
            next=next+5

        else:
            break
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart != 'yes' and restart != 'no':
            restart=input('You have entered invalid answer, would you like to restart? Enter yes or no.\n')    
        
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
