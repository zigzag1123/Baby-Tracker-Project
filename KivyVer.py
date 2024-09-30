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

loadingstr = ("""
<LoginWindow>:
    name: "login"

    FloatLayout:

        Label:
            text: "Username:"
            pos_hint: {'x': .45, 'y': .7}
            color: 255,255,255
            size_hint: .1, .1

        TextInput:
            id: userw
            multiline: False
            write_tab: False
            pos_hint: {'x': .45, 'y': .65}
            size_hint: .1, .05
              
        Label:
            text: "Password:"
            pos_hint: {'x': .45, 'y': .5}
            color: 255,255,255
            size_hint: .1, .1

        TextInput:
            id: passw
            password: True
            multiline: False
            write_tab: False
            pos_hint: {'x': .45, 'y': .45}
            size_hint: .1, .05

        Button:
            text: "Submit"
            pos_hint: {'x': .45, 'y': .3}
            size_hint: .1, .1
            on_release:
                app.loginProt()

<MainWindow>:
    name: "main"

    FloatLayout:
        
        Label:
            id: childtext
            text: "Child 1"
            pos_hint: {'x': .0, 'y': .9}
            color: 255,255,255
            size_hint: .1, .1

        Button:
            text: "Select Child"
            pos_hint: {'x': .1, 'y': .9}
            size_hint: .1, .1
            on_release:
                app.changeChild()
        
        Button:
            text: "Sleep"
            pos_hint: {'x': .2, 'y': .9}
            size_hint: .1, .1
            on_release:
                app.updateGlobals()
                app.root.current = "sleep"
                root.manager.transition.direction = "left"

        Button:
            text: "Settings"
            pos_hint: {'x': .9, 'y': .9}
            size_hint: .1, .1
            on_release:
                app.root.current = "settings"
                root.manager.transition.direction = "left"

<SleepWindow>:
    name: "sleep"

    FloatLayout:
        
        Label:
            id: childtext
            text: "Child 1"
            pos_hint: {'x': .0, 'y': .9}
            color: 255,255,255
            size_hint: .1, .1

        Button:
            text: "Select Child"
            pos_hint: {'x': .1, 'y': .9}
            size_hint: .1, .1
            on_release:
                app.changeChild()
              
        Button:
            text: "Main"
            pos_hint: {'x': .2, 'y': .9}
            size_hint: .1, .1
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "left"
              
        Button:
            text: "Settings"
            pos_hint: {'x': .9, 'y': .9}
            size_hint: .1, .1
            on_release:
                app.root.current = "settings"
                root.manager.transition.direction = "left"
              
        Image:
            id:sleepgraph
            source:'' #image source
            pos_hint: {'x': .0, 'y': .05}
            size_hint: .6, .5
              
            allow_stretch: True
            
            keep_ratio: True

        Label:
            text: "Date"
            pos_hint: {'x': .1, 'y': .75}
            color: 255,255,255
            size_hint: .1, .05

        Label:
            text: "Time"
            pos_hint: {'x': .2, 'y': .75}
            color: 255,255,255
            size_hint: .1, .05

        Label:
            text: "Activity"
            pos_hint: {'x': .3, 'y': .75}
            color: 255,255,255
            size_hint: .1, .05
               
        TextInput:
            id: sleepdate
            multiline: False
            write_tab: False
            pos_hint: {'x': .1, 'y': .7}
            size_hint: .1, .05
              
        TextInput:
            id: sleeptime
            multiline: False
            write_tab: False
            pos_hint: {'x': .2, 'y': .7}
            size_hint: .1, .05
              
        TextInput:
            id: sleepactivity
            multiline: False
            write_tab: False
            pos_hint: {'x': .3, 'y': .7}
            size_hint: .1, .05
          
        Button:
            text: "Submit"
            pos_hint: {'x': .2, 'y': .65}
            size_hint: .1, .05
            on_release:
                app.submitSleepData()
              
        Label:
            text: "Past Sleep Activity"
            multiline: False
            pos_hint: {'x': .75, 'y': .8}
            color: 255,255,255
            size_hint: .1, .05

        Label:
            text: "Date"
            multiline: False
            pos_hint: {'x': .65, 'y': .75}
            color: 255,255,255
            size_hint: .1, .05
        
        Label:
            text: "Time"
            multiline: False
            pos_hint: {'x': .75, 'y': .75}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            text: "Activity"
            multiline: False
            pos_hint: {'x': .85, 'y': .75}
            color: 255,255,255
            size_hint: .1, .05

        Label:
            id: date1
            text: "Date1"
            multiline: False
            pos_hint: {'x': .65, 'y': .65}
            color: 255,255,255
            size_hint: .1, .05
        
        Label:
            id: time1
            text: "Time1"
            multiline: False
            pos_hint: {'x': .75, 'y': .65}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            id: activity1
            text: "Activity1"
            multiline: False
            pos_hint: {'x': .85, 'y': .65}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            id: date2
            text: "Date2"
            multiline: False
            pos_hint: {'x': .65, 'y': .55}
            color: 255,255,255
            size_hint: .1, .05
        
        Label:
            id: time2
            text: "Time2"
            multiline: False
            pos_hint: {'x': .75, 'y': .55}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            id: activity2
            text: "Activity2"
            multiline: False
            pos_hint: {'x': .85, 'y': .55}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            id: date3
            text: "Date3"
            multiline: False
            pos_hint: {'x': .65, 'y': .45}
            color: 255,255,255
            size_hint: .1, .05
        
        Label:
            id: time3
            text: "Time3"
            multiline: False
            pos_hint: {'x': .75, 'y': .45}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            id: activity3
            text: "Activity3"
            multiline: False
            pos_hint: {'x': .85, 'y': .45}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            id: date4
            text: "Date4"
            multiline: False
            pos_hint: {'x': .65, 'y': .35}
            color: 255,255,255
            size_hint: .1, .05
        
        Label:
            id: time4
            text: "Time4"
            multiline: False
            pos_hint: {'x': .75, 'y': .35}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            id: activity4
            text: "Activity4"
            multiline: False
            pos_hint: {'x': .85, 'y': .35}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            id: date5
            text: "Date5"
            multiline: False
            pos_hint: {'x': .65, 'y': .25}
            color: 255,255,255
            size_hint: .1, .05
        
        Label:
            id: time5
            text: "Time5"
            multiline: False
            pos_hint: {'x': .75, 'y': .25}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            id: activity5
            text: "Activity5"
            multiline: False
            pos_hint: {'x': .85, 'y': .25}
            color: 255,255,255
            size_hint: .1, .05
              
        Label:
            text: "Time Slept Today"
            multiline: False
            pos_hint: {'x': .625, 'y': .15}
            color: 255,255,255
            size_hint: .15, .05

        Label:
            text: "Time Slept this Week"
            multiline: False
            pos_hint: {'x': .8, 'y': .15}
            color: 255,255,255
            size_hint: .15, .05  
              
        Label:
            id: sleptday
            text: "Time"
            multiline: False
            pos_hint: {'x': .625, 'y': .1}
            color: 255,255,255
            size_hint: .15, .05
              
        Label:
            id: sleptweek
            text: "Time"
            multiline: False
            pos_hint: {'x': .8, 'y': .1}
            color: 255,255,255
            size_hint: .15, .05


<SettingsWindow>:
    name: "settings"

    FloatLayout:
        
        Label:
            id: childtext
            text: "Child 1"
            pos_hint: {'x': .0, 'y': .9}
            color: 255,255,255
            size_hint: .1, .1

        Button:
            text: "Select Child"
            pos_hint: {'x': .1, 'y': .9}
            size_hint: .1, .1
            on_release:
                app.changeChild()

        Button:
            text: "Settings"
            pos_hint: {'x': .9, 'y': .9}
            size_hint: .1, .1

        Button:
            text: "Log Out"
            pos_hint: {'x': .7, 'y': .1}
            size_hint: .2, .1
            on_release:
                app.root.current = "login"
                root.manager.transition.direction = "left"    
""")
global parentID
parentID = 0
global childrenID
childrenID = []
global currentchild
currentchild = 1
global dates
dates = []
global times
times = []
global activities
activities = []
global df
df = pd.read_csv('User1.csv')

class LoginWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class SleepWindow(Screen):
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
        self.a = Builder.load_string(loadingstr)
    
    def loginProt(self):
        username  = self.root.get_screen('login').ids.userw.text
        password = self.root.get_screen('login').ids.passw.text
        self.root.get_screen('login').ids.passw.text = ""
        self.root.transition.direction = "left"

        self.c.execute("select * from tbl_parents where fld_username = %s", (username,))          
        
        result = self.c.fetchall()
        
        if password == result[0][2]:
            self.root.current = "main"
        else:
            self.root.current = "login"
        

    def build(self):

        sm = ScreenManager()
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(SleepWindow(name='sleep'))
        sm.add_widget(SettingsWindow(name='settings'))

        return sm
    
    '''def updateGlobals(self):
        X=[ 1, 2, 3, 4, 5]
        Y= [5, 14, 7, 20, 11]  #your dataset
       
        plt.plot(X,Y)  #craete yourdataset graph
        plt.title("title here")
        plt.xlabel("x-axis label here)")
        plt.ylabel("y-axis label here")
       
        buf=io.BytesIO()
        plt.savefig(buf)  #save your dataset to IoByte
       
        buf.seek(0) #seek your graph
        self.root.get_screen('sleep').ids.sleepgraph.texture=CoreImage(buf, ext="png").texture     #display your image
        self.root.get_screen('sleep').ids.sleepgraph.reload()
        del buf #then delete created buf'''

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
        line_to_append = [[tempdate,str(self.root.get_screen('sleep').ids.sleepactivity.text)]]
        filename = 'User'+str(currentchild)+'.csv'
        file = open(filename,'a', newline='')
        writer = csv.writer(file)

        # Write new data line to csv
        writer.writerows(line_to_append)

        # Close csv
        file.close()
        
        # Clear data entry spots
        self.root.get_screen('sleep').ids.sleepdate.text = ""
        self.root.get_screen('sleep').ids.sleeptime.text = ""
        self.root.get_screen('sleep').ids.sleepactivity.text = ""

        self.updateGlobals()

    def changeChild(self):
        global currentchild
        # Check current child and update to next child
        if (currentchild == 1):
            currentchild = 2
        elif (currentchild== 2):
            currentchild = 3
        elif (currentchild == 3):
            currentchild = 4
        elif (currentchild == 4):
            currentchild = 1
        
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

        global currentchild

        # Check currentchild and update button text
        if (currentchild == 2):
            self.root.get_screen('main').ids.childtext.text = "Child 2"
            self.root.get_screen('sleep').ids.childtext.text = "Child 2"
            self.root.get_screen('settings').ids.childtext.text = "Child 2"
        elif (currentchild == 3):
            self.root.get_screen('main').ids.childtext.text = "Child 3"
            self.root.get_screen('sleep').ids.childtext.text = "Child 3"
            self.root.get_screen('settings').ids.childtext.text = "Child 3"
        elif (currentchild == 4):
            self.root.get_screen('main').ids.childtext.text = "Child 4"
            self.root.get_screen('sleep').ids.childtext.text = "Child 4"
            self.root.get_screen('settings').ids.childtext.text = "Child 4"
        elif (currentchild == 1):
            self.root.get_screen('main').ids.childtext.text = "Child 1"
            self.root.get_screen('sleep').ids.childtext.text = "Child 1"
            self.root.get_screen('settings').ids.childtext.text = "Child 1"

        # Based off of currentchild load csv corresponding to the child
        filename = 'User'+str(currentchild)+'.csv' 
        df = pd.read_csv(filename)

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

if __name__ == "__main__":
    MyMainApp().run()
