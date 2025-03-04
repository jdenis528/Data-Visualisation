'''
    Contains some functions to preprocess the data used in the visualisation.
'''


def round_decimals(my_df):
    '''
        Rounds all the numbers in the dataframe to two decimal points

        args:
            my_df: The dataframe to preprocess
        returns:
            The dataframe with rounded numbers
    '''
    # TODO : Round the dataframe
    return None


def get_range(col, df1, df2):
    '''
        An array containing the minimum and maximum values for the given
        column in the two dataframes.

        args:
            col: The name of the column for which we want the range
            df1: The first dataframe containing a column with the given name
            df2: The first dataframe containing a column with the given name
        returns:
            The minimum and maximum values across the two dataframes
    '''
    # TODO : Get the range from the dataframes
    # Check if the column exists in both dataframes
    if col not in df1.columns or col not in df2.columns:
        raise ValueError(f"Column '{col}' not found in one or both dataframes")

    # Get the minimum and maximum values from both dataframes
    min_val = min(df1[col].min(), df2[col].min())
    max_val = max(df1[col].max(), df2[col].max())

    # Return the range as a list
    return [min_val, max_val]
    


def combine_dfs(df1, df2):
    '''
        Combines the two dataframes, adding a column 'Year' with the
        value 2000 for the rows from the first dataframe and the value
        2015 for the rows from the second dataframe

        args:
            df1: The first dataframe to combine
            df2: The second dataframe, to be appended to the first
        returns:
            The dataframe containing both dataframes provided as arg.
            Each row of the resulting dataframe has a column 'Year'
            containing the value 2000 or 2015, depending on its
            original dataframe.
    '''
    # TODO : Combine the two dataframes
    # Add the 'Year' column to each dataframe
    df1['Year'] = 2000
    df2['Year'] = 2015

    # Concatenate the two dataframes
    combined_df = pd.concat([df1, df2], ignore_index=True)

    return combined_df


def sort_dy_by_yr_continent(my_df):
    '''
        Sorts the dataframe by year and then by continent.

        args:
            my_df: The dataframe to sort
        returns:
            The sorted dataframe.
    '''
    # TODO : Sort the dataframe
    sorted_df = my_df.sort_values(by=['Year', 'Continent'], ascending=[True, True])

    return sorted_df
 
