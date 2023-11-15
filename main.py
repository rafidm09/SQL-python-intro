import mysql.connector

def Country_insert(pointer, my_DB):
    cname = input('Enter the country name: ')
    gld = input('Enter the number of all time gold medals won: ')
    slvr = input('Enter the number of all time silver medals won: ')
    brnz = input('Enter the number of all time bronze medals won: ')
    pointer.execute("""INSERT INTO Country(CName, AllTimeGold, AllTimeSilver, AllTimeBronze) values(%s,%s,%s,%s)""", (cname, gld, slvr, brnz))
    my_DB.commit()
    print('Data inserted successfully.')
    my_DB.close()

def Participant_insert(pointer, my_DB):
    olid = input('Enter Olympic ID: ')
    sex = input('Enter Sex: ')
    byear = input('Enter Birth Year: ')
    fgames = input('Enter the First Games: ')
    pointer.execute("""INSERT INTO PARTICIPANT(OlympicID, Sex, BirthYear, FirstGames) values(%s,%s,%s,%s)""", (olid,sex,byear,fgames))
    my_DB.commit()
    print('Data inserted successfully')
    my_DB.close()

def Athlete_insert(pointer, my_DB):
    olid = input('Enter Olympic ID: ')
    lname = input('Enter Last Name: ')
    fname = input('Enter First Name: ')
    country = input('Enter the country name: ')
    pointer.execute("""INSERT INTO PARTICIPANT(OlympicID, LName, FName, Country) values(%s,%s,%s,%s)""", (olid,lname,fname,country))
    my_DB.commit()
    print('Data inserted successfully')
    my_DB.close()


def Team_results_insert(pointer, my_DB):
    eid = input('Enter Event ID: ')
    team = input('Enter team: ')
    medal = input('Enter First Name: ') 
    pointer.execute("""INSERT INTO PARTICIPANT(EventID,Team,Medal) values(%s,%s,%s)""", (eid,team,medal))
    my_DB.commit()
    print('Data inserted successfully')
    my_DB.close()

def Coach_insert(pointer, my_DB):
        olname = input('Enter the OlympicID: ')
        ornt = input('Enter orientation: ')
    
        pointer.execute("""INSERT INTO Coach(OlympicID, Orientation) values(%s,%s)""", (olname, ornt))
        my_DB.commit()
        print('Data inserted successfully')
        my_DB.close()
    
def Team_insert(pointer, my_DB):
    tmid = input('Enter TeamID: ')
    mm1 = input('Enter Member1: ')
    mm2 = input('Enter Member2: ')
    mm3 = input('Enter Member3: ')
    mm4 = input('Enter Member4: ')
    mm5 = input('Enter Member5: ')
    mm6 = input('Enter Member6: ')
    pointer.execute("""INSERT INTO TeamID, Member1, Member2, Member3, Member4, Member5, Member6) values(%s,%s,%s,%s,%s,%s,%s)""", (tmid, mm1, mm2, mm3, mm4, mm5, mm6))
    my_DB.commit()
    print('Data inserted successfully')
    my_DB.close()
    

def Event_insert(pointer, my_DB):
    evntid = input('Enter the event ID: ')
    evntdt = input('Enter the event date: ')
    loca = input('Enter the event location: ')
    pointer.execute("""INSERT INTO EVENT_SCHEDULE(EventID, EventDate, Location) values(%s,%s,%s)""", (evntid, evntdt, loca))
    my_DB.commit()
    print('Data inserted successfully.')
    my_DB.close()

def Indiv_results_insert(pointer, my_DB):
    evntid = input('Enter the event ID: ')    
    olympian = input('Enter the olympian ID: ')
    medal = input('Enter the type of medal: ')
    pointer.execute("""INSERT INTO INDIVIDUAL_RESULTS(EventID, Olympian, Medal) values(%s,%s,%s)""", (evntid, olympian, medal))
    my_DB.commit()
    print('Data inserted successfully.')
    my_DB.close()

