import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = list(CITY_DATA.keys())
MONTH_DICT = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June'}
DAY_DICT = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
MONTHS = ['All','January','February','March','April','May','June']
DAYS = ['All','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

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
    city = input('\nPlease select which city you would like to explore. (Chicago, New York City or Washington).\n')

    while city.lower() not in CITIES:
        city = input('\nInvalid city name entered, please choose from the 3 cities provided: Chicago, New York City or Washington.\n')
        
    print('\nCity selected: '+ city.title())
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nPlease select the month you would like to explore. (All, January, February, March, April, May or June).\n')
    while month.title() not in MONTHS:
        month = input('\nInvalid month entered, please select from the provided list. (All, January, February, March, April, May or June).\n')

    print('\nMonth selected: '+ month.title())
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('\nPlease select the day of week you would like to explore. (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).\n')

    while day.title() not in DAYS:
        day = input('\nInvalid day of week entered, please select from the provided list. (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).\n')
    
    
    print('\nDay of week selected: '+ day.title())
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
    #get filename based on user input
    filename = CITY_DATA[city.lower()]
    
    #Read file
    df = pd.read_csv('./'+filename)
    
    #convert column type into datetime in dataframe
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    print(df.head())
    
    if month.lower() != 'all':
        if month.lower() == 'january':
            df = df.loc[(df['Start Time'].dt.month == 1)]
        elif month.lower() == 'february':
            df = df.loc[(df['Start Time'].dt.month == 2)]
        elif month.lower() == 'march':
            df = df.loc[(df['Start Time'].dt.month == 3)]
        elif month.lower() == 'april':
            df = df.loc[(df['Start Time'].dt.month == 4)]
        elif month.lower() == 'may':
            df = df.loc[(df['Start Time'].dt.month == 5)]
        elif month.lower() == 'june':
            df = df.loc[(df['Start Time'].dt.month == 6)]
    
    if day.lower() != 'all':
        if day.lower() == 'monday':
            df = df.loc[(df['Start Time'].dt.dayofweek == 0)]
        elif day.lower() == 'tuesday':
            df = df.loc[(df['Start Time'].dt.dayofweek == 1)]
        elif day.lower() == 'wednesday':
            df = df.loc[(df['Start Time'].dt.dayofweek == 2)]
        elif day.lower() == 'thursday':
            df = df.loc[(df['Start Time'].dt.dayofweek == 3)]
        elif day.lower() == 'friday':
            df = df.loc[(df['Start Time'].dt.dayofweek == 4)]
        elif day.lower() == 'saturday':
            df = df.loc[(df['Start Time'].dt.dayofweek == 5)]
        elif day.lower() == 'sunday':
            df = df.loc[(df['Start Time'].dt.dayofweek == 6)]
    

    df.reset_index(drop=True, inplace=True)
    
    #df = df.sort_index()
    #print(df.head())
    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel.
    Args:
        (df) df - DataFrame
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    s = df.groupby(df['Start Time'].dt.month).size().nlargest(1)
    s.index.name = 'Month'
    new_df = pd.DataFrame({'Month':s.index, 'Count':s.values})
    
            
    if month.lower() == 'all':
     
      println='Top usage month in city ' + city.title() + ' was: ' + MONTH_DICT.get(new_df['Month'].values[0])
      print(println)
    
    println='Total usage in ' + MONTH_DICT.get(new_df['Month'].values[0]) + ' was: ' + str(new_df['Count'].values[0]) 
    print(println)
     # print(MONTH_DICT.get(new_df['Month'].values[0]))

    # TO DO: display the most common day of week
    s = df.groupby(df['Start Time'].dt.dayofweek).size().nlargest(1)
    s.index.name = 'Day'
    new_df = pd.DataFrame({'Day':s.index, 'Count':s.values})
    if day.lower() == 'all':
        if month.lower() != 'all':
          println='\nTop usage day of week of ' + month.title() + ' in city ' + city.title() + ' was: ' + DAY_DICT.get(new_df['Day'].values[0])
          print(println)
        else:
          println='\nTop usage day of week all time in city ' + city.title() + ' was: ' + DAY_DICT.get(new_df['Day'].values[0])
          print(println)
      
    println='Total usage on '+ DAY_DICT.get(new_df['Day'].values[0]) + ' was: ' + str(new_df['Count'].values[0]) 
    print(println)

    # TO DO: display the most common start hour
    s = df.groupby(df['Start Time'].dt.hour).size().nlargest(1)
    s.index.name = 'Hour'
    new_df = pd.DataFrame({'Hour':s.index, 'Count':s.values})
    
    if day.lower() != 'all':
        if month.lower() != 'all':
          println='\nTop usage hour every ' + day.title() + ' of ' + month.title() + ' in city ' + city.title() + ' was: ' + str(new_df['Hour'].values[0])
          print(println)
        else:
          println='\nTop usage hour every ' + day.title() + ' of all months in city ' + city.title() + ' was: ' + str(new_df['Hour'].values[0])
          print(println)
    else:
      println='Top usage hour all time in city ' + city.title() + ' was: ' + str(new_df['Hour'].values[0])
      print(println)
        
    println='Total usage on '+ str(new_df['Hour'].values[0]) + ' hundred was: ' + str(new_df['Count'].values[0]) 
    print(println)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    s = df.groupby(['Start Station']).size().nlargest(1)
    s.index.name = 'Start Station'
    new_df = pd.DataFrame({'Start Station':s.index, 'Count':s.values})
    
    println = '\nThe most popular Start Station in city ' + city.title() + ' is: ' + new_df['Start Station'].values[0]
    print(println)
    if month.lower() != 'all':
      println = 'There were ' + str(new_df['Count'].values[0]) + ' times where people departs from this station in the month of '+ month.title() + '.'
      print(println)
    else:
      println = 'There were ' + str(new_df['Count'].values[0]) + ' times where people departs from this station all time.'
      print(println)

    # TO DO: display most commonly used end station
    s = df.groupby(['End Station']).size().nlargest(1)
    s.index.name = 'End Station'
    new_df = pd.DataFrame({'End Station':s.index, 'Count':s.values})
    
    println = '\nThe most popular Destination in city ' + city.title() + ' is: ' + new_df['End Station'].values[0]
    print(println)
    if month.lower() != 'all':
      println = 'There was ' + str(new_df['Count'].values[0]) + ' times where people comes to this station in the month of '+ month.title() + '.'
      print(println)
    else:
      println = 'There was ' + str(new_df['Count'].values[0]) + ' times where people comes to this station all time.'
      print(println)
    
    
    # TO DO: display most frequent combination of start station and end station trip
    s = df.groupby(['Start Station','End Station']).size().nlargest(1)
    s.index.name = 'Start End Station'
    new_df = pd.DataFrame({'Start End Station':s.index, 'Count':s.values})
    
    println = '\nMost of the people departs from station ' + new_df['Start End Station'].values[0][0] + ' to station ' + new_df['Start End Station'].values[0][1] + ' in the city ' + city.title() + '.'
    print(println)
    println = 'And this happened ' +  str(new_df['Count'].values[0]) + ' times!'
    print(println)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_second = df['Trip Duration'].sum();
    hour=total_second//3600
    minute=(total_second%3600)//60
    second=(total_second%3600)%60
    println = 'Total travel time in city ' + city.title() + ' is ' + str(total_second) + ' seconds.'
    print(println)
    println = 'OR ' + str(hour) + ' hours ' + str(minute) + ' minutes and ' + str(second) + 'seconds.'
    print(println)

    # TO DO: display mean travel time
    total_second = df['Trip Duration'].mean();
    hour=total_second//3600
    minute=(total_second%3600)//60
    second=(total_second%3600)%60
    println = '\nMean travel time in city ' + city.title() + ' is ' + str(total_second) + ' seconds.'
    print(println)
    println = 'OR ' + str(hour) + ' hours ' + str(minute) + ' minutes and ' + str(second) + 'seconds.'
    print(println)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    s = df.groupby(['User Type']).size()
    s.index.name = 'User Type'
    new_df = pd.DataFrame({'User Type':s.index, 'Count':s.values})
        
   # print(new_df)
    println = 'User type statistic in city ' + city.title() + ': '
    print(println)
    for index, row in new_df.iterrows():
        user_type = row['User Type']
        user_type_count = row['Count']
        println = user_type + ' : ' + str(user_type_count)
        print(println)
    # TO DO: Display counts of gender
    try:  
      s = df.groupby(['Gender']).size()
      s.index.name = 'Gender'
      new_df = pd.DataFrame({'Gender':s.index, 'Count':s.values})
        
   # print(new_df)
    
      println = '\nGender statistic in city ' + city.title() + ': '
      print(println)
      for index, row in new_df.iterrows():
          gender = row['Gender']
          gender_count = row['Count']
          println = gender + ' : ' + str(gender_count)
          print(println)
    except KeyError:
        print('\nNo Gender information available.')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      s = df.groupby(['Birth Year']).size()
      s.index.name = 'Birth Year'
      new_df = pd.DataFrame({'Birth Year':s.index, 'Count':s.values})
      latest_birth_year_df = new_df.nlargest(1,'Birth Year')
      earliest_birth_year_df = new_df.nsmallest(1,'Birth Year')
    
      latest_birth_year = str(int(latest_birth_year_df['Birth Year'].values))
      latest_birth_year_count = str(int(latest_birth_year_df['Count'].values))
      earliest_birth_year = str(int(earliest_birth_year_df['Birth Year'].values))
      earliest_birth_year_count = str(int(earliest_birth_year_df['Count'].values))
    
      println = '\nBirth year statistic of city ' + city.title() + ' : '
      print(println)
    
      println = 'Earliest birth year :' + earliest_birth_year 
      print(println)
      println = 'There''s ' + str(earliest_birth_year_count) + ' users born in year ' + earliest_birth_year 
      print(println)
    
      println = '\nMost recent birth year :' + latest_birth_year 
      print(println)
      println = 'There''s ' + str(latest_birth_year_count) + ' users born in year ' + latest_birth_year 
      print(println)
    
      for index, row in new_df.nlargest(1,'Birth Year').iterrows():
        common_birth_year = str(int(row['Birth Year']))
        common_birth_year_count = row['Count']
        println = '\nMost common birth year :' + common_birth_year 
        print(println)
        println = 'There''s ' + str(int(common_birth_year_count)) + 'users born in year ' + common_birth_year 
        print(println)

    except KeyError:
      print('\nNo Birth Year information available.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    """Displays raw data on bikeshare users."""
    start_time = time.time()
    start_rn = 0
    raw = input('\nDo you want to check out raw data? (Y/n)\n')
    while True:
      if raw.upper() == 'Y':
        while True:
          rn = input('How many rows of raw data you would like to check?\n')
          try:
              rn = int(rn)
              break
          except ValueError:
              print('Invalid input, please key in an integer.')
          except rn <= 0:
              print('Invalid input, please key in a positive number.')
      
        start_rn = start_rn
        end_rn = start_rn + rn -1
        print(df.loc[start_rn:end_rn])
        start_rn = start_rn + rn
      else:
        break
        
      raw = input('\nDo you want to check out more raw data? (Y/n)\n')
          
        
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
                
        #time_stats(df, city, month, day)
        #station_stats(df, city, month, day)
        #trip_duration_stats(df, city, month, day)
        #user_stats(df, city, month, day)
        
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
