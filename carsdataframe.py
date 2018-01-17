dssasken@gmail.com
datascience2811

  df_cars1 = pd.DataFrame({'name': ['bmw', 'lexus', 'ferrari', 'mercedez'],
                                'colour': ['red', 'white', 'black', 'blue'],
                                'year': ['2012', '2014', '2011', '2016'],
                               },index=[0, 1, 2,3])
    df_cars2 = pd.DataFrame({'name': ['audi', 'hyundai', 'maruti', 'ford'],
                                'colour': ['grey', 'brown', 'yellow', 'white'],
                                'year': ['2011', '2014', '2012', '2015'],
                               },index=[4, 5,6,7])
    df_car_details = pd.DataFrame({'country': ['germany', 'france', 'US', 'UK'],
                                'units': ['2500', '4700', '3250', '6470'],
                                'variant': ['diesel', 'petrol', 'petrol', 'diesel'],
                               },index=[0, 1,2,3])


    # Dataframes print
   
    #'''
    print('\nCars from datafrme 1\n')
    print(df_cars1)
    print('\nCars from dataframe 2\n')
    print(df_cars2)
    print('\n Car details from dataframe 3\n')
    print(df_car_details)
   # '''




  

df_subject = pd.DataFrame({'SectionId': ['Id1', 'Id2', 'Id3', 'Id4'],
                                'Subjects': ['Maths', 'Science', 'Computer', 'History'],
                                'Semester': ['First','Second','First','Third']
                               },index=[0, 1, 2,3])

df_students = pd.DataFrame({'ClassId': ['Id4', 'Id1', 'Id6', 'Id2'],
                               'Students': ['John', 'Trevor', 'David', 'Chris'],
                               },index=[4,5,6,7])
merge_frame= pd.merge(df_subject,df_students,how='right',left_on='SectionId',right_on='ClassId')
print("\nSubjects dataframe\n")