def Country_delete(pointer, my_DB):
    rem_country = input('Type the name of the country you want to delete: ')
    pointer.execute(f"DELETE FROM Country WHERE CName='{rem_country}'")
    my_DB.commit()
    print("Data deleted successfully")
    my_DB.close()
    
def Coach_delete(pointer, my_DB):
    coach = input('Type the name of the OlympicID you want to delete: ')
    pointer.execute(f"DELETE FROM Coach WHERE OlympicID='{coach}'")
    my_DB.commit()
    print("Data deleted successfully")
    my_DB.close()
    
def Team_delete(pointer, my_DB):
    team_id = input('Type the name of the TeamID you want to delete: ')
    pointer.execute(f"DELETE FROM Team WHERE TeamID='{team_id}'")
    my_DB.commit()
    print("Data deleted successfully")
    my_DB.close()   
        

def Participant_delete(pointer, my_DB):
    participant = input('Type the OlympicID of the participant you want to delete: ')
    pointer.execute(f"DELETE FROM Participant WHERE OlympicID='{participant}'")
    my_DB.commit()
    print("Data deleted successfully")
    my_DB.close()

def Athlete_delete(pointer, my_DB):
    athlete = input('Type the OlympicID of the athlete you want to delete: ')
    pointer.execute(f"DELETE FROM Athlete WHERE OlympicID='{athlete}'")
    my_DB.commit()
    print("Data deleted successfully")
    my_DB.close()

def Event_delete(pointer, my_DB):
    evnt = input('Type the Event Schedule you want to delete: ')
    pointer.execute(f"DELETE FROM Event_Schedule WHERE EventID='{evnt}'")
    my_DB.commit()
    print("Data deleted successfully.")
    my_DB.close()

def Indiv_results_delete(pointer, my_DB):
    indir = input('Type the individual result you want to delete: ')
    pointer.execute(f"DELETE FROM Individual_Results WHERE EventID='{indir}'")
    my_DB.commit()
    print("Data deleted successfuly.")
    my_DB.close()

def Team_results_delete(pointer, my_DB):
    tresult = input('Type the name of the teamID you want to delete: ')
    pointer.execute(f"DELETE FROM Team_Results WHERE Team='{tresult}'")
    my_DB.commit()
    print("Data deleted successfully")
    my_DB.close()

def Country_update(pointer, my_DB):
    update_name = input('Enter the name of the country that you want to update info on: ')
    new_gld = input('Enter the new number of gold medals: ')
    new_slvr = input('Enter the new number of silver medals: ')
    new_brnze = input('enter the new number of bronze medals: ')
    pointer.execute(f"UPDATE Country SET AllTimeGold = '{new_gld}', AllTimeSilver = '{new_slvr}', AllTimeBronze ='{new_brnze}' WHERE CName = '{update_name}'")
    my_DB.commit()
    print('Updated successfully.')
    my_DB.close()


def Event_update(pointer, my_DB):
    new_evntid = input('Enter the EventID you want to update: ')
    new_evntdt = input('Enter the event date you want to update: ')
    new_loca = input('Enter the location you want to update: ')
    pointer.execute(f"UPDATE Event_Schedule SET EventDate = '{new_evntdt}', Location = '{new_loca}' WHERE EventID = '{new_evntid}'")
    my_DB.commit()
    print('Updated successfully.')
    my_DB.close()

def Indiv_results_update(pointer, my_DB):
    new_evntid = input('Enter the EventID you want to update: ')
    new_olympian = input('Enter the olympian you want to update: ')
    new_medal = input('Enter the medal you want to update: ')
    pointer.execute(f"UPDATE Individual_Results SET Olympian = '{new_olympian}', Medal = '{new_medal}' WHERE EventID = '{new_evntid}'")
    my_DB.commit()
    print('Updatetd successfully.')
    my_DB.close()
    
