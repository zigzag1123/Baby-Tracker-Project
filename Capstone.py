from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import csv
from PIL import ImageTk,Image


# Create object for tkinter
root = Tk()

# Create login and sleep frame - Not implemented
sleepwindow = Frame(root)
loginwindow = Frame(root)

# Hard coded USER/PASS
# Will be hooked up to SQL for verification in sprint 3
username = "jhs0137"
password = "Pokemon12"

# Create Login Window and all objects
main = Toplevel()
main.title("Login")
name_label = Label(main,text="Baby Tracker").pack()
name_label = Label(main,text="Version 1.0").pack()
my_img = ImageTk.PhotoImage(Image.open("logo.png"))
img_label = Label(main,image=my_img).pack()
loginentry = Entry(main)
loginentry.pack()
passentry = Entry(main,show="*")
passentry.pack()

# Opens Sleep Tracking if USER/PASS Match
def opentop():
        global username
        global password
        global loginentry
        global passentry

        # Check USER and PASS

        if (username == str(loginentry.get())):
            if (password == str(passentry.get())):
                # Destroy Login Screen
                main.destroy()
                
                # Initialize Sleep Activity Screen
                top = Toplevel()
                top.title("Sleep Activity")
                top.geometry("1024x768")
                top.minsize(1024, 768)
                # Specify Grid
                gColumns = 8
                gRows = 13

                # Setup grid
                for i in range(gRows):
                    Grid.rowconfigure(top,i,weight=1)
                    for j in range(gColumns):
                        Grid.columnconfigure(top,j,weight=1)

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
                global color
                color = False

                # Invert color function for button
                def invertcolor():
                    global color
                    # Check color and switch between dark and light mode
                    # Light Mode
                    if color:
                        top.configure(bg="white")
                        for item in top.grid_slaves():
                            if isinstance(item, Entry):
                                item.configure(bg="lightgray",fg="black")
                            elif isinstance(item, Label):
                                item.configure(bg="lightgray",fg="black")
                            elif isinstance(item, Button):
                                item.configure(bg="lightgray",fg="black")
                        color = False
                    # Dark Mode
                    else:
                        top.configure(bg="black")
                        for item in top.grid_slaves():
                            if isinstance(item, Entry):
                                item.configure(bg="black",fg="white")
                            elif isinstance(item, Label):
                                item.configure(bg="black",fg="white")
                            elif isinstance(item, Button):
                                item.configure(bg="black",fg="white")
                                        
                        color = True
                
                # Create Buttons and Entry Locations
                button_1 = Label(top,text="Child1")

                button_3 = Button(top,text="Invert Color",command=invertcolor)
                button_4 = Button(top,text="")
                label_dt = Label(top,text="")

                label_1 = Label(top,text="Date")
                label_2 = Label(top,text="Time")
                label_3 = Label(top,text="Activity")

                entry_1 = Entry(top)
                entry_2 = Entry(top)
                entry_3 = Entry(top)

                table1_00_3 = Label(top,text="Past Sleep Activity")
                table1_10 = Label(top,text="Date")
                table1_11 = Label(top,text="Time")
                table1_12 = Label(top,text="Activity")

                # Get last 7 or all data whichever is less
                if(len(df) >= 7):
                    last_n_rows = df.tail(7)
                else:
                    last_n_rows = df.tail(len(df))

                # Process data from STR to datetime and fill in the arrays
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
                
                global table1_20
                global table1_21
                global table1_22
                global table1_30
                global table1_31
                global table1_32
                global table1_40
                global table1_41
                global table1_42
                global table1_50
                global table1_51
                global table1_52
                global table1_60
                global table1_61
                global table1_62
                global table1_70
                global table1_71
                global table1_72
                global table1_80
                global table1_81
                global table1_82

                # Put all data from arrays into the table in a viewable manner
                table1_20 = Label(top,text=dates[0])
                table1_21 = Label(top,text=times[0])
                table1_22 = Label(top,text=activities[0])
                table1_30 = Label(top,text=dates[1])
                table1_31 = Label(top,text=times[1])
                table1_32 = Label(top,text=activities[1])
                table1_40 = Label(top,text=dates[2])
                table1_41 = Label(top,text=times[2])
                table1_42 = Label(top,text=activities[2])
                table1_50 = Label(top,text=dates[3])
                table1_51 = Label(top,text=times[3])
                table1_52 = Label(top,text=activities[3])
                table1_60 = Label(top,text=dates[4])
                table1_61 = Label(top,text=times[4])
                table1_62 = Label(top,text=activities[4])
                table1_70 = Label(top,text=dates[5])
                table1_71 = Label(top,text=times[5])
                table1_72 = Label(top,text=activities[5])
                table1_80 = Label(top,text=dates[6])
                table1_81 = Label(top,text=times[6])
                table1_82 = Label(top,text=activities[6])

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

                # Setup figure
                f = Figure(figsize=(4, 2.25), dpi=100)
                ax = f.add_subplot(111)

                # Configure bar graph
                ax.bar(sleep_df['Date'], sleep_df['SleepHours'], color='skyblue')
                ax.set_title('Sleep Duration for Last 7 Days')
                ax.set_xlabel('Date')
                ax.set_ylabel('Hours of Sleep')
                ax.set_xticklabels(sleep_df['Date'], rotation=45)

                # Post new figure to the application screen
                canvas = FigureCanvasTkAgg(f, master=top)
                canvas.draw()
                canvas.get_tk_widget().grid(row=5,column=1,columnspan=3,rowspan=7,padx=10,pady=10,sticky="NEWS")

                global table2_10
                global table2_11
                global table2_12

                table2_00 = Label(top,text="Time Slept Today")
                table2_01 = Label(top,text="Time Slept this Week")
                table2_02 = Label(top,text="Average Time Slept per Day")
                # If sleep data input data into table
                if (len(sleep_df) > 0):
                    table2_10 = Label(top,text=round(sleep_df.iloc[-1]['SleepHours'],2))
                    table2_11 = Label(top,text=round(sleep_df['SleepHours'].sum(),2))
                    table2_12 = Label(top,text="1")
                else:
                    table2_10 = Label(top,text='N/A')
                    table2_11 = Label(top,text='N/A')
                    table2_12 = Label(top,text='N/A')


                def UpdateGlobals():
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
                        button_1.config(text="Child 2")
                    elif (currentchild == 3):
                        button_1.config(text="Child 3")
                    elif (currentchild == 4):
                        button_1.config(text="Child 4")
                    elif (currentchild == 1):
                        button_1.config(text="Child 1")

                    # Based off of currentchild load csv corresponding to the child
                    filename = 'User'+str(currentchild)+'.csv' 
                    df = pd.read_csv(filename)
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

                    global table1_20
                    global table1_21
                    global table1_22
                    global table1_30
                    global table1_31
                    global table1_32
                    global table1_40
                    global table1_41
                    global table1_42
                    global table1_50
                    global table1_51
                    global table1_52
                    global table1_60
                    global table1_61
                    global table1_62
                    global table1_70
                    global table1_71
                    global table1_72
                    global table1_80
                    global table1_81
                    global table1_82

                    # Put data into table in a viewable manner
                    table1_20.config(text=dates[0])
                    table1_21.config(text=times[0])
                    table1_22.config(text=activities[0])
                    table1_30.config(text=dates[1])
                    table1_31.config(text=times[1])
                    table1_32.config(text=activities[1])
                    table1_40.config(text=dates[2])
                    table1_41.config(text=times[2])
                    table1_42.config(text=activities[2])
                    table1_50.config(text=dates[3])
                    table1_51.config(text=times[3])
                    table1_52.config(text=activities[3])
                    table1_60.config(text=dates[4])
                    table1_61.config(text=times[4])
                    table1_62.config(text=activities[4])
                    table1_70.config(text=dates[5])
                    table1_71.config(text=times[5])
                    table1_72.config(text=activities[5])
                    table1_80.config(text=dates[6])
                    table1_81.config(text=times[6])
                    table1_82.config(text=activities[6])

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
                    ax.set_xticklabels(sleep_df['Date'], rotation=45)

                    # Delete previous graph if it exists

                    if hasattr(top, 'canvas'):
                        top.canvas.get_tk_widget().destroy()

                    # Post new figure to the aplication

                    canvas = FigureCanvasTkAgg(f, master=top)
                    canvas.draw()
                    canvas.get_tk_widget().grid(row=5,column=1,columnspan=3,rowspan=7,padx=10,pady=10,sticky="NEWS")
                    
                    global table2_10
                    global table2_11
                    global table2_12
                    # If sleep data input data into table 
                    if (len(sleep_df) > 0):
                        table2_10.config(text=round(sleep_df.iloc[-1]['SleepHours'],2))
                        table2_11.config(text=round(sleep_df['SleepHours'].sum(),2))
                        table2_12.config(text="1")
                    else:
                        table2_10.config(text='N/A')
                        table2_11.config(text='N/A')
                        table2_12.config(text='N/A')

                def SleepActivityBtn():
                # Data check. Break if data not correct
                    if (str(entry_1.get()) == ""):
                        return
                    if (str(entry_2.get()) == ""):
                        return
                    if (str(entry_3.get()) != "Sleep"):
                        if (str(entry_3.get()) != "Awake"):
                            return


                    # Get date data
                    date = str(entry_1.get())

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
                    time = str(entry_2.get())

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
                    line_to_append = [[tempdate,str(entry_3.get())]]
                    filename = 'User'+str(currentchild)+'.csv'
                    file = open(filename,'a', newline='')
                    writer = csv.writer(file)

                    # Write new data line to csv
                    writer.writerows(line_to_append)

                    # Close csv
                    file.close()
                    
                    # Clear data entry spots
                    entry_1.delete(0, END)
                    entry_2.delete(0, END)
                    entry_3.delete(0, END)

                    # Call to update tables and graph
                    UpdateGlobals()
                    

                button_5 = Button(top,text="Add Sleep Activity",command=SleepActivityBtn)

                def changechild():
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
                    UpdateGlobals()

                # Create Change child button
                button_2 = Button(top,text="Change Child",command=changechild)

                # Assign all objects to a grid
                button_1.grid(row=0,column=0,padx=10,pady=10,sticky="NEWS")
                button_2.grid(row=0,column=1,padx=10,pady=10,sticky="NEWS")
                button_3.grid(row=0,column=2,padx=10,pady=10,sticky="NEWS")
                button_4.grid(row=0,column=3,padx=10,pady=10,sticky="NEWS")
                label_dt.grid(row=0,column=5,columnspan=3,padx=10,pady=10,sticky="NEWS")

                label_1.grid(row=2,column=1,padx=10,pady=10,sticky="NEWS")
                label_2.grid(row=2,column=2,padx=10,pady=10,sticky="NEWS")
                label_3.grid(row=2,column=3,padx=10,pady=10,sticky="NEWS")

                entry_1.grid(row=3,column=1,padx=10,pady=10,sticky="NEWS")
                entry_2.grid(row=3,column=2,padx=10,pady=10,sticky="NEWS")
                entry_3.grid(row=3,column=3,padx=10,pady=10,sticky="NEWS")

                button_5.grid(row=4,column=1,columnspan=3,padx=10,pady=10,sticky="NEWS")

                table1_00_3.grid(row=1,column=5,columnspan=3,padx=10,pady=10,sticky="NEWS")
                table1_10.grid(row=2,column=5,padx=10,pady=10,sticky="NEWS")
                table1_11.grid(row=2,column=6,padx=10,pady=10,sticky="NEWS")
                table1_12.grid(row=2,column=7,padx=10,pady=10,sticky="NEWS")

                table1_20.grid(row=3,column=5,padx=10,pady=10,sticky="NEWS")
                table1_21.grid(row=3,column=6,padx=10,pady=10,sticky="NEWS")
                table1_22.grid(row=3,column=7,padx=10,pady=10,sticky="NEWS")
                table1_30.grid(row=4,column=5,padx=10,pady=10,sticky="NEWS")
                table1_31.grid(row=4,column=6,padx=10,pady=10,sticky="NEWS")
                table1_32.grid(row=4,column=7,padx=10,pady=10,sticky="NEWS")
                table1_40.grid(row=5,column=5,padx=10,pady=10,sticky="NEWS")
                table1_41.grid(row=5,column=6,padx=10,pady=10,sticky="NEWS")
                table1_42.grid(row=5,column=7,padx=10,pady=10,sticky="NEWS")
                table1_50.grid(row=6,column=5,padx=10,pady=10,sticky="NEWS")
                table1_51.grid(row=6,column=6,padx=10,pady=10,sticky="NEWS")
                table1_52.grid(row=6,column=7,padx=10,pady=10,sticky="NEWS")
                table1_60.grid(row=7,column=5,padx=10,pady=10,sticky="NEWS")
                table1_61.grid(row=7,column=6,padx=10,pady=10,sticky="NEWS")
                table1_62.grid(row=7,column=7,padx=10,pady=10,sticky="NEWS")
                table1_70.grid(row=8,column=5,padx=10,pady=10,sticky="NEWS")
                table1_71.grid(row=8,column=6,padx=10,pady=10,sticky="NEWS")
                table1_72.grid(row=8,column=7,padx=10,pady=10,sticky="NEWS")
                table1_80.grid(row=9,column=5,padx=10,pady=10,sticky="NEWS")
                table1_81.grid(row=9,column=6,padx=10,pady=10,sticky="NEWS")
                table1_82.grid(row=9,column=7,padx=10,pady=10,sticky="NEWS")

                table2_00.grid(row=11,column=5,padx=10,pady=10,sticky="NEWS")
                table2_01.grid(row=11,column=6,padx=10,pady=10,sticky="NEWS")
                table2_02.grid(row=11,column=7,padx=10,pady=10,sticky="NEWS")
                table2_10.grid(row=12,column=5,padx=10,pady=10,sticky="NEWS")
                table2_11.grid(row=12,column=6,padx=10,pady=10,sticky="NEWS")
                table2_12.grid(row=12,column=7,padx=10,pady=10,sticky="NEWS")

                # Set all items to the light mode config
                top.configure(bg="white")
                for item in top.grid_slaves():
                    if isinstance(item, Entry):
                        item.configure(bg="lightgray",fg="black")
                    elif isinstance(item, Label):
                        item.configure(bg="lightgray",fg="black")
                    elif isinstance(item, Button):
                        item.configure(bg="lightgray",fg="black")


# Set login button
btn = Button(main,text="Login",command=opentop).pack()


main.configure(bg="white")

# Set all items to the light mode config
for item in main.pack_slaves():
        if isinstance(item, Entry):
            item.configure(bg="white")
        elif isinstance(item, Label):
            item.configure(bg="white")
        elif isinstance(item, Button):
            item.configure(bg="white")

# Execute tkinter
root.mainloop()