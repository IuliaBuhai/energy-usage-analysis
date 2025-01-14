import pandas as pd

def clean_data(df):
    # Select the columns 
    selected_columns = [
        'COMMUNITY AREA NAME', 'CENSUS BLOCK', 'KWH JANUARY 2010', 'KWH FEBRUARY 2010',
        'KWH MARCH 2010', 'KWH APRIL 2010', 'KWH MAY 2010', 'KWH JUNE 2010',
        'KWH JULY 2010', 'KWH AUGUST 2010', 'KWH SEPTEMBER 2010', 'KWH OCTOBER 2010',
        'KWH NOVEMBER 2010', 'KWH DECEMBER 2010', 'TOTAL KWH'
    ]
    
    # Keep only selected columns
    df_selected = df[selected_columns]
    
    # removing missing values
    df_selected.dropna(inplace=True)
    
    return df_selected
