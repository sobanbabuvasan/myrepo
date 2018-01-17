import pandas as pd
import numpy as np



def concat_df(df_cars1,df_cars2,df_car_details):

    
    concat_frame = pd.concat([df_cars1,df_cars2],axis=0)
    print("\nConcatenated dataframe of cars on default axis 0\n")
    print('\n'+str(concat_frame)+'\n')

    concat_axis= pd.concat([df_cars1,df_cars2],axis=1)
    print("\nConcatenated dataframe of cars on axis 1 i.e. using columns as axis\n")
    print('\n'+str(concat_axis)+'\n')
    

    
    print("\nConcatenated dataframe of cars 1 with details on axis 1 i.e. using columns as axis\n")
    print pd.concat([df_cars1,df_car_details],axis=1)
    



def merge_df():

    df_subject = pd.DataFrame({'SectionId': ['Id1', 'Id2', 'Id3', 'Id4'],
                                'Subjects': ['Maths', 'Science', 'Computer', 'History'],
                                'Semester': ['First','Second','First','Third']
                               },index=[0, 1, 2,3])

    df_students = pd.DataFrame({'ClassId': ['Id4', 'Id1', 'Id6', 'Id2'],
                                'Students': ['John', 'Trevor', 'David', 'Chris'],
                               },index=[4,5,6,7])
    merge_frame= pd.merge(df_subject,df_students,how='right',left_on='SectionId',right_on='ClassId')
    print("\nSubjects dataframe\n")
    print('\n'+str(df_subject)+'\n')
    print("\nStudents dataframe\n")
    print('\n'+str(df_students)+'\n')
    print("\nMerged dataframe\n")
    print merge_frame




def join_df(df_cars1,df_cars2,df_car_details):

    #Joining Dataframe cars 2 to dataframe cars 1
    print  pd.DataFrame.join(df_cars1,df_cars2,lsuffix='_left',rsuffix='_right')
    print("\n")
    #Joining Dataframe cars 1 to dataframe cars 2
    print  pd.DataFrame.join(df_cars2,df_cars1,lsuffix='_left',rsuffix='_right')
    print("\n")
    # Joining dataframe car details to cars1 ,having same indexes
    print  pd.DataFrame.join(df_cars1,df_car_details)


def main():

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
   
    '''
    print('\nCars from datafrme 1\n')
    print(df_cars1)
    print('\nCars from dataframe 2\n')
    print(df_cars2)
    print('\n Car details from dataframe 3\n')
    print(df_car_details)
   '''



    #concat_df(df_cars1,df_cars2,df_car_details)
    #merge_df()
    join_df(df_cars1,df_cars2,df_car_details)



if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it
