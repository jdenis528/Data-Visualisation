'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    # Iterate over each column in the dataframe
    dataframe['Date_Plantation'] = pd.to_datetime(dataframe['Date_Plantation'])
                
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    
    dataframe = dataframe[(dataframe['date_column'].dt.year >= start) & (dataframe['date_column'].dt.year <= end)]
    
    return dataframe
    



def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    summary_df = dataframe.groupby(['neighborhood', 'year']).size().reset_index(name='Counts')
   

    
    return summary_df
   
   
  


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0
    
    heatmap_df = yearly_df.pivot_table(
        index='Arrond_Nom',
        columns='Date_Plantation',
        values='Trees_Planted'
    )fillna(0)
    
    return heatmap_df 
         
    
    



def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    df_filtered = dataframe[
        (dataframe['Arrond_Nom'] == arrond) &
        (dataframe['Date_Plantation'] == year)
        ]
    
    daily_tree_count = df_filtered.groupby('Date_Plantation')['Trees_Planted'].sum()
    
         
    
    # Convert the 'Date' column to datetime (if it's not already in datetime format)
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])

    # Return the daily tree count data
    return daily_tree_count
    
