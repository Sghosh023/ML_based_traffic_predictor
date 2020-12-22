
class Validation:
    def method_validation(self,df_test):
        # the feature columns of the training dataset
        columns = ['holiday','temp','rain_1h','snow_1h','clouds_all','weather_main','date_time']
        # available list of holidays in the training dataset
        holiday_values = ['None', 'Columbus Day', 'Veterans Day', 'Thanksgiving Day',
       'Christmas Day', 'New Years Day', 'Washingtons Birthday',
       'Memorial Day', 'Independence Day', 'Labor Day']
        # available list of different weather type in the training dataset
        weather_values = ['Clouds', 'Clear', 'Rain', 'Drizzle', 'Mist', 'Haze', 'Fog',
       'Thunderstorm', 'Snow', 'Squall', 'Smoke']
        cols = []
        # getting the number of rows of records in the uploaded file for bulk prediction
        x = df_test.shape[0]
        # dropping the columns which are not required from the uploaded file for bulk prediction
        for column in list(df_test.columns):
            if column not in columns:
                cols.append(column)

        df_test.drop(cols, axis=1, inplace=True)
        df_test.dropna(inplace=True) # dropping any nan values

        # check if the columns of the Dataset is matching with the required columns of our model prediction Dataset
        if list(df_test.columns) == columns:
            # check if the all the holiday values belong to the required set(subset) of holiday values
            if (all(x in holiday_values for x in list(df_test['holiday'].unique()))):
                df_test['holiday'] = df_test['holiday'].apply(lambda a: 0 if a == 'None' else 1)
            else:
                return "Bad data"
            # check if all the available values of weather_main belong to the required set of weather values
            if (all(x in weather_values for x in list(df_test['weather_main'].unique()))):
                print("Valid data")
            else:
                return "Bad data"

            #Date format checking
            for i in range(0,x):
                if (len(df_test['date_time'][i]) == 19 and df_test['date_time'][i][0:3] == '201' and
                        df_test['date_time'][i][4] == '-' and df_test['date_time'][i][10] == ' '):
                    pass
        else:
            return "Data not Valid"

        return df_test




