import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months = ['january', 'february', 'march','april', 'may', 'june','all']

Days = ['all' ,'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = CITY_DATA[input("write the name of city (chicago, new york city, washington) : ").lower()]
            break
        except :
            print('ops you entre a invalid value!')
            print('please inter one of the choices!')
    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = Months[Months.index(input("write the name of the month you want to explore (january, february, march, april, may, june or all) : ").lower())]
            break
        except :
            print('ops you entre a invalid value!')
            print('please enter one of the choices!')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = Days[Days.index(input("write the day of the week you want to explore (monday, tuesday, wednesday, thursday, friday, saturday, sunday) or type (all) if you eant to explore all data ) : ").lower())]
            break
        except :
            print('ops you entre a invalid value!')
            print('please inter one of the choices!')

    print("you selected city: {} , month: {} ,day: {} ".format(city, month, day))
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
    # load data file into a dataframe
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = Months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    if month == 'all':
        popular_month = Months[df['month'].mode()[0]-1]
        print('the most comman month: {}'.format(popular_month))

    # TO DO: display the most common day of week
    if day == 'all':
        popular_day = df['day_of_week'].mode()[0]
        print('the most comman day: {}'.format(popular_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour        
    popular_hour = df['hour'].mode()[0]
    print('the most comman hour : {}:00 hrs'.format(popular_hour))

          
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    count_popular_start_station = df['Start Station'].value_counts()[0]
    print('the most comman used start staion: {}  Count:{} .'.format(popular_start_station, count_popular_start_station ))
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    count_popular_end_station = df['End Station'].value_counts()[0]
    print('the most comman used END staion: {}  Count:{} .'.format(popular_end_station, count_popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['frequent'] = "start: " + df['Start Station']+ "  and end with: " + df['End Station']
    popular_frequent = df['frequent'].mode()[0]
    count_popular_frequent = df['frequent'].value_counts()[0]
    print('The most frequent {}    Count:{} .'.format(popular_frequent, count_popular_frequent))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    df['travel_time'] =  pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    total_travel_time = df['travel_time'].sum()
    print("Total travel time : {}".format(total_travel_time))
    # TO DO: display mean travel time
   
    Mean_travel_time = df['travel_time'].mean()
    print("Mean travel time : {}".format(Mean_travel_time))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    print(city)
    if city != 'washington.csv':
    
        gender = df['Gender'].value_counts()
        print(gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_comman_year_of_birth = df['Birth Year'].mode()[0]
    
        print('Earliest year of birth: {}'.format(earliest_year_of_birth))
        print('Most recent year of birth: {}'.format(most_recent_year_of_birth))
        print('Most comman year of birth: {}'.format(most_comman_year_of_birth))
    
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   

def display_data(df):
    i = -5
    display_5_raws = input('\Do you want to see 5 rows of data? Enter yes or no.\n').lower()
    if display_5_raws == 'yes':  
        while True :
            i +=5
            with pd.option_context('display.max_columns', None):
                print(df[i:i+5])    
            display_again = input('\Do you want to see another 5 rows of data? Enter yes or no.\n').lower()
            if display_again != 'yes':
                break
    
def main():
    city, month, day = get_filters()
    df = load_data(city, month, day)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    display_data(df)
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() == 'yes':
        main()



city, month, day = get_filters()
df = load_data(city, month, day)
time_stats(df)
station_stats(df)
trip_duration_stats(df)
user_stats(df)
display_data(df)

restart = input('\nWould you like to restart? Enter yes or no.\n')
if restart.lower() == 'yes':
    main()
      
      
      # gameeeeeeeeeeeeeeeeed


