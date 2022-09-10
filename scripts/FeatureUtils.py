def check_if_promo_month(row):

    intervals = {0:[], 1:[1,4,7,10], 2:[2,5,8,11], 3:[3,6,9,12]}
    try:        
        if row['Promo2Open'] and row['Month'] in intervals[row['PromoInterval']]:
            return 1
        else:
            return 0
    except Exception:
        return 0

def add_promo_cols(df):
    # Months since Promo2 was open
    df['Promo2Open'] = 12 * (df.Year - df.Promo2SinceYear) +  (df.WeekOfYear - df.Promo2SinceWeek)*7/30.5
    df['Promo2Open'] = df['Promo2Open'].map(lambda x: 0 if x < 0 else x).fillna(0) * df['Promo2']
    # Whether a new round of promotions was started in the current month
    df['IsPromo2Month'] = df.apply(check_if_promo_month, axis=1) * df['Promo2']
    return df

def add_comp_months(df):
    df['CompetitionOpen'] = 12 * (df.Year - df.CompetitionOpenSinceYear) + (df.Month - df.CompetitionOpenSinceMonth)
    df['CompetitionOpen'] = df['CompetitionOpen'].map(lambda x: 0 if x < 0 else x).fillna(0)
    
    return df
    