def Coach_update(pointer, my_DB):
    coach_name = input('Enter the name of the OlympicID that you want to update info on: ')
   
    new_ornt = input('Enter new orientation: ')
    pointer.execute(f"UPDATE Coach SET  Orientation = '{new_ornt}' WHERE OlympicID = '{coach_name}'")
    my_DB.commit()
    print('Updated Successfully')
    my_DB.close()
    
def Team_update(pointer, my_DB):
    teamid_name = input('Enter the name of the TeamID that you want to update info on: ')
    new_mm1 = input('Enter the new Member1: ')
    new_mm2 = input('Enter the new Member2: ')
    new_mm3 = input('Enter the new Member3: ')
    new_mm4 = input('Enter the new Member4: ')
    new_mm5 = input('Enter the new Member5: ')
    new_mm6 = input('Enter the new Member6: ')
    
    pointer.execute(f"UPDATE Team SET Member1 = '{new_mm1}', Member2 ='{new_mm2}', Member3 = '{new_mm3}', Member4 = '{new_mm4}', Member5 = '{new_mm5}', Member6 = '{new_mm6}' WHERE TeamID = '{teamid_name}'")
    my_DB.commit()
    print('Updated Successfully')
    my_DB.close()
    
   
    
        
        

def Participant_update(pointer, my_DB):
    update_id = input('Enter the OlympicID that you want to update info on: ')
    ne_lname = input('Enter the new last name of participant: ')
    new_fname = input('Enter the new first name of participant: ')
    new_cname = input('enter the new name of country: ')
    pointer.execute(f"UPDATE Participant SET LName = '{ne_lname}', FName='{new_fname}', Country = '{new_cname}' WHERE OlympicID = '{update_id}''")
    my_DB.commit()
    print('Updated Successfully')
    my_DB.close()

# def Country_alter(pointer, my_DB):
#     print('Enter New if you want to create a new column\n')
#     print('Enter Drop if you want to delete a column\n')
#     print('Enter Modify if you want to modify a column\n')
#     decision = input('Your choice: ')

#     if decision.lower() == 'new':
#         new_name = input('Enter the name of the new column: ')
#         d_type = input('Enter the data type for the column: ')
#         pointer.execute("ALTER TABLE Country ADD  "+ new_name+" " + d_type+" ";"")
#         my_DB.commit()
#         print('Added Successfully')
#         my_DB.close()


def Athlete_update(pointer, my_DB):
    update_id = input('Enter the OlympicID that you want to update info on: ')
    ne_sex = input('Enter the new sex of athlete: ')
    new_byear = input('Enter the new birth year of athlete: ')
    new_fgames = input('enter the new fgames of the athlete: ')
    pointer.execute(f"UPDATE Athlete SET Sex = '{ne_sex}', BirthYear ='{new_byear}', FirstGames ='{new_fgames}' WHERE OlympicID = '{update_id}'")
    my_DB.commit()
    print('Updated Successfully')
    my_DB.close()

def Team_results_update(pointer, my_DB):
    update_id = input('Enter the event ID that you want to update info on: ')
    ne_team = input('Enter the new team: ')
    new_medal = input('Enter the new medal: ')
    pointer.execute(f"UPDATE Team_Results SET EventID = '{update_id}', Medal ='{new_medal}' WHERE Team = '{ne_team}'")
    my_DB.commit()
    print('Updated Successfully')
    my_DB.close()
    

