import sys
import urllib3, requests, json
try:
     import Tkinter as tk
except ImportError:
     import tkinter as tk
try:
     import ttk
     py3 = False
except ImportError:
     import tkinter.ttk as ttk
     py3 = True

# recieve wml_service_credentials_username, wml_service_credentials_password, and wml_service_credentials_url from the
# service credentials associated with your IBM Cloud Watson Machine Learning Service instance
def get_loan(Gender, Married, Education, SelfEmployed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, CreditHistory, PropertyArea): 
 wml_credentials={
 "url": '',
 "username": '8caf8295---------------------',
 "password": 'b1f36523---------------------'
 }


 #array_of_values_to_be_scored = ["Male","Yes", "Graduate", "No",4583,1508,128,360,1,"Rural"]
 #another_array_of_values_to_be_scored =["Female","No", "Graduate","No",3510, 0, 76,360,0,"Urban"]
 array_of_values_to_be_scored = [Gender, Married, Education, SelfEmployed, int(ApplicantIncome), int(CoapplicantIncome), int(LoanAmount), int(Loan_Amount_Term), int(CreditHistory), PropertyArea]
 another_array_of_values_to_be_scored =["Female","No", "Graduate","No",3510, 0, 76,360,0,"Urban"]


 headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
 url = '{}/v3/identity/token'.format(wml_credentials['url'])
 response = requests.get(url, headers=headers)
 mltoken = json.loads(response.text).get('token')

 header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

