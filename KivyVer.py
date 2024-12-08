from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import pygments

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image,CoreImage 

import io   #I used io it's simple and useful!

import matplotlib.pyplot as plt   #need matplotlib library
from matplotlib.figure import Figure 
import pandas as pd
from datetime import datetime, timedelta
import csv

## Here for providing colour to the background  
from kivy.core.window import Window 

import mysql.connector

global parentID
parentID = ""
global childrenID
childrenID = []
global childrenNames
childrenNames = []
global currentchild
currentchild = 0
global dates
dates = []
global times
times = []
global activities
activities = []
global df
df = pd.DataFrame()
global diaperdf
diaperdf = pd.DataFrame()
global diaperdates
diaperdates = []
global diapertimes
diapertimes = []
global diaperactivities
diaperactivities = []

class LoginWindow(Screen):
    pass

class CreationWindow(Screen):
    pass

class FirstChildWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class SleepWindow(Screen):
    pass

class DiaperWindow(Screen):
    pass

class SettingsWindow(Screen):
    pass

class MyMainApp(MDApp):
    main_text = "None"

    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Capstone1!",
            database = "baby_tracker"
        )
    c = mydb.cursor()

    # initialing the Application
    def __init__(self, **kwargs):
        super(MyMainApp, self).__init__(**kwargs)
        self.a = Builder.load_file('design.kv')

    def build(self):

        sm = ScreenManager()
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(CreationWindow(name='creation'))
        sm.add_widget(FirstChildWindow(name='firstchild'))
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(SleepWindow(name='sleep'))
        sm.add_widget(DiaperWindow(name='diaper'))
        sm.add_widget(SettingsWindow(name='settings'))

        return sm
    
    def loginProt(self):
        global parentID
        global df
        username  = self.root.get_screen('login').ids.userw.text
        password = self.root.get_screen('login').ids.passw.text
        self.root.get_screen('login').ids.passw.text = ""
        self.root.transition.direction = "left"

        self.c.execute("select * from tbl_parents where fld_p_username_pk = %s", (username,))          
        
        result = self.c.fetchall()
        
        if result == []:
            # Placeholder for if username not found
            print()
        else:
            if password == result[0][1]:
                self.root.get_screen('login').ids.userw.text = ""
                parentID = username
                                    
                self.c.execute("select * from tbl_child where fld_c_p_username_fk = %s", (username,))
                result = self.c.fetchall()
                print(result)
                for i in range(len(result)):
                    childrenID.insert(i,result[i][0])

                for i in range(len(result)):
                    childrenNames.insert(i,str(result[i][2]+", "+result[i][1]))

                if(childrenID != []):

                    print(childrenID)
                    print(childrenNames)
                    print(childrenID[currentchild])
                    
                    self.c.execute("select fld_event_time, fld_event_type from tbl_event_data where fld_c_id_fk = %s and (fld_event_type = 'Sleep' or fld_event_type = 'Awake')", (childrenID[currentchild],))
                    result = self.c.fetchall()

                    print(result)

                    df = pd.DataFrame(result, columns=[i[0] for i in self.c.description])
                    #print(df)
                    df = df.rename(columns={'fld_event_time': 'Date', 'fld_event_type': 'Activity'})
                    #print(df)
                    self.root.get_screen('main').ids.childtext.text = childrenNames[currentchild]
                    self.root.get_screen('sleep').ids.childtext.text = childrenNames[currentchild]
                    self.root.get_screen('diaper').ids.childtext.text = childrenNames[currentchild]
                    self.root.get_screen('settings').ids.childtext.text = childrenNames[currentchild]
                    self.root.current = "main"
                else:
                    self.root.current = "firstchild"
            else:
                self.root.current = "login"

    def createUser(self):
        global parentID
        global df
        username  = self.root.get_screen('creation').ids.userw.text
        password = self.root.get_screen('creation').ids.passw.text
        self.root.get_screen('creation').ids.passw.text = ""
        self.root.transition.direction = "left"

        self.c.execute("select * from tbl_parents where fld_p_username_pk = %s", (username,))          
        
        result = self.c.fetchall()
        
        if result == []:
            self.c.execute("INSERT INTO `baby_tracker`.`tbl_parents` (`fld_p_username_pk`, `fld_p_password`) VALUES (%s, %s)",(username, password,))
            self.mydb.commit()
            self.root.current = "login"
        else:
            #Error username exists
            self.root.get_screen('creation').ids.userw.text = ""

    def createFirstChild(self):
        global parentID
        global df
        firstname = self.root.get_screen('firstchild').ids.cfname.text
        lastname = self.root.get_screen('firstchild').ids.clname.text
        self.root.transition.direction = "left"         
        
        
        if all(x.isspace() for x in firstname) or all(x.isspace() for x in lastname):
            return
        else:
            self.c.execute("INSERT INTO `baby_tracker`.`tbl_child` (`fld_c_p_username_fk`, `fld_c_fname`, `fld_c_lname`) VALUES (%s, %s, %s)",(parentID, firstname, lastname,))
            self.mydb.commit()
            self.root.get_screen('login').ids.userw.text = ""
            self.c.execute("select * from tbl_child where fld_c_p_username_fk = %s", (parentID,))
            result = self.c.fetchall()
            # print(result)
            for i in range(len(result)):
                childrenID.insert(i,result[i][0])

            for i in range(len(result)):
                childrenNames.insert(i,str(result[i][2]+", "+result[i][1]))

            # print(childrenID)
            # print(childrenNames)
            
            self.c.execute("select fld_event_time, fld_event_type from tbl_event_data where fld_c_id_fk = %s and (fld_event_type = 'Sleep' or fld_event_type = 'Awake')", (childrenID[currentchild],))
            result = self.c.fetchall()

            # print(result)

            df = pd.DataFrame(result, columns=[i[0] for i in self.c.description])
            #print(df)
            df = df.rename(columns={'fld_event_time': 'Date', 'fld_event_type': 'Activity'})
            #print(df)
            self.root.get_screen('main').ids.childtext.text = childrenNames[currentchild]
            self.root.get_screen('sleep').ids.childtext.text = childrenNames[currentchild]
            self.root.get_screen('diaper').ids.childtext.text = childrenNames[currentchild]
            self.root.get_screen('settings').ids.childtext.text = childrenNames[currentchild]
            self.root.current = "main"

    def createNewChild(self):
        global parentID
        global df
        firstname = self.root.get_screen('settings').ids.cfname.text
        lastname = self.root.get_screen('settings').ids.clname.text
        self.root.transition.direction = "left"         
        
        
        if all(x.isspace() for x in firstname) or all(x.isspace() for x in lastname):
            return
        else:
            self.c.execute("INSERT INTO `baby_tracker`.`tbl_child` (`fld_c_p_username_fk`, `fld_c_fname`, `fld_c_lname`) VALUES (%s, %s, %s)",(parentID, firstname, lastname,))
            self.mydb.commit()
            self.root.get_screen('settings').ids.cfname.text = ''
            self.root.get_screen('settings').ids.clname.text = ''
            self.c.execute("select * from tbl_child where fld_c_p_username_fk = %s", (parentID,))
            result = self.c.fetchall()
            # print(result)
            for i in range(len(result)):
                childrenID.insert(i,result[i][0])

            for i in range(len(result)):
                childrenNames.insert(i,str(result[i][2]+", "+result[i][1]))

            # print(childrenID)
            # print(childrenNames)
            
            self.c.execute("select fld_event_time, fld_event_type from tbl_event_data where fld_c_id_fk = %s and (fld_event_type = 'Sleep' or fld_event_type = 'Awake')", (childrenID[currentchild],))
            result = self.c.fetchall()

            # print(result)

            df = pd.DataFrame(result, columns=[i[0] for i in self.c.description])
            #print(df)
            df = df.rename(columns={'fld_event_time': 'Date', 'fld_event_type': 'Activity'})
            #print(df)
            self.root.get_screen('main').ids.childtext.text = childrenNames[currentchild]
            self.root.get_screen('sleep').ids.childtext.text = childrenNames[currentchild]
            self.root.get_screen('diaper').ids.childtext.text = childrenNames[currentchild]
            self.root.get_screen('settings').ids.childtext.text = childrenNames[currentchild]

    def logoutProt(self):
        global parentID
        parentID = ""
        global childrenID
        childrenID = []
        global currentchild
        currentchild = 0
        global dates
        dates = []
        global times
        times = []
        global activities
        activities = []
        global df
        df = pd.DataFrame()
        global diaperdf
        diaperdf = pd.DataFrame()
        global diaperdates
        diaperdates = []
        global diapertimes
        diapertimes = []
        global diaperactivities
        diaperactivities = []
        self.root.get_screen('sleep').ids.date1.text = ''
        self.root.get_screen('sleep').ids.time1.text = ''
        self.root.get_screen('sleep').ids.activity1.text = ''
        self.root.get_screen('sleep').ids.date2.text = ''
        self.root.get_screen('sleep').ids.time2.text = ''
        self.root.get_screen('sleep').ids.activity2.text = ''
        self.root.get_screen('sleep').ids.date3.text = ''
        self.root.get_screen('sleep').ids.time3.text = ''
        self.root.get_screen('sleep').ids.activity3.text = ''
        self.root.get_screen('sleep').ids.date4.text = ''
        self.root.get_screen('sleep').ids.time4.text = ''
        self.root.get_screen('sleep').ids.activity4.text = ''
        self.root.get_screen('sleep').ids.date5.text = ''
        self.root.get_screen('sleep').ids.time5.text = ''
        self.root.get_screen('sleep').ids.activity5.text = ''
        self.root.get_screen('diaper').ids.date1.text = ''
        self.root.get_screen('diaper').ids.time1.text = ''
        self.root.get_screen('diaper').ids.date2.text = ''
        self.root.get_screen('diaper').ids.time2.text = ''
        self.root.get_screen('diaper').ids.date3.text = ''
        self.root.get_screen('diaper').ids.time3.text = ''
        self.root.get_screen('diaper').ids.date4.text = ''
        self.root.get_screen('diaper').ids.time4.text = ''
        self.root.get_screen('diaper').ids.date5.text = ''
        self.root.get_screen('diaper').ids.time5.text = ''
        self.root.transition.direction = "left"
        self.root.current = "login"

    def submitSleepData(self):
        if (str(self.root.get_screen('sleep').ids.sleepdate.text) == ""):
            return
        if (str(self.root.get_screen('sleep').ids.sleeptime.text) == ""):
            return
        if (str(self.root.get_screen('sleep').ids.sleepactivity.text) != "Sleep"):
            if (str(self.root.get_screen('sleep').ids.sleepactivity.text) != "Awake"):
                return


        # Get date data
        date = self.root.get_screen('sleep').ids.sleepdate.text

        # Take data and format it where the program can understand it. Temporary and will be irrelavant in future updates.
        tempdate = ""
        if (len(date) == 3):
            tempdate = tempdate + "0"
            tempdate = tempdate + date[0]
            tempdate = tempdate + " 0"
            tempdate = tempdate + date[2]
        elif (len(date) == 4):
            if (date[1] == '/'):
                tempdate = tempdate + "0"
                tempdate = tempdate + date[0]
                tempdate = tempdate + " "
                tempdate = tempdate + date[2]
                tempdate = tempdate + date[3]
            if (date[2] == '/'):
                tempdate = tempdate + date[0]
                tempdate = tempdate + date[1]
                tempdate = tempdate + " 0"
                tempdate = tempdate + date[3]
        elif (len(date) == 5):
            tempdate = tempdate + date[0]
            tempdate = tempdate + date[1]
            tempdate = tempdate + " "
            tempdate = tempdate + date[3]
            tempdate = tempdate + date[4]
        
        # Get time data
        time = str(self.root.get_screen('sleep').ids.sleeptime.text)

        # Take time and format it where the program can understand it. Temporary and will be irrelavant in future updates.
        temptime = ""
        if (len(time) == 3):
            temptime = temptime + "0"
            temptime = temptime + time[0]
            temptime = temptime + ":0"
            temptime = temptime + time[2]
        elif (len(time) == 4):
            if (time[1] == ':'):
                temptime = temptime + "0"
                temptime = temptime + time[0]
                temptime = temptime + ":"
                temptime = temptime + time[2]
                temptime = temptime + time[3]
            if (time[2] == ':'):
                temptime = temptime + time[0]
                temptime = temptime + time[1]
                temptime = temptime + ":0"
                temptime = temptime + time[3]
        elif (len(time) == 5):
            temptime = temptime + time[0]
            temptime = temptime + time[1]
            temptime = temptime + ":"
            temptime = temptime + time[3]
            temptime = temptime + time[4]

        # Concatenate data for storage in the csv
        tempdate = tempdate + " 2024  " + temptime

        # Open csv corresponding to the current child
        # line_to_append = [[tempdate,str(self.root.get_screen('sleep').ids.sleepactivity.text)]]
        # filename = 'User'+str(currentchild)+'.csv'
        # file = open(filename,'a', newline='')
        # writer = csv.writer(file)

        # # Write new data line to csv
        # writer.writerows(line_to_append)

        # # Close csv
        # file.close()
        tempactivity = str(self.root.get_screen('sleep').ids.sleepactivity.text)
        #print(int(childrenID[currentchild]))
        #print(tempdate)
        #print(tempactivity)
        self.c.execute("INSERT INTO `baby_tracker`.`tbl_event_data` (`fld_c_id_fk`, `fld_event_time`, `fld_event_type`) VALUES (%s, %s, %s)", (int(childrenID[currentchild]),tempdate,tempactivity,))
        self.mydb.commit()
        
        # Clear data entry spots
        self.root.get_screen('sleep').ids.sleepdate.text = ""
        self.root.get_screen('sleep').ids.sleeptime.text = ""
        self.root.get_screen('sleep').ids.sleepactivity.text = ""

        self.updateGlobals()

    def submitDiaperData(self):
        if (str(self.root.get_screen('diaper').ids.diaperdate.text) == ""):
            return
        if (str(self.root.get_screen('diaper').ids.diapertime.text) == ""):
            return

        # Get date data
        date = self.root.get_screen('diaper').ids.diaperdate.text

        # Take data and format it where the program can understand it. Temporary and will be irrelavant in future updates.
        tempdate = ""
        if (len(date) == 3):
            tempdate = tempdate + "0"
            tempdate = tempdate + date[0]
            tempdate = tempdate + " 0"
            tempdate = tempdate + date[2]
        elif (len(date) == 4):
            if (date[1] == '/'):
                tempdate = tempdate + "0"
                tempdate = tempdate + date[0]
                tempdate = tempdate + " "
                tempdate = tempdate + date[2]
                tempdate = tempdate + date[3]
            if (date[2] == '/'):
                tempdate = tempdate + date[0]
                tempdate = tempdate + date[1]
                tempdate = tempdate + " 0"
                tempdate = tempdate + date[3]
        elif (len(date) == 5):
            tempdate = tempdate + date[0]
            tempdate = tempdate + date[1]
            tempdate = tempdate + " "
            tempdate = tempdate + date[3]
            tempdate = tempdate + date[4]
        
        # Get time data
        time = str(self.root.get_screen('diaper').ids.diapertime.text)

        # Take time and format it where the program can understand it. Temporary and will be irrelavant in future updates.
        temptime = ""
        if (len(time) == 3):
            temptime = temptime + "0"
            temptime = temptime + time[0]
            temptime = temptime + ":0"
            temptime = temptime + time[2]
        elif (len(time) == 4):
            if (time[1] == ':'):
                temptime = temptime + "0"
                temptime = temptime + time[0]
                temptime = temptime + ":"
                temptime = temptime + time[2]
                temptime = temptime + time[3]
            if (time[2] == ':'):
                temptime = temptime + time[0]
                temptime = temptime + time[1]
                temptime = temptime + ":0"
                temptime = temptime + time[3]
        elif (len(time) == 5):
            temptime = temptime + time[0]
            temptime = temptime + time[1]
            temptime = temptime + ":"
            temptime = temptime + time[3]
            temptime = temptime + time[4]

        # Concatenate data for storage in the csv
        tempdate = tempdate + " 2024  " + temptime

        # Open csv corresponding to the current child
        # line_to_append = [[tempdate,str(self.root.get_screen('sleep').ids.sleepactivity.text)]]
        # filename = 'User'+str(currentchild)+'.csv'
        # file = open(filename,'a', newline='')
        # writer = csv.writer(file)

        # # Write new data line to csv
        # writer.writerows(line_to_append)

        # # Close csv
        # file.close()
        #print(int(childrenID[currentchild]))
        #print(tempdate)
        self.c.execute("INSERT INTO `baby_tracker`.`tbl_event_data` (`fld_c_id_fk`, `fld_event_time`, `fld_event_type`) VALUES (%s, %s, %s)", (int(childrenID[currentchild]),tempdate,'Diaper',))
        self.mydb.commit()
        
        # Clear data entry spots
        self.root.get_screen('diaper').ids.diaperdate.text = ""
        self.root.get_screen('diaper').ids.diapertime.text = ""

        self.updateGlobals()

    def changeChild(self):
        global currentchild
        global childrenID
        # Check current child and update to next child
        if len(childrenID) > (currentchild + 1):
            currentchild += 1
        else:
            currentchild = 0
        
        # Call to update tables and graph
        self.updateGlobals()

    def updateGlobals(self):
        global dates 
        dates = []
        global times 
        times = []
        global activities 
        activities = []
        global df
        global diaperdf
        global childrenID
        global childrenNames
        global currentchild
        global diaperdates
        diaperdates = []
        global diapertimes
        diapertimes = []
        global diaperactivities
        diaperactivities = []

        # Check currentchild and update button text
        # if (currentchild == 2):
        #     self.root.get_screen('main').ids.childtext.text = "Child 2"
        #     self.root.get_screen('sleep').ids.childtext.text = "Child 2"
        #     self.root.get_screen('settings').ids.childtext.text = "Child 2"
        # elif (currentchild == 3):
        #     self.root.get_screen('main').ids.childtext.text = "Child 3"
        #     self.root.get_screen('sleep').ids.childtext.text = "Child 3"
        #     self.root.get_screen('settings').ids.childtext.text = "Child 3"
        # elif (currentchild == 4):
        #     self.root.get_screen('main').ids.childtext.text = "Child 4"
        #     self.root.get_screen('sleep').ids.childtext.text = "Child 4"
        #     self.root.get_screen('settings').ids.childtext.text = "Child 4"
        # elif (currentchild == 1):
        #     self.root.get_screen('main').ids.childtext.text = "Child 1"
        #     self.root.get_screen('sleep').ids.childtext.text = "Child 1"
        #     self.root.get_screen('settings').ids.childtext.text = "Child 1"
        if(childrenID != []):
            self.root.get_screen('main').ids.childtext.text = childrenNames[currentchild]
            self.root.get_screen('sleep').ids.childtext.text = childrenNames[currentchild]
            self.root.get_screen('diaper').ids.childtext.text = childrenNames[currentchild]
            self.root.get_screen('settings').ids.childtext.text = childrenNames[currentchild]

            # Based off of currentchild load csv corresponding to the child
            # filename = 'User'+str(currentchild)+'.csv' 
            # df = pd.read_csv(filename)
            self.c.execute("select fld_event_time, fld_event_type from tbl_event_data where fld_c_id_fk = %s AND (fld_event_type = 'Sleep' or fld_event_type = 'Awake')", (childrenID[currentchild],))
            sresult = self.c.fetchall()

            # print(sresult)

            df = pd.DataFrame(sresult, columns=[i[0] for i in self.c.description])
            # print(df)
            df = df.rename(columns={'fld_event_time': 'Date', 'fld_event_type': 'Activity'})
            # print(df)

            df.sort_values(by=['Date'])
            # Load last 7 or all of data, whichever is less
            if(len(df) >= 7):
                last_n_rows = df.tail(7)
            else:
                last_n_rows = df.tail(len(df))
            # Populate last data entries into the three arrays
            for i in range(7):
                if (i < len(last_n_rows)):
                    temp = last_n_rows.iloc[[i]].values[0]
                    temp[0] = str(temp[0])
                    #print(temp[0])
                    date = datetime.strptime(temp[0], "%m %d %Y  %H:%M")
                    dates.insert(0,str(date.month)+"/"+str(date.day))
                    times.insert(0,str(date.hour)+":"+str(date.minute))
                    activities.insert(0,temp[1])
                else:
                    dates.append("")
                    times.append("")
                    activities.append("")

            self.root.get_screen('sleep').ids.date1.text = dates[0]
            self.root.get_screen('sleep').ids.time1.text = times[0]
            self.root.get_screen('sleep').ids.activity1.text = activities[0]
            self.root.get_screen('sleep').ids.date2.text = dates[1]
            self.root.get_screen('sleep').ids.time2.text = times[1]
            self.root.get_screen('sleep').ids.activity2.text = activities[1]
            self.root.get_screen('sleep').ids.date3.text = dates[2]
            self.root.get_screen('sleep').ids.time3.text = times[2]
            self.root.get_screen('sleep').ids.activity3.text = activities[2]
            self.root.get_screen('sleep').ids.date4.text = dates[3]
            self.root.get_screen('sleep').ids.time4.text = times[3]
            self.root.get_screen('sleep').ids.activity4.text = activities[3]
            self.root.get_screen('sleep').ids.date5.text = dates[4]
            self.root.get_screen('sleep').ids.time5.text = times[4]
            self.root.get_screen('sleep').ids.activity5.text = activities[4]

            # Convert 'Date' column to datetime
            df['Date'] = pd.to_datetime(df['Date'], format="%m %d %Y %H:%M")

            # Initialize sleep duration dictionary
            sleep_duration = {}

            # Loop through the DataFrame to calculate sleep duration for each day
            for i in range(len(df)-1):
                if df.iloc[i]['Activity'] == 'Sleep' and df.iloc[i+1]['Activity'] == 'Awake':
                    date = df.iloc[i]['Date'].date()
                    duration = (df.iloc[i+1]['Date'] - df.iloc[i]['Date']).total_seconds() / 3600
                    if date in sleep_duration:
                        sleep_duration[date] += duration
                    else:
                        sleep_duration[date] = duration

            # Convert sleep duration to DataFrame
            sleep_df = pd.DataFrame(list(sleep_duration.items()), columns=['Date', 'SleepHours'])

            # Remove the year from the date
            sleep_df['Date'] = sleep_df['Date'].apply(lambda x: x.strftime('%m-%d'))

            # Filter last 7 days
            end_date = datetime.today().date()
            start_date = end_date - timedelta(days=6)
            sleep_df = sleep_df[sleep_df['Date'].isin([(start_date + timedelta(days=i)).strftime('%m-%d') for i in range(7)])]

            # Create graph figure

            f = Figure(figsize=(4, 3), dpi=100)
            ax = f.add_subplot(111)

            # Setup bar graph

            ax.bar(sleep_df['Date'], sleep_df['SleepHours'], color='skyblue')
            ax.set_title('Sleep Duration for Last 7 Days')
            ax.set_ylabel('Hours of Sleep')
            ax.set_xticklabels(sleep_df['Date'], rotation=0)

            buf=io.BytesIO()
            f.savefig(buf)  #save your dataset to IoByte
        
            buf.seek(0) #seek your graph
            self.root.get_screen('sleep').ids.sleepgraph.texture=CoreImage(buf, ext="png").texture     #display your image
            self.root.get_screen('sleep').ids.sleepgraph.reload()
            del buf #then delete created buf

            # If sleep data input data into table
            if (len(sleep_df) > 0):
                self.root.get_screen('sleep').ids.sleptday.text = str(round(sleep_df.iloc[-1]['SleepHours'],2))
                self.root.get_screen('sleep').ids.sleptweek.text = str(round(sleep_df['SleepHours'].sum(),2))
            else:
                self.root.get_screen('sleep').ids.sleptday.text = "N/A"
                self.root.get_screen('sleep').ids.sleptweek.text = "N/A"

            self.c.execute("select fld_event_time, fld_event_type from tbl_event_data where fld_c_id_fk = %s and fld_event_type = 'Diaper'", (childrenID[currentchild],))
            dresult = self.c.fetchall()

            #print(dresult)

            diaperdf = pd.DataFrame(dresult, columns=[i[0] for i in self.c.description])
            # print(diaperdf)
            diaperdf = diaperdf.rename(columns={'fld_event_time': 'Date', 'fld_event_type': 'Activity'})
            
            #print(diaperdf)

            diaperdf.sort_values(by=['Date'])
            #print(diaperdf)
            # Load last 7 or all of data, whichever is less
            if(len(diaperdf) >= 7):
                last_n_rows = diaperdf.tail(7)
            else:
                last_n_rows = diaperdf.tail(len(diaperdf))
            # Populate last data entries into the three arrays

            for i in range(7):
                if (i < len(last_n_rows)):
                    temp = last_n_rows.iloc[[i]].values[0]
                    temp[0] = str(temp[0])
                    print(temp[0])
                    date = datetime.strptime(temp[0], "%m %d %Y  %H:%M")
                    diaperdates.insert(0,str(date.month)+"/"+str(date.day))
                    diapertimes.insert(0,str(date.hour)+":"+str(date.minute))
                    diaperactivities.insert(0,temp[1])
                else:
                    diaperdates.append("")
                    diapertimes.append("")
                    diaperactivities.append("")

            self.root.get_screen('diaper').ids.date1.text = diaperdates[0]
            self.root.get_screen('diaper').ids.time1.text = diapertimes[0]
            self.root.get_screen('diaper').ids.date2.text = diaperdates[1]
            self.root.get_screen('diaper').ids.time2.text = diapertimes[1]
            self.root.get_screen('diaper').ids.date3.text = diaperdates[2]
            self.root.get_screen('diaper').ids.time3.text = diapertimes[2]
            self.root.get_screen('diaper').ids.date4.text = diaperdates[3]
            self.root.get_screen('diaper').ids.time4.text = diapertimes[3]
            self.root.get_screen('diaper').ids.date5.text = diaperdates[4]
            self.root.get_screen('diaper').ids.time5.text = diapertimes[4]

if __name__ == "__main__":
    MyMainApp().run()