def main():
    
    my_DB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="*@@11854##Root",
        database="olympicarchery"
    )

    pointer = my_DB.cursor()

    pointer.execute('SELECT * FROM Country')
    rslt = pointer.fetchall()
    print(rslt)

    print('Welcome to the Olympic Archery database\n')
    print('Select the operation that you would like to use from the following options: \nINSERT\nDELETE\nUPDATE\nCREATE TABLE\nCREATE VIEW\nALTER\nQUERY\n')
    operation_input = input('Type your preffered operation: ') 
    
    if operation_input.lower() == 'insert':
        print('The tables available are \nCountry\nParticipant\nAthlete\nCoach\nTeam\nEvent Schedule\nIndividual Results\nTeam Results\n')

        table_input = input('Enter the table you would like to insert data into: ')

        if table_input.lower() == 'country':
            Country_insert(pointer, my_DB)

        elif table_input.lower == 'participant':
            Participant_insert(pointer, my_DB)

        elif table_input.lower == 'athlete':
            Athlete_insert(pointer, my_DB)

        elif table_input.lower == 'coach':
            Coach_insert(pointer, my_DB)

        elif table_input.lower == 'team':
            Team_insert(pointer, my_DB)
        
        elif table_input.lower == 'event Schedule':
            Event_insert(pointer, my_DB)

        elif table_input.lower == 'individual results':
            Indiv_results_insert(pointer, my_DB)
        
        elif table_input.lower == 'team results':
            Team_results_insert(pointer, my_DB)

    elif operation_input.lower() == 'delete':
        print('The tables available are \nCountry\nParticipant\nAthlete\nCoach\nTeam\nEvent Schedule\nIndividual Results\nTeam Results\n')

        table_slct = input('Enter the table you would like to delete data from: ')

        if table_slct.lower() == 'country':
            Country_delete(pointer, my_DB)

        elif table_slct.lower == 'participant':
            Participant_delete(pointer, my_DB)

        elif table_slct.lower == 'athlete':
            Athlete_delete(pointer, my_DB)

        elif table_slct.lower == 'coach':
            Coach_delete(pointer, my_DB)

        elif table_slct.lower == 'team':
            Team_delete(pointer, my_DB)
        
        elif table_slct.lower == 'event schedule':
            Event_delete(pointer, my_DB)

        elif table_slct.lower == 'individual results':
            Indiv_results_delete(pointer, my_DB)
        
        elif table_slct.lower == 'team results':
            Team_results_delete(pointer, my_DB)
    
    elif operation_input.lower() == 'update':
        print('The tables available are \nCountry\nParticipant\nAthlete\nCoach\nTeam\nEvent Schedule\nIndividual Results\nTeam Results\n')

        table_selct = input('Enter the table you would like to update: ')

        if table_selct.lower() == 'country':
            Country_update(pointer, my_DB)

        elif table_selct.lower == 'participant':
            Participant_update(pointer, my_DB)

        elif table_selct.lower == 'athlete':
            Athlete_update(pointer, my_DB)

        elif table_selct.lower == 'coach':
            Coach_update(pointer, my_DB)

        elif table_selct.lower == 'team':
            Team_update(pointer, my_DB)
        
        elif table_selct.lower == 'event schedule':
            Event_update(pointer, my_DB)

        elif table_selct.lower == 'individual results':
            Indiv_results_update(pointer, my_DB)
        
        elif table_selct.lower == 'team results':
            Team_results_update(pointer, my_DB)
    
    elif operation_input.lower() == 'alter':
        print('The tables available are \nCountry\nParticipant\nAthlete\nCoach\nTeam\nEvent Schedule\nIndividual Results\nTeam Results\n')

        table_name = input('Enter the table you would like to alter: ')
        
        if table_name.lower() == 'country':
            Country_alter(pointer, my_DB)

        elif table_name.lower == 'participant':
            Participant_alter(pointer, my_DB)

        elif table_name.lower == 'athlete':
            Athlete_alter(pointer, my_DB)

        elif table_name.lower == 'coach':
            Coach_alter(pointer, my_DB)

        elif table_name.lower == 'team':
            Team_alter(pointer, my_DB)
        
        elif table_name.lower == 'event schedule':
            Event_alter(pointer, my_DB)

        elif table_name.lower == 'individual results':
            Indiv_results_alter(pointer, my_DB)
        
        elif table_name.lower == 'team results':
            Team_results_alter(pointer, my_DB)
main()