#manually define and pass the array(s) of values to be scored in the next line
 payload_scoring = {"fields": ["Gender", "Married", "Education", "SelfEmployed", "ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "CreditHistory", "PropertyArea"], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}

 response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/-------------', json=payload_scoring, headers=header)
 print("Scoring response")
 print(json.loads(response_scoring.text))
 j= json.loads(response_scoring.text)
 global mylist
 mylist =j['values'][0]
 print(mylist[14])
 print(j['values'][0])
 Label3 = mylist[14]

def set_Tk_var():
       global combobox
       combobox = tk.StringVar()
       global che73
       che73 = tk.StringVar()
   
def init(top, gui, *args, **kwargs):
       global w, top_level, root
       w = gui
       top_level = top
       root = top
   
def destroy_window():
       global top_level
       top_level.destroy()
       top_level = None

def vp_start_gui():
     '''Starting point when module is the main routine.'''
     global val, w, root
     root = tk.Tk()
     set_Tk_var()
     top = Toplevel1(root)
     init(root, top)
     root.mainloop()
 
w = None
def create_Toplevel1(root, * args, ** kwargs):
     '''Starting point when module is imported by another program.'''
     global w, w_win, rt
     rt = root
     w = tk.Toplevel(root)
     set_Tk_var()
     top = Toplevel1(w)
     init(w, top, * args, ** kwargs)
     return (w, top)
 
def destroy_Toplevel1():
     global w
     w.destroy()
     w = None
 
class Toplevel1 :
     def __init__(self, top=None):
         _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
         _fgcolor = '#000000'  # X11 color: 'black'
         _compcolor = '#d9d9d9' # X11 color: 'gray85'
        
         _ana2color = '#ececec' # Closest X11 color: 'gray92'
         font10 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
             "italic -underline 0 -overstrike 0"
         font9 = "-family {Segoe UI} -size 10 -weight bold -slant roman"  \
             " -underline 0 -overstrike 0"
         self.style = ttk.Style()
         if sys.platform == "win32":
             self.style.theme_use('winnative')
         self.style.configure('.', background=_bgcolor)
         self.style.configure('.', foreground=_fgcolor)
         self.style.configure('.', font="TkDefaultFont")
         self.style.map('.', background=
             [('selected', _compcolor), ('active', _ana2color)])
 
         top.geometry("710x547+606+254")
         top.title("Cognitive Computers")
         top.configure(background="#d9d9d9")
 
         self.Canvas1 = tk.Canvas(top)
         self.Canvas1.place(relx=0.028, rely=0.055, relheight=0.938
                 , relwidth=0.934)
         self.Canvas1.configure(background="#d9d9d9")
         self.Canvas1.configure(borderwidth="2")
         self.Canvas1.configure(insertbackground="black")
         self.Canvas1.configure(relief="ridge")
         self.Canvas1.configure(selectbackground="#c4c4c4")
         self.Canvas1.configure(selectforeground="black")
         self.Canvas1.configure(width=663)
 
         self.TButton1 = ttk.Button(self.Canvas1)
         self.TButton1.place(relx=0.226, rely=0.702, height=45, width=126)
         self.TButton1.configure(takefocus="")
         self.TButton1.configure(text='''RESULT''')
         self.TButton1.configure(width=126)
         self.TButton1.configure(command=lambda: get_loan(self.Text1_18.get('1.0'),self.Text1_20.get('1.0'),self.Text1_19.get('1.0'),self.Text1_15.get('1.0'),self.Text1_11.get('1.0'),self.Text1_16.get('1.0'),self.Text1_12.get('1.0'),self.Text1_17.get('1.0'),self.Text1_13.get('1.0'),self.Text1_21.get('1.0')))
         
 
         self.Label1 = tk.Label(self.Canvas1)
         self.Label1.place(relx=0.023, rely=0.117, height=31, width=64)
         self.Label1.configure(background="#d8d8d8")
         self.Label1.configure(disabledforeground="#a3a3a3")
         self.Label1.configure(font=font9)
         self.Label1.configure(foreground="#000000")
         self.Label1.configure(text='''Gender''')
         self.Label1.configure(width=64)
 
         self.Label1_1 = tk.Label(self.Canvas1)
         self.Label1_1.place(relx=0.528, rely=0.107, height=31, width=64)
         self.Label1_1.configure(activebackground="#f9f9f9")
         self.Label1_1.configure(activeforeground="black")
         self.Label1_1.configure(background="#d8d8d8")
         self.Label1_1.configure(disabledforeground="#a3a3a3")
         self.Label1_1.configure(font=font9)
         self.Label1_1.configure(foreground="#000000")
         self.Label1_1.configure(highlightbackground="#d9d9d9")
         self.Label1_1.configure(highlightcolor="black")
         self.Label1_1.configure(text='''Married''')
 
         self.Label1_2 = tk.Label(self.Canvas1)
         self.Label1_2.place(relx=0.023, rely=0.195, height=31, width=64)
         self.Label1_2.configure(activebackground="#f9f9f9")
         self.Label1_2.configure(activeforeground="black")
         self.Label1_2.configure(background="#d8d8d8")
         self.Label1_2.configure(disabledforeground="#a3a3a3")
         self.Label1_2.configure(font=font9)
         self.Label1_2.configure(foreground="#000000")
         self.Label1_2.configure(highlightbackground="#d9d9d9")
         self.Label1_2.configure(highlightcolor="black")
         self.Label1_2.configure(text='''Education''')
 
         self.Label1_3 = tk.Label(self.Canvas1)
         self.Label1_3.place(relx=0.513, rely=0.195, height=31, width=124)
         self.Label1_3.configure(activebackground="#f9f9f9")
         self.Label1_3.configure(activeforeground="black")
         self.Label1_3.configure(background="#d8d8d8")
         self.Label1_3.configure(disabledforeground="#a3a3a3")
         self.Label1_3.configure(font=font9)
         self.Label1_3.configure(foreground="#000000")
         self.Label1_3.configure(highlightbackground="#d9d9d9")
         self.Label1_3.configure(highlightcolor="black")
         self.Label1_3.configure(text='''SelfEmployed''')
         self.Label1_3.configure(width=124)
 
         self.Label1_4 = tk.Label(self.Canvas1)
         self.Label1_4.place(relx=0.023, rely=0.292, height=31, width=114)
         self.Label1_4.configure(activebackground="#f9f9f9")
         self.Label1_4.configure(activeforeground="black")
         self.Label1_4.configure(background="#d8d8d8")
         self.Label1_4.configure(disabledforeground="#a3a3a3")
         self.Label1_4.configure(font=font9)
         self.Label1_4.configure(foreground="#000000")
         self.Label1_4.configure(highlightbackground="#d9d9d9")
         self.Label1_4.configure(highlightcolor="black")
         self.Label1_4.configure(text='''Applicant Income''')
         self.Label1_4.configure(width=114)
 
         self.Label1_5 = tk.Label(self.Canvas1)
         self.Label1_5.place(relx=0.535, rely=0.292, height=41, width=134)
         self.Label1_5.configure(activebackground="#f9f9f9")
         self.Label1_5.configure(activeforeground="black")
         self.Label1_5.configure(background="#d8d8d8")
         self.Label1_5.configure(disabledforeground="#a3a3a3")
         self.Label1_5.configure(font=font9)
         self.Label1_5.configure(foreground="#000000")
         self.Label1_5.configure(highlightbackground="#d9d9d9")
         self.Label1_5.configure(highlightcolor="black")
         self.Label1_5.configure(text='''Coapplicant Income''')
         self.Label1_5.configure(width=134)
 
         self.Label1_6 = tk.Label(self.Canvas1)
         self.Label1_6.place(relx=0.023, rely=0.39, height=31, width=94)
         self.Label1_6.configure(activebackground="#f9f9f9")
         self.Label1_6.configure(activeforeground="black")
         self.Label1_6.configure(background="#d8d8d8")
         self.Label1_6.configure(disabledforeground="#a3a3a3")
         self.Label1_6.configure(font=font9)
         self.Label1_6.configure(foreground="#000000")
         self.Label1_6.configure(highlightbackground="#d9d9d9")
         self.Label1_6.configure(highlightcolor="black")
         self.Label1_6.configure(text='''Loan Amount''')
         self.Label1_6.configure(width=94)
 
         self.Label1_7 = tk.Label(self.Canvas1)
         self.Label1_7.place(relx=0.52, rely=0.39, height=31, width=64)
         self.Label1_7.configure(activebackground="#f9f9f9")
         self.Label1_7.configure(activeforeground="black")
         self.Label1_7.configure(background="#d8d8d8")
         self.Label1_7.configure(disabledforeground="#a3a3a3")
         self.Label1_7.configure(font=font9)
         self.Label1_7.configure(foreground="#000000")
         self.Label1_7.configure(highlightbackground="#d9d9d9")
         self.Label1_7.configure(highlightcolor="black")
         self.Label1_7.configure(text='''Term''')
 
         self.Label1_8 = tk.Label(self.Canvas1)
         self.Label1_8.place(relx=0.015, rely=0.487, height=31, width=94)
         self.Label1_8.configure(activebackground="#f9f9f9")
         self.Label1_8.configure(activeforeground="black")
         self.Label1_8.configure(background="#d8d8d8")
         self.Label1_8.configure(disabledforeground="#a3a3a3")
         self.Label1_8.configure(font=font9)
         self.Label1_8.configure(foreground="#000000")
         self.Label1_8.configure(highlightbackground="#d9d9d9")
         self.Label1_8.configure(highlightcolor="black")
         self.Label1_8.configure(text='''Credit History''')
         self.Label1_8.configure(width=94)
 
         self.Label1_9 = tk.Label(self.Canvas1)
         self.Label1_9.place(relx=0.528, rely=0.478, height=31, width=64)
         self.Label1_9.configure(activebackground="#f9f9f9")
         self.Label1_9.configure(activeforeground="black")
         self.Label1_9.configure(background="#d8d8d8")
         self.Label1_9.configure(disabledforeground="#a3a3a3")
         self.Label1_9.configure(font=font9)
         self.Label1_9.configure(foreground="#000000")
         self.Label1_9.configure(highlightbackground="#d9d9d9")
         self.Label1_9.configure(highlightcolor="black")
         self.Label1_9.configure(text='''Area''')
 
         self.Text1_11 = tk.Text(self.Canvas1)
         self.Text1_11.place(relx=0.226, rely=0.292, relheight=0.066
                 , relwidth=0.202)
         self.Text1_11.configure(background="white")
         self.Text1_11.configure(font="TkTextFont")
         self.Text1_11.configure(foreground="red")
         self.Text1_11.configure(highlightbackground="#d9d9d9")
         self.Text1_11.configure(highlightcolor="black")
         self.Text1_11.configure(insertbackground="black")
         self.Text1_11.configure(selectbackground="#c4c4c4")
         self.Text1_11.configure(selectforeground="black")
         self.Text1_11.configure(width=134)
         self.Text1_11.configure(wrap="word")
 
         self.Text1_12 = tk.Text(self.Canvas1)
         self.Text1_12.place(relx=0.226, rely=0.39, relheight=0.066
                 , relwidth=0.202)
         self.Text1_12.configure(background="white")
         self.Text1_12.configure(font="TkTextFont")
         self.Text1_12.configure(foreground="yellow")
         self.Text1_12.configure(highlightbackground="#d9d9d9")
         self.Text1_12.configure(highlightcolor="black")
         self.Text1_12.configure(insertbackground="black")
         self.Text1_12.configure(selectbackground="#c4c4c4")
         self.Text1_12.configure(selectforeground="black")
         self.Text1_12.configure(width=134)
         self.Text1_12.configure(wrap="word")
 
         self.Text1_13 = tk.Text(self.Canvas1)
         self.Text1_13.place(relx=0.226, rely=0.487, relheight=0.066
                 , relwidth=0.202)
         self.Text1_13.configure(background="white")
         self.Text1_13.configure(font="TkTextFont")
         self.Text1_13.configure(foreground="black")
         self.Text1_13.configure(highlightbackground="#d9d9d9")
         self.Text1_13.configure(highlightcolor="black")
         self.Text1_13.configure(insertbackground="black")
         self.Text1_13.configure(selectbackground="#c4c4c4")
         self.Text1_13.configure(selectforeground="black")
         self.Text1_13.configure(width=134)
         self.Text1_13.configure(wrap="word")
 
         self.Text1_15 = tk.Text(self.Canvas1)
         self.Text1_15.place(relx=0.762, rely=0.195, relheight=0.066
                 , relwidth=0.202)
         self.Text1_15.configure(background="white")
         self.Text1_15.configure(font="TkTextFont")
         self.Text1_15.configure(foreground="black")
         self.Text1_15.configure(highlightbackground="#d9d9d9")
         self.Text1_15.configure(highlightcolor="black")
         self.Text1_15.configure(insertbackground="black")
         self.Text1_15.configure(selectbackground="#c4c4c4")
         self.Text1_15.configure(selectforeground="black")
         self.Text1_15.configure(width=134)
         self.Text1_15.configure(wrap="word")
 
         self.Text1_16 = tk.Text(self.Canvas1)
         self.Text1_16.place(relx=0.762, rely=0.292, relheight=0.066
                 , relwidth=0.202)
         self.Text1_16.configure(background="white")
         self.Text1_16.configure(font="TkTextFont")
         self.Text1_16.configure(foreground="black")
         self.Text1_16.configure(highlightbackground="#d9d9d9")
         self.Text1_16.configure(highlightcolor="black")
         self.Text1_16.configure(insertbackground="black")
         self.Text1_16.configure(selectbackground="#c4c4c4")
         self.Text1_16.configure(selectforeground="black")
         self.Text1_16.configure(width=134)
         self.Text1_16.configure(wrap="word")
 
         self.Text1_17 = tk.Text(self.Canvas1)
         self.Text1_17.place(relx=0.762, rely=0.39, relheight=0.066
                 , relwidth=0.202)
         self.Text1_17.configure(background="white")
         self.Text1_17.configure(font="TkTextFont")
         self.Text1_17.configure(foreground="black")
         self.Text1_17.configure(highlightbackground="#d9d9d9")
         self.Text1_17.configure(highlightcolor="black")
         self.Text1_17.configure(insertbackground="black")
         self.Text1_17.configure(selectbackground="#c4c4c4")
         self.Text1_17.configure(selectforeground="black")
         self.Text1_17.configure(width=134)
         self.Text1_17.configure(wrap="word")
 
         self.Label2 = tk.Label(self.Canvas1)
         self.Label2.place(relx=0.302, rely=0.019, height=31, width=284)
         self.Label2.configure(background="#d9d9d9")
         self.Label2.configure(disabledforeground="#a3a3a3")
         self.Label2.configure(font=font10)
         self.Label2.configure(foreground="#000000")
         self.Label2.configure(text='''Loan Predictor''')
         self.Label2.configure(width=284)
 
         self.Label3 = tk.Label(self.Canvas1)
         self.Label3.place(relx=0.437, rely=0.721, height=100, width=200)
         self.Label3.configure(background="#d9d9d9")
         self.Label3.configure(disabledforeground="#a3a3a3")
         self.Label3.configure(foreground="#000000")
         #self.Label3.configure(text='''json.loads(response_scoring.text)''')
         if not (mylist):
          self.Label3.configure(text='')
             
         else:    
          
          self.Label3.configure(text=mylist[14])
         self.Label3.configure(width=124)
 
         self.Text1_18 = tk.Text(self.Canvas1)
         self.Text1_18.place(relx=0.226, rely=0.097, relheight=0.066
          , relwidth=0.202)
         self.Text1_18.configure(background="white")
         self.Text1_18.configure(font="TkTextFont")
         self.Text1_18.configure(foreground="black")
         self.Text1_18.configure(highlightbackground="#d9d9d9")
         self.Text1_18.configure(highlightcolor="black")
         self.Text1_18.configure(insertbackground="black")
         self.Text1_18.configure(selectbackground="#c4c4c4")
         self.Text1_18.configure(selectforeground="black")
         self.Text1_18.configure(width=134)
         self.Text1_18.configure(wrap="word")
 
         self.Text1_19 = tk.Text(self.Canvas1)
         self.Text1_19.place(relx=0.226, rely=0.195, relheight=0.066
          , relwidth=0.202)
         self.Text1_19.configure(background="white")
         self.Text1_19.configure(font="TkTextFont")
         self.Text1_19.configure(foreground="black")
         self.Text1_19.configure(highlightbackground="#d9d9d9")
         self.Text1_19.configure(highlightcolor="black")
         self.Text1_19.configure(insertbackground="black")
         self.Text1_19.configure(selectbackground="#c4c4c4")
         self.Text1_19.configure(selectforeground="black")
         self.Text1_19.configure(width=134)
         self.Text1_19.configure(wrap="word")
 
         self.Text1_20 = tk.Text(self.Canvas1)
         self.Text1_20.place(relx=0.762, rely=0.097, relheight=0.066
          , relwidth=0.202)
         self.Text1_20.configure(background="white")
         self.Text1_20.configure(font="TkTextFont")
         self.Text1_20.configure(foreground="black")
         self.Text1_20.configure(highlightbackground="#d9d9d9")
         self.Text1_20.configure(highlightcolor="black")
         self.Text1_20.configure(insertbackground="black")
         self.Text1_20.configure(selectbackground="#c4c4c4")
         self.Text1_20.configure(selectforeground="black")
         self.Text1_20.configure(width=134)
         self.Text1_20.configure(wrap="word")
 
         self.Text1_21 = tk.Text(self.Canvas1)
         self.Text1_21.place(relx=0.762, rely=0.487, relheight=0.066
          , relwidth=0.202)
         self.Text1_21.configure(background="white")
         self.Text1_21.configure(font="TkTextFont")
         self.Text1_21.configure(foreground="black")
         self.Text1_21.configure(highlightbackground="#d9d9d9")
         self.Text1_21.configure(highlightcolor="black")
         self.Text1_21.configure(insertbackground="black")
         self.Text1_21.configure(selectbackground="#c4c4c4")
         self.Text1_21.configure(selectforeground="black")
         self.Text1_21.configure(width=134)
         self.Text1_21.configure(wrap="word")
 
if __name__ == '__main__':
     vp_start_gui()



