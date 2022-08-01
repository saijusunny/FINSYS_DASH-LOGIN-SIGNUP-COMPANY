import matplotlib.pyplot as plt
from calendar import c
from cgitb import enable, reset, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
from tkinter import font
from tkinter.font import BOLD
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Canvas

import customtkinter
import PIL.Image
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

# fbilldb = mysql.connector.connect(
#     host="localhost", user="root", password="", database="fbilling", port="3306"
# )
# fbcursor = fbilldb.cursor()

root=Tk()
root.geometry("1366x768+0+0")

root.title("Fin sYs")

p1 = PhotoImage(file = 'images/favicon.png')
root.iconphoto(False, p1)

#-------------------------------------------------------------------------------------------------------------------------Images
# banking = PhotoImage(file="images/banking.PNG")
# sales = PhotoImage(file="images/sheet.PNG")
# expenses = PhotoImage(file="images/expense.PNG")
# payroll = PhotoImage(file="images/payroll.PNG")
# report = PhotoImage(file="images/reports.PNG")
# taxes = PhotoImage(file="images/taxes.PNG")
# accounts = PhotoImage(file="images/accounting.PNG")



imgr1 =PIL.Image.open("images\logs.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)

mnu =PIL.Image.open("images\menu bar.PNG")
mnus=ImageTk.PhotoImage(mnu)


srh =PIL.Image.open("images\search.PNG")
srh_img=ImageTk.PhotoImage(srh)

stn =PIL.Image.open("images\Settings.PNG")
stn_img=ImageTk.PhotoImage(stn)

logo =PIL.Image.open("images\logo-icon.png")
resized_image= logo.resize((50,50))
mai_logo= ImageTk.PhotoImage(resized_image)

sig_up =PIL.Image.open("images/register.png")
resized_sign_up= sig_up.resize((500,400))
sign_up=ImageTk.PhotoImage(resized_sign_up)

#------------------------------------------------------------------------------------------------------------Login Button Function

def main_sign_in():
    try:
        main_frame_signup.pack_forget()
    except:
        pass
    try:
        main_frame_signin.pack_forget()
    except:
        pass
    Sys_top_frame=Frame(root, height=70,bg="#213b52")
    Sys_top_frame.pack(fill=X,)

    #---------------------------------------------------------------------------------------Top Menu
    tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Logo Name Frame
    tp_lb_nm.grid(row=1,column=1,sticky='nsew')
    tp_lb_nm.grid_rowconfigure(0,weight=1)
    tp_lb_nm.grid_columnconfigure(0,weight=1)

    label = Label(tp_lb_nm, image = mai_logo,height=70,bg="#213b52",border=0)
    label.grid(row=2,column=1,sticky='nsew')
    label = Label(tp_lb_nm, text="Fin sYs",bg="#213b52", fg="white",font=('Calibri 30 bold'),border=0)
    label.grid(row=2,column=2,sticky='nsew')
  
    mnu_btn = Button(tp_lb_nm, image=mnus, bg="white", fg="black",border=0)
    mnu_btn.grid(row=2,column=4,padx=50)

    

    tp_lb_srh=LabelFrame(Sys_top_frame,bg="#213b52")#-------------------------Serch area Frame
    tp_lb_srh.grid(row=1,column=2,sticky='nsew')
    tp_lb_srh.grid_rowconfigure(0,weight=1)
    tp_lb_srh.grid_columnconfigure(0,weight=1)

    def srh_fn(event):
        if srh_top.get()=="Search":
            srh_top.delete(0,END)
        else:
            pass

    srh_top = Entry(tp_lb_srh, width=50, font=('Calibri 16'))
    srh_top.insert(0,"Search")
    srh_top.bind("<Button-1>",srh_fn)
    srh_top.grid(row=2,column=1,padx=(30,0), pady=20,sticky='nsew')

    srh_btn = Button(tp_lb_srh, image=srh_img, bg="#213b52", fg="black",border=0)
    srh_btn.grid(row=2,column=4,padx=(0,30))

    #------------------------------------------------------settings 
    def close_lst_2():
            lst_prf2.place_forget()
            set_btn4 = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
            set_btn4.grid(row=2,column=5,padx=(0,30))
            
    def settings():
        

        # create a list box
        stng = ("Accounts And Settings","Customize From Style","Chart Of Accounts")

        stngs = StringVar(value=stng)
        global lst_prf2
        lst_prf2 = Listbox(root,listvariable=stngs,height=3 ,selectmode='extended',bg="black",fg="white")

        lst_prf2.place(relx=0.70, rely=0.10)
        lst_prf2.bind('<<ListboxSelect>>', )
        set_btn.grid_forget()
        set_btn2 = Button(tp_lb_srh, image=stn_img,command=close_lst_2, bg="#213b52", fg="black",border=0)
        set_btn2.grid(row=2,column=5,padx=(0,30))

    set_btn = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
    set_btn.grid(row=2,column=5,padx=(0,30))

    tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Notification
    tp_lb_nm.grid(row=1,column=3,sticky='nsew')
    tp_lb_nm.grid_rowconfigure(0,weight=1)
    tp_lb_nm.grid_columnconfigure(0,weight=1)
    srh_btn = Button(tp_lb_nm, image=stn_img, bg="#213b52", fg="black",border=0)
    srh_btn.grid(row=0,column=0,padx=35)
    
    tp_lb_npr=LabelFrame(Sys_top_frame,bg="#213b52")#---------------------------profile area name
    tp_lb_npr.grid(row=1,column=4,sticky='nsew')
    tp_lb_npr.grid_rowconfigure(0,weight=1)
    tp_lb_npr.grid_columnconfigure(0,weight=1)

    label = Label(tp_lb_npr, text="Errors",bg="#213b52", fg="white", anchor="center",width=10,font=('Calibri 16 bold'),border=0)
    label.grid(row=1,column=1,sticky='nsew')
    label = Label(tp_lb_npr, text="Online",bg="#213b52", fg="white",width=15,font=('Calibri 12 bold'),border=0)
    label.grid(row=2,column=1,sticky='nsew')

    pro =PIL.Image.open("images/user.png")
    resized_pro= pro.resize((20,20))
    pro_pic= ImageTk.PhotoImage(resized_pro)
    
    def lst_frt():
        lst_prf.place_forget()
        srh_btn3 = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=profile)
        srh_btn3.grid(row=2,column=2,padx=15)
    def lst_prf_slt(event):
        def edit_profile():
            def responsive_widgets_edit(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                


                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/13
                y2 = dheight/.53

                dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )                              

                
                # dcanvas.coords("bg_polygen_pr",dwidth/16,dheight/.6,dwidth/1.07,dheight/9)
                dcanvas.coords("my_pro",dwidth/2.3,dheight/12.5)

                dcanvas.coords("pr_hr_l",dwidth/16,dheight/7,dwidth/1.07,dheight/7)
                dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                dcanvas.coords("pr_crpass_lb",dwidth/17.075,dheight/1.33)
                dcanvas.coords("pr_crpass_ent",dwidth/17.075,dheight/1.26)
                dcanvas.coords("pr_re_pass_lb",dwidth/17.075,dheight/1.16)
                dcanvas.coords("pr_re_pass_ent",dwidth/17.075,dheight/1.1)
                dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)
                dcanvas.coords("pr_new_pass_lb",dwidth/1.92,dheight/1.33)
                dcanvas.coords("pr_new_pass_ent",dwidth/1.92,dheight/1.26)

                
                #-------------------------------------------------------------------------company section
                dcanvas.coords("cmp_hd",dwidth/20,dheight/1)
                dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/0.93)
                dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/0.89)
                dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/0.84)
                dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/0.81)
                dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/0.77)
                dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.745)
                dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.712)
                dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.69)
                dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.66)
                dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.64)
                dcanvas.coords("cmp_file_lb",dwidth/17.075,dheight/.615)
                dcanvas.coords("cmp_file_ent",dwidth/17.075,dheight/.6)
                

                #--------------------------------------------------------------------------company right

                dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/0.93)
                dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/0.89)
                dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/0.84)
                dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/0.81)
                dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/0.77)
                dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.745)
                dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.712)
                dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.69)
                dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.66)
                dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.64)
                dcanvas.coords("btn_edit",dwidth/2.4,dheight/.57)
            
            Sys_mains_frame_pr.place_forget()
            global Sys_mains_frame_pr_ed
            Sys_mains_frame_pr_ed=Frame(tab1, height=750)
            Sys_mains_frame_pr_ed.grid(row=0,column=0,sticky='nsew')
            Sys_mains_frame_pr_ed.grid_rowconfigure(0,weight=1)
            Sys_mains_frame_pr_ed.grid_columnconfigure(0,weight=1)

            pr_canvas_ed=Canvas(Sys_mains_frame_pr_ed,height=766,width=1340,scrollregion=(0,0,766,1650),bg="#2f516f",border=0)
            pr_canvas_ed.bind('<Configure>', responsive_widgets_edit)
            
            pr_myscrollbar_ed=Scrollbar(Sys_mains_frame_pr_ed,orient="vertical",command=pr_canvas_ed.yview)
            pr_canvas_ed.configure(yscrollcommand=pr_myscrollbar_ed.set)

            pr_myscrollbar_ed.pack(side="right",fill="y")
            pr_canvas_ed.pack(fill=X)

            rth2 = pr_canvas_ed.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_pr"),smooth=True,)

            grd1c=Label(pr_canvas_ed, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
            win_inv1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

            pr_canvas_ed.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
            #----------------------------------------------------------------------------------------Personal info
            pr_hd=Label(pr_canvas_ed, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

            fir_name=Label(pr_canvas_ed, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

            fr_name_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

            pr_em_lb=Label(pr_canvas_ed, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

            pr_crpass_lb=Label(pr_canvas_ed, text="Enter your Current Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_lb,tag=("pr_crpass_lb"))

            pr_crpass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_ent,tag=("pr_crpass_ent"))

            pr_re_pass_lb=Label(pr_canvas_ed, text="Re-type new Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_lb,tag=("pr_re_pass_lb"))

            pr_re_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_ent,tag=("pr_re_pass_ent"))


            em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

            last_nm_lb=Label(pr_canvas_ed, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

            lst_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

            usr_nm_lb=Label(pr_canvas_ed, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

            usr_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

            pr_new_pass_lb=Label(pr_canvas_ed, text="Enter New Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_lb,tag=("pr_new_pass_lb"))

            pr_new_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_ent,tag=("pr_new_pass_ent"))


            # #------------------------------------------------------------------------------------------------COMPANY SECTION
            cmp_hd=Label(pr_canvas_ed, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

            cmp_nm_lb=Label(pr_canvas_ed, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

            cmp_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

            cmp_cty_lb=Label(pr_canvas_ed, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

            cmp_cty_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

            cmp_pin_lb=Label(pr_canvas_ed, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

            cmp_pin_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

            cmp_ph_lb=Label(pr_canvas_ed, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

            cmp_ph_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

            cmp_indest_lb=Label(pr_canvas_ed, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

            cmp_indest_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

            # #----------------------------------------------------------------------------------------------------RIGHT SIDE
            cmp_addr_lb=Label(pr_canvas_ed, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

            cmp_addr_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

            cmp_st_lb=Label(pr_canvas_ed, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

            cmp_st_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

            cmp_em_lb=Label(pr_canvas_ed, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

            cmp_em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

            cmp_lg_nm=Label(pr_canvas_ed, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

            cmp_lg_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

            cmp_typ_lb=Label(pr_canvas_ed, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

            cmp_typ_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))

            cmp_file_lb=Label(pr_canvas_ed, text="File",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_lb,tag=("cmp_file_lb"))

            cmp_file_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_ent,tag=("cmp_file_ent"))


            btn_edit = Button(pr_canvas_ed, text='Update Profile', command=edit_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))

        
        selected_indices = lst_prf.curselection()
        selected_langs = ",".join([lst_prf.get(i) for i in selected_indices])
        lst_prf.place_forget()

        def pr_responsive_widgets(event):
                
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
             
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/13
                y2 = dheight/.6

                dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )                   
 
                dcanvas.coords("my_pro",dwidth/2.3,dheight/12.5)

                dcanvas.coords("pr_hr_l",dwidth/16,dheight/7,dwidth/1.07,dheight/7)
                dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                
                dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)

                #-------------------------------------------------------------------------company section
                dcanvas.coords("cmp_hd",dwidth/20,dheight/1.32)
                dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/1.22)
                dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/1.16)
                dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/1.07)
                dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/1.02)
                dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/.95)
                dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.91)
                dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.86)
                dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.83)
                dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.78)
                dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.755)

                #--------------------------------------------------------------------------company right

                dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/1.22)
                dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/1.16)
                dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/1.07)
                dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/1.02)
                dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/.95)
                dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.91)
                dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.86)
                dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.83)
                dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.78)
                dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.755)
                dcanvas.coords("btn_edit",dwidth/2.4,dheight/.71)

        if selected_langs=="Profile":
            # canvas.pack_forget()
            # myscrollbar.pack_forget()
            # Sys_mains_frame.pack_forget()
            
            Sys_mains_frame_pr=Frame(tab1, height=750,bg="#2f516f",)
            Sys_mains_frame_pr.grid(row=0,column=0,sticky='nsew')
            Sys_mains_frame_pr.grid_rowconfigure(0,weight=1)
            Sys_mains_frame_pr.grid_columnconfigure(0,weight=1)

            pr_canvas=Canvas(Sys_mains_frame_pr,height=700,width=1340,scrollregion=(0,0,700,1300),bg="#2f516f",border=0)
            pr_canvas.bind("<Configure>", pr_responsive_widgets)
            
            pr_myscrollbar=Scrollbar(Sys_mains_frame_pr,orient="vertical",command=pr_canvas.yview)
            pr_canvas.configure(yscrollcommand=pr_myscrollbar.set)

            pr_myscrollbar.pack(side="right",fill="y")
            pr_canvas.pack(fill=X)

            rth2 = pr_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",smooth=True,tags=("bg_polygen_pr"))

            grd1c=Label(pr_canvas, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
            win_inv1 = pr_canvas.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

            pr_canvas.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
            #----------------------------------------------------------------------------------------Personal info
            pr_hd=Label(pr_canvas, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

            fir_name=Label(pr_canvas, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

            fr_name_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

            pr_em_lb=Label(pr_canvas, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

            em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

            last_nm_lb=Label(pr_canvas, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

            lst_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

            usr_nm_lb=Label(pr_canvas, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

            usr_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

            #------------------------------------------------------------------------------------------------COMPANY SECTION
            cmp_hd=Label(pr_canvas, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

            cmp_nm_lb=Label(pr_canvas, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

            cmp_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

            cmp_cty_lb=Label(pr_canvas, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

            cmp_cty_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

            cmp_pin_lb=Label(pr_canvas, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

            cmp_pin_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

            cmp_ph_lb=Label(pr_canvas, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

            cmp_ph_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

            cmp_indest_lb=Label(pr_canvas, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

            cmp_indest_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

            #----------------------------------------------------------------------------------------------------RIGHT SIDE
            cmp_addr_lb=Label(pr_canvas, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

            cmp_addr_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

            cmp_st_lb=Label(pr_canvas, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

            cmp_st_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

            cmp_em_lb=Label(pr_canvas, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

            cmp_em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

            cmp_lg_nm=Label(pr_canvas, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

            cmp_lg_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

            cmp_typ_lb=Label(pr_canvas, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

            cmp_typ_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))


            btn_edit = Button(pr_canvas, text='Edit Profile', command=edit_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))
        
        elif selected_langs=="Log Out":
            
            Sys_top_frame2.pack_forget()
            Sys_top_frame.pack_forget()
            main_frame_signin.pack(fill=X,)
        elif selected_langs== "Dashboard":
            try:
                Sys_mains_frame_pr_ed.place_forget()
            except:
                pass
            try:
                
                Sys_mains_frame_pr.place_forget()
            except:
                pass

        else:
            pass

    def profile():
        # create a list box
        langs = ("Dashboard","Profile","Log Out")

        langs_var = StringVar(value=langs)
        global lst_prf
        lst_prf = Listbox(root,listvariable=langs_var,height=3 ,selectmode='extended',bg="black",fg="white")

        lst_prf.place(relx=0.90, rely=0.10)
        lst_prf.bind('<<ListboxSelect>>', lst_prf_slt)
        srh_btn.grid_forget()
        srh_btn2 = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=lst_frt)
        srh_btn2.grid(row=2,column=2,padx=15)
   
    srh_btn = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=profile)
    srh_btn.grid(row=2,column=2,padx=15)

    Sys_top_frame2=Frame(root, height=10,bg="#213b52")
    Sys_top_frame2.pack(fill=X,)
    
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="#213b52",foreground="white", width=150,anchor="center", padding=5)
    s.map('TNotebook.Tab',background=[("selected","#2f516f")])
    def right_nav():
        
        tabControl.pack_forget()
        btn_nav.place_forget()
        tabControl2.pack(expand = 1, fill ="both")
        btn_nav2.place(relx=0, rely=0)
        try:
            btn_nav3.place_forget()
        except:
            pass
    def left_nav():
        
        tabControl2.pack_forget()
        btn_nav2.place_forget()
        tabControl.pack(expand = 1, fill ="both")
        global btn_nav3
        btn_nav3=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
        btn_nav3.place(relx=0.97, rely=0)

    tabControl = ttk.Notebook(Sys_top_frame2)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6=  ttk.Frame(tabControl)
    tab7 = ttk.Frame(tabControl)
    tab8 = ttk.Frame(tabControl)
    
    
    btn_nav=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
    btn_nav.place(relx=0.97, rely=0)
    tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
    tabControl.add(tab2,compound = LEFT, text ='Banking')
    tabControl.add(tab3,compound = LEFT, text ='Sales')
    tabControl.add(tab4,compound = LEFT, text ='Expenses')
    tabControl.add(tab5,compound = LEFT, text ='Payroll') 
    tabControl.add(tab6,compound = LEFT, text ='Report')
    tabControl.add(tab7,compound = LEFT, text ='Taxes')
    tabControl.add(tab8,compound = LEFT, text ='Accounting')
    
    tabControl.pack(expand = 1, fill ="both")


    
    tabControl2 = ttk.Notebook(Sys_top_frame2)
    tab9 =  ttk.Frame(tabControl2)
    tab10=  ttk.Frame(tabControl2)
    tab11 = ttk.Frame(tabControl2)
    tab12=  ttk.Frame(tabControl2)
    tab13 = ttk.Frame(tabControl2)
    tab14 = ttk.Frame(tabControl2)
    tab15 =  ttk.Frame(tabControl2)

    btn_nav2=Button(Sys_top_frame2,text="<<", command=left_nav, width=3, bg="#213b52",fg="white")
    
        
    tabControl2.add(tab9,compound = LEFT, text ='My Account')
    tabControl2.add(tab10,compound = LEFT, text ='Cash Management')
    tabControl2.add(tab11,compound = LEFT, text ='Production')
    tabControl2.add(tab12,compound = LEFT, text ='Quality Management')
    tabControl2.add(tab13,compound = LEFT, text ='Project Management')
    tabControl2.add(tab14,compound = LEFT, text ='Usage Decisions')
    tabControl2.add(tab15,compound = LEFT, text ='Account & Payable')

   
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Dash Board}
    tab1.grid_columnconfigure(0,weight=1)
    tab1.grid_rowconfigure(0,weight=1)
    
    Sys_mains_frame=Frame(tab1,bg="#2f516f",)
    Sys_mains_frame.grid(row=0,column=0,sticky='nsew')

    
    
    def responsive_wid(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
      
        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/13
        y2 = dheight/6

        dcanvas.coords("bg_polygen_dash",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )                    

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/3.1
        y1 = dheight/5
        y2 = dheight/1.1

        dcanvas.coords("bg_polygen_dash1",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        r1 = 25
        x1 = dwidth/2.95
        x2 = dwidth/1.529
        y1 = dheight/5
        y2 = dheight/1.1

        dcanvas.coords("bg_polygen_dash2",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        r1 = 25
        x1 = dwidth/1.49
        x2 = dwidth/1.021
        y1 = dheight/5
        y2 = dheight/1.1

        dcanvas.coords("bg_polygen_dash3",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/3.1
        y1 = dheight/1.06
        y2 = dheight/.59
        
        #-----------------------------------------second row
        dcanvas.coords("bg_polygen_dash4",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        r1 = 25
        x1 = dwidth/2.95
        x2 = dwidth/1.529
        y1 = dheight/1.06
        y2 = dheight/.59

        dcanvas.coords("bg_polygen_dash5",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        r1 = 25
        x1 = dwidth/1.49
        x2 = dwidth/1.021
        y1 = dheight/1.06
        y2 = dheight/.59

        dcanvas.coords("bg_polygen_dash6",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        dcanvas.coords("head_lb",dwidth/2,dheight/8.4)
        dcanvas.coords("prf_lb",dwidth/53,dheight/4.7)
        
        dcanvas.coords("prf_hr",dwidth/53,dheight/3.7,dwidth/3.15,dheight/3.7)
        dcanvas.coords("net_prf",dwidth/53,dheight/3.2)
        dcanvas.coords("graph",dwidth/53,dheight/2.2)
        #--------------------------------------------------------------second
        dcanvas.coords("exp_hd_lb",dwidth/2.9,dheight/4.7)
        dcanvas.coords("exp_hr",dwidth/2.9,dheight/3.7,dwidth/1.54,dheight/3.7)
        dcanvas.coords("graph_2",dwidth/2.9,dheight/2.2)
        
        #-----------------------------------------------------------third
        dcanvas.coords("bnk_lb",dwidth/1.48,dheight/4.7)
        dcanvas.coords("bank_hr",dwidth/1.48,dheight/3.7,dwidth/1.03,dheight/3.7)
        #--------------------------------------------------------------forth
        dcanvas.coords("incom_lb",dwidth/53,dheight/1.04)
        
        dcanvas.coords("incom_hr",dwidth/53,dheight/0.99,dwidth/3.15,dheight/0.99)

     
        dcanvas.coords("graph_4",dwidth/53,dheight/0.85)
   
        #-------------------------------------------------------------fifth
        dcanvas.coords("inv_lb",dwidth/2.9,dheight/1.04)
        dcanvas.coords("invs_hr",dwidth/2.9,dheight/0.99,dwidth/1.54,dheight/0.99)
        dcanvas.coords("inv_lb2",dwidth/2.9,dheight/0.95)
        dcanvas.coords("inv_lb3",dwidth/2.9,dheight/0.90)
        dcanvas.coords("graph_5",dwidth/2.9,dheight/0.85)
        #-------------------------------------------------------------sixth
        dcanvas.coords("sales_lb",dwidth/1.48,dheight/1.04)
        dcanvas.coords("sales_hr",dwidth/1.48,dheight/0.99,dwidth/1.03,dheight/0.99)
        
        


        dcanvas.coords("grapg_6",dwidth/1.48,dheight/0.85)
        

        
    Sys_mains_frame.grid_rowconfigure(0,weight=1)
    Sys_mains_frame.grid_columnconfigure(0,weight=1)

    canvas = Canvas(Sys_mains_frame,height=700,bg='#2f516f',scrollregion=(0,0,700,1200))
    sr_Scroll = Scrollbar(Sys_mains_frame,orient=VERTICAL)
    sr_Scroll.grid(row=0,column=1,sticky='ns')
    sr_Scroll.config(command=canvas.yview)
    canvas.bind("<Configure>", responsive_wid)
    canvas.config(yscrollcommand=sr_Scroll.set)
    canvas.grid(row=0,column=0,sticky='nsew')
    

    cmp_name=Label(canvas, text="Clown",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
  
    win_inv1 = canvas.create_window(0, 0, anchor="center", window=cmp_name,tag=("head_lb"))
    
    rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash"),smooth=True,)
    # #----------------------------------------------------------------------------------------------------------------grid 1
    rth1 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash1"),smooth=True,)

    prf_lb=Label(canvas, text="PROFIT AND LOSS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=prf_lb, tag=("prf_lb"))

    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("prf_hr") )

    net_prf=Label(canvas, text="NET INCOME: ₹ 0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=net_prf,tag=("net_prf"))

    figlast = plt.figure(figsize=(8, 4), dpi=50)

    x="Income"
    y=10 
    plt.barh(x,y, label="Undefined", color="blue") 
    plt.legend()
  
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()

    x="Expense"
    y=100
    plt.barh(x,y, color="red") 
    plt.legend()
 
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()
              

    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph"))
    # #----------------------------------------------------------------------------------------------------------------grid 2
    rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash2"),smooth=True,)

    exp_hd_lb=Label(canvas, text="EXPENSES: ₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=exp_hd_lb, tag=("exp_hd_lb"))
    canvas.create_line(0, 0, 0, 0,fill="gray" ,tag=("exp_hr"))
    fig, ax = plt.subplots(figsize=(8, 4), dpi=50)

    size = 0.3
    vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

    cmap = plt.colormaps["tab20c"]
    outer_colors = cmap(np.arange(3)*4)
    # inner_colors = cmap([1, 2, 5, 6, 9, 10])

    ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
        wedgeprops=dict(width=size, edgecolor='w'))

    # ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
    #        wedgeprops=dict(width=size, edgecolor='w'))

    ax.set(aspect="equal", title='Pie plot with `ax.pie`')

    canvasbar = FigureCanvasTkAgg(fig, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_2"))

    # #----------------------------------------------------------------------------------------------------------------grid 3
    rth3 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash3"),smooth=True,)

    bnk_lb=Label(canvas, text="BANK ACCOUNTS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=bnk_lb,tag=("bnk_lb"))
    canvas.create_line(910, 195, 1290, 195,fill="gray",tag=("bank_hr"))
    # #----------------------------------------------------------------------------------------------------------------grid 4
    rth4 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash4"),smooth=True,)

    incom_lb=Label(canvas, text="INCOME: ₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=incom_lb,tag=("incom_lb"))
    canvas.create_line(0, 0, 0, 0,fill="gray",tag=("incom_hr") )

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots(figsize=(8, 4), dpi=50)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    canvasbar = FigureCanvasTkAgg(fig1, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_4"))

    # #----------------------------------------------------------------------------------------------------------------grid 5
    rth5 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash5"),smooth=True,)
    inv_lb=Label(canvas, text="INVOICE",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb, tag=("inv_lb"))

    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("invs_hr") )
    inv_lb2=Label(canvas, text="UNPAID:₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb2, tag=("inv_lb2"))
    inv_lb3=Label(canvas, text="PAID:₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0,0 , anchor="nw", window=inv_lb3, tag=("inv_lb3"))

    figlast = plt.figure(figsize=(8, 4), dpi=50)

    x="Unpaid"
    y=10 
    plt.barh(x,y, label="Undefined", color="blue") 
    plt.legend()
  
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()

    x="Paid"
    y=100
    plt.barh(x,y, color="red") 
    plt.legend()
 
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()
              

    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(480, 780, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_5"))
    # #----------------------------------------------------------------------------------------------------------------grid 5
    

    # win_inv1 = canvas.create_window(920, 640, anchor="nw", window=grd1)
    
    # canvas.create_line(910, 675, 1290, 675,fill="gray" )
    # figlast = plt.figure(figsize=(8, 4), dpi=50)

    # x="Income"
    # y=10 
    # plt.barh(x,y, label="Undefined", color="blue") 
    # plt.legend()
  
    # plt.ylabel("")
    # axes=plt.gca()
    # axes.xaxis.grid()

    # canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
    # canvasbar
    # canvasbar.draw()
    # canvasbar.get_tk_widget()
    # win_inv1 = canvas.create_window(900, 780, anchor="nw", window=canvasbar.get_tk_widget())
    # #----------------------------------------------------------------------------------------------------------------grid 6
    rth6 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash6"),smooth=True,)
    sales_lb=Label(canvas, text="SALES $0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=sales_lb, tag=("sales_lb"))

    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("sales_hr") )
    
    
    fig, ax = plt.subplots(figsize=(8, 4), dpi=50)
    ax.plot(range(10))
    ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
   

    canvasbar = FigureCanvasTkAgg(fig, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("grapg_6"))
    
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Banking Section(Tab2)

    tab_bank = ttk.Notebook(tab2)
    tab2_1 =  ttk.Frame(tab_bank)
    tab2_2=  ttk.Frame(tab_bank)
    tab2_3 = ttk.Frame(tab_bank)

    tab_bank.add(tab2_1,compound = LEFT, text ='Online Banking')
    tab_bank.add(tab2_2,compound = LEFT, text ='Offline banking')
    tab_bank.add(tab2_3,compound = LEFT, text ='Bank Reconvilation')

    
    tab_bank.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Sales Tab}
    tab_sales = ttk.Notebook(tab3)
    tab3_1 =  ttk.Frame(tab_sales)
    tab3_2=  ttk.Frame(tab_sales)
    tab3_3 = ttk.Frame(tab_sales)
    tab3_4=  ttk.Frame(tab_sales)

    
        
    tab_sales.add(tab3_1,compound = LEFT, text ='Sales Records')
    tab_sales.add(tab3_2,compound = LEFT, text ='Invoices')
    tab_sales.add(tab3_3,compound = LEFT, text ='Customers')
    tab_sales.add(tab3_4,compound = LEFT, text ='Product & Services')
 
    tab_sales.pack(expand = 1, fill ="both")

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Expenses Tab}
    tab_exp = ttk.Notebook(tab4)
    tab4_1 =  ttk.Frame(tab_exp)
    tab4_2=  ttk.Frame(tab_exp)
    tab_exp.add(tab4_1,compound = LEFT, text ='Expenses')
    tab_exp.add(tab4_2,compound = LEFT, text ='Supliers')
    tab_exp.pack(expand = 1, fill ="both")
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333{Pay Roll Tab}
    tab_payroll = ttk.Notebook(tab5)
    tab5_1 =  ttk.Frame(tab_payroll)
    tab5_2=  ttk.Frame(tab_payroll)
     
    tab_payroll.add(tab5_1,compound = LEFT, text ='Employee')
    tab_payroll.add(tab5_2,compound = LEFT, text ='Payslip')

    tab_payroll.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Report Tab}

    tab_report = ttk.Notebook(tab6)
    tab6_1 =  ttk.Frame(tab_report)
    tab6_2=  ttk.Frame(tab_report)
    tab6_3 = ttk.Frame(tab_report)
    tab6_4=  ttk.Frame(tab_report)

    
        
    tab_report.add(tab6_1,compound = LEFT, text ='Profit & Loss')
    tab_report.add(tab6_2,compound = LEFT, text ='Balance Sheet')
    tab_report.add(tab6_3,compound = LEFT, text ='Accounts Receivables')
    tab_report.add(tab6_4,compound = LEFT, text ='Accounts Payables')
 
    tab_report.pack(expand = 1, fill ="both")

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Taxes}

    tab_tax = ttk.Notebook(tab7)
    tab7_1 =  ttk.Frame(tab_tax)
    tab7_2=  ttk.Frame(tab_tax)

    tab_tax.add(tab7_1,compound = LEFT, text ='GST')
    tab_tax.add(tab7_2,compound = LEFT, text ='New')

    tab_tax.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Accounting}
    tab_account = ttk.Notebook(tab8)
    tab8_1 =  ttk.Frame(tab_account)
    tab8_2=  ttk.Frame(tab_account)

    tab_account.add(tab8_1,compound = LEFT, text ='Chart Of Accounts')
    tab_account.add(tab8_2,compound = LEFT, text ='Reconcile')
   
 
    tab_account.pack(expand = 1, fill ="both")
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Cash Management}
    tab_cash = ttk.Notebook(tab10)
    
    tab10_1 =  ttk.Frame(tab_cash)
    tab10_2=  ttk.Frame(tab_cash)
    tab10_3 = ttk.Frame(tab_cash)

    tab_cash.add(tab10_1,compound = LEFT, text ='Cash Position')
    tab_cash.add(tab10_2,compound = LEFT, text ='Cash Flow Analyzer')
    tab_cash.add(tab10_3,compound = LEFT, text ='Check Cash Flow')

    tab_cash.pack(expand = 1, fill ="both")
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{My Account}
    Sys_mains_frame=Frame(tab9, height=750,bg="#2f516f")
    Sys_mains_frame.pack(fill=X)

#---------------------------------------------------------------------------------------------------------------Company Second Portion
def cmpny_crt2():
    main_frame_cmpny.pack_forget()
    global main_frame_cmpny2
    main_frame_cmpny2=Frame(root, height=750,bg="#213b52")
    main_frame_cmpny2.pack(fill=X,)

    cmpny_dt_frm2=Frame(main_frame_cmpny2, height=650, width=500,bg="white")
    cmpny_dt_frm2.pack(pady=105)

    def responsive_wid_cmp2(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("cmpny_hd1",dwidth/40,dheight/15)
        dcanvas.coords("nm_nm2",dwidth/6,dheight/5)
        dcanvas.coords("cmpny_cntry",dwidth/6,dheight/3.2)
        dcanvas.coords("cmpny_cntry2",dwidth/6,dheight/2.35)
        dcanvas.coords("r1",dwidth/2.2,dheight/1.8)
        dcanvas.coords("r2",dwidth/2.2,dheight/1.6)
        dcanvas.coords("cmpny_cntry3",dwidth/6,dheight/1.38)
        dcanvas.coords("button_cmp2",dwidth/4.3,dheight/1.2)
        dcanvas.coords("button_cmp3",dwidth/1.9,dheight/1.2)

        dcanvas.coords("cmp_lbl1",dwidth/6,dheight/3.8)
        dcanvas.coords("cmp_lbl2",dwidth/6,dheight/2.7)
        dcanvas.coords("cmp_lbl3",dwidth/6,dheight/2)
        dcanvas.coords("cmp_lbl4",dwidth/6,dheight/1.46)
        

    lf_cmpy2= Canvas(cmpny_dt_frm2,height=650, width=500)
    lf_cmpy2.bind("<Configure>", responsive_wid_cmp2)
    lf_cmpy2.pack(fill=X)

    def name_ent2(event):
        if nm_nm2.get()=="Legal Business Name":
            nm_nm2.delete(0,END)
        else:
            pass


    cmpny_hd1=Label(lf_cmpy2, text="Let's Start Building Your FinsYs",font=('Calibri 28 bold'), fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_hd1, tag=("cmpny_hd1"))

    

    nm_nm2 = Entry(cmpny_dt_frm2, width=30, font=('Calibri 16'),borderwidth=2)
    nm_nm2.insert(0,"Legal Business Name")
    nm_nm2.bind("<Button-1>",name_ent2)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=nm_nm2, tag=("nm_nm2"))

    cmp_lbl1=Label(cmpny_dt_frm2, text="Your Industry",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl1, tag=("cmp_lbl1"))

    invset_bg_var = StringVar()
    cmpny_cntry = ttk.Combobox(cmpny_dt_frm2,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Accounting Services','Consultants, doctors, Lawyers and similar','Information Tecnology','Manufacturing','Professional, Scientific and Technical Services','Restaurant/Bar and similar','Retail and Smilar','Other Finanacial Services')
    cmpny_cntry.current(0)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry, tag=("cmpny_cntry"))

    cmp_lbl2=Label(cmpny_dt_frm2, text="Company type",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl2, tag=("cmp_lbl2"))

    invset_bg_var = StringVar()
    cmpny_cntry2 = ttk.Combobox(cmpny_dt_frm2,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Private Limited Company','Public Limited Company','Joint-Venture Company','Partnership Firm Company','One Person Company','Branch Office Company','Non Government Organization')
    cmpny_cntry.current(0)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry2, tag=("cmpny_cntry2"))
    
    cmp_lbl3=Label(cmpny_dt_frm2, text="Do you have an Accountant, Bookkeeper or Tax Pro ?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl3, tag=("cmp_lbl3"))

    bs_cus_ct=StringVar()
    r1=Radiobutton(cmpny_dt_frm2, text = "Yes", variable = bs_cus_ct, value ="Yes",font=('Calibri 16'))
    r1.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r1, tag=("r1"))

    r2=Radiobutton(cmpny_dt_frm2, text = "No", variable = bs_cus_ct, value ="No",font=('Calibri 16'))
    r2.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r2, tag=("r2"))


    cmp_lbl4=Label(cmpny_dt_frm2, text="How do you like to get paid?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl4, tag=("cmp_lbl4"))
    
    invset_bg_var = StringVar()
    cmpny_cntry3 = ttk.Combobox(cmpny_dt_frm2,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Cash','Cheque','Credit card/Debit card','Bank Transfer','Paypal/Other service')
    cmpny_cntry.current(0)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry3, tag=("cmpny_cntry3"))

    button_cmp2 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=cmpny_crt1,text="Previous",bg="#213b52")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp2, tag=("button_cmp2"))
    button_cmp3 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=fun_sign_in,text="Submit",bg="#213b52")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp3, tag=("button_cmp3"))
#-------------------------------------------------------------------------------------------------------------------company creation
def cmpny_crt1():
    try:
        main_frame_cmpny2.pack_forget()
    except:
        pass
    try:
        main_frame_signup.pack_forget()
    except:
        pass
    global main_frame_cmpny
    main_frame_cmpny=Frame(root, height=750,bg="#213b52")
    main_frame_cmpny.pack(fill=X,)

    cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
    cmpny_dt_frm.pack(pady=50)

    def name_ent(event):
        if nm_nm.get()=="Company Name":
            nm_nm.delete(0,END)
        else:
            pass

    def cmp_add(event):
        if cmp_cmpn.get()=="Company Address":
                cmp_cmpn.delete(0,END)
        else:
            pass
    def cty_ent(event):
        if cmp_cty.get()=="City":
            cmp_cty.delete(0,END)
        else:
            pass

    def em_ent(event):
        if cmp_email.get()=="Email":
                cmp_email.delete(0,END)
        else:
            pass
    def ph_ent(event):
        if cmp_ph.get()=="Phone Number":
            cmp_ph.delete(0,END)
        else:
            pass

    def fil_ent(event):
        
        cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
        
        cmp_files.delete(0,END)
        cmp_files.insert(0,cmp_logo)
    
    def responsive_wid_cmp1(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("cmpny_hd",dwidth/2,dheight/13)
        dcanvas.coords("nm_nm",dwidth/2,dheight/5)
        dcanvas.coords("cmp_cmpn",dwidth/2,dheight/3.5)
        dcanvas.coords("cmp_cty",dwidth/2,dheight/2.7)
        dcanvas.coords("cmpny_cntry",dwidth/2,dheight/2.2)
        dcanvas.coords("cmp_pin",dwidth/2,dheight/1.85)
        dcanvas.coords("cmp_email",dwidth/2,dheight/1.6)
        dcanvas.coords("cmp_ph",dwidth/2,dheight/1.4)
        dcanvas.coords("cmp_files",dwidth/2,dheight/1.25)
        dcanvas.coords("button_cmp",dwidth/2,dheight/1.1)


    lf_cmpy1= Canvas(cmpny_dt_frm,height=650, width=500)
    lf_cmpy1.bind("<Configure>", responsive_wid_cmp1)
    lf_cmpy1.pack(fill=X)

    cmpny_hd=Label(lf_cmpy1, text="We're Happy you're Here!",font=('Calibri 30 bold'), fg="black")
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_hd, tag=("cmpny_hd"))


    nm_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
    nm_nm.insert(0,"Company Name")
    nm_nm.bind("<Button-1>",name_ent)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=nm_nm, tag=("nm_nm"))

    cmp_cmpn = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_cmpn.insert(0,"Company Address")
    cmp_cmpn.bind("<Button-1>",cmp_add)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cmpn, tag=("cmp_cmpn"))

    cmp_cty = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_cty.insert(0,"City")
    cmp_cty.bind("<Button-1>",cty_ent)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cty, tag=("cmp_cty"))

    invset_bg_var = StringVar()
    cmpny_cntry = ttk.Combobox(lf_cmpy1,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_cntry, tag=("cmpny_cntry"))
    cmpny_cntry['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
    cmpny_cntry.current(0)

    cmp_pin = Spinbox(lf_cmpy1,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
    cmp_pin.delete(0,END)
    cmp_pin.insert(0,"Pincode")
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_pin, tag=("cmp_pin"))
   

    cmp_email = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_email.insert(0,"Email")
    cmp_email.bind("<Button-1>",em_ent)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_email, tag=("cmp_email"))

    cmp_ph = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_ph.insert(0,"Phone Number")
    cmp_ph.bind("<Button-1>",ph_ent)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_ph, tag=("cmp_ph"))

    cmp_files = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_files.insert(0,"No file Chosen")
    cmp_files.bind("<Button-1>",fil_ent)
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_files, tag=("cmp_files"))

    button_cmp = customtkinter.CTkButton(master=lf_cmpy1,command=cmpny_crt2,text="Next",bg="#213b52")
    win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_cmp"))
    
#--------------------------------------------------------------------------------------------------------Sign in frame in signup section
def fun_sign_in():
    print("haii")
    try:
        main_frame_signup.pack_forget()
    except:
        pass
    try:
        main_frame_cmpny2.pack_forget()
    except:
        pass

    main_frame_signin.pack(fill=X,)
    


#---------------------------------------------------------------------------------------------------------------------Sign Up Section
def func_sign_up():
    
    global main_frame_signup
    main_frame_signin.pack_forget()

    main_frame_signup=Frame(root, height=750)
    main_frame_signup.pack(fill=X,)

    def responsive_wid_signup(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("round_signup",dwidth/2,-dheight/.5,dwidth/.7,dheight/.5)
        dcanvas.coords("sign_in_lb",dwidth/6,dheight/12)
        dcanvas.coords("fst_nm",dwidth/8.5,dheight/5)
        dcanvas.coords("lst_nm",dwidth/8.5,dheight/3.5)
        dcanvas.coords("sys_em",dwidth/8.5,dheight/2.7)
        dcanvas.coords("sys_usr",dwidth/8.5,dheight/2.2)
        dcanvas.coords("sys_pass",dwidth/8.5,dheight/1.85)
        dcanvas.coords("sys_cf",dwidth/8.5,dheight/1.6)
        dcanvas.coords("button_sign",dwidth/6,dheight/1.4)
        dcanvas.coords("lft_lab",dwidth/1.4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/1.52,dheight/10)
        dcanvas.coords("btn_signup2",dwidth/1.36,dheight/6.6)
        dcanvas.coords("label_img",dwidth/1.8,dheight/5)
        
        


    lf_signup= Canvas(main_frame_signup,width=1500, height=1500)
    lf_signup.bind("<Configure>", responsive_wid_signup)
    lf_signup.pack(fill=X)

    lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_signup"))

    # #--------------------------------------------------------------------------------sign up section
    sign_in_lb=Label(lf_signup, text="Sign Up",font=('Calibri 30 bold'), fg="black")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_in_lb, tag=("sign_in_lb"))

    def nme(event):
        if fst_nm.get()=="Firstname":
            fst_nm.delete(0,END)
        else:
            pass

    def nme1(event):
        if lst_nm.get()=="Lastname":
            lst_nm.delete(0,END)
        else:
            pass
        
    def nme2(event):
        if sys_em.get()=="Email":
            sys_em.delete(0,END)
        else:
            pass
        
        
    def nme3(event):
        if sys_usr.get()=="Username":
            sys_usr.delete(0,END)
        else:
            pass
        
    def nme4(event):
        if sys_pass.get()=="Password":
            sys_pass.delete(0,END)
        else:
            pass
    
    def nme5(event):
        if sys_cf.get()=="Confirm Password":
            sys_cf.delete(0,END)
        else:
            pass
    
    

    fst_nm = Entry(lf_signup, width=25, font=('Calibri 16'))
    fst_nm.insert(0,"Firstname")
    fst_nm.bind("<Button-1>",nme)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=fst_nm, tag=("fst_nm"))

    lst_nm = Entry(lf_signup,  width=25, font=('Calibri 16'))
    lst_nm.insert(0,"Lastname")
    lst_nm.bind("<Button-1>",nme1)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lst_nm, tag=("lst_nm"))

    sys_em = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_em.insert(0,"Email")
    sys_em.bind("<Button-1>",nme2)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_em, tag=("sys_em"))

    sys_usr = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_usr.insert(0,"Username")
    sys_usr.bind("<Button-1>",nme3)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_usr, tag=("sys_usr"))

    sys_pass = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_pass.insert(0,"Password")
    sys_pass.bind("<Button-1>",nme4)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_pass, tag=("sys_pass"))

    sys_cf = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_cf.insert(0,"Confirm Password")
    sys_cf.bind("<Button-1>",nme5)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_cf, tag=("sys_cf"))

    button_sign = customtkinter.CTkButton(master=lf_signup, command=cmpny_crt1,text="Sign Up",bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button_sign, tag=("button_sign"))

    label_img = Label(lf_signup, image = sign_up,bg="#213b52", width=800,anchor="w")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=label_img, tag=("label_img"))
    
    

    lft_lab=Label(lf_signup, text="One of us ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
    lft_lab2=Label(lf_signup, text="click here for work with FinsYs.",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

    btn_signup2 = Button(lf_signup, text='Sign In', command=fun_sign_in, bg="white", fg="black",borderwidth = 3,height=1,width=10)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn_signup2, tag=("btn_signup2"))


main_frame_signin=Frame(root, height=750)
main_frame_signin.pack(fill=X,)
# main_frame_signin=Frame(root)
# main_frame_signin.grid(row=0,column=0,sticky='nsew')
# main_frame_signin.grid_rowconfigure(0,weight=1)
# main_frame_signin.grid_columnconfigure(0,weight=1)



def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

def sig_pass(event):
        if pass_ent.get()=="Password":
            pass_ent.delete(0,END)
        else:
            pass


def responsive_wid_login(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("sign_inlb",dwidth/1.4,dheight/4)

        dcanvas.coords("nm_ent",dwidth/1.5,dheight/2.7)
        dcanvas.coords("pass_ent",dwidth/1.5,dheight/2.2)
        dcanvas.coords("button",dwidth/1.4,dheight/1.8)
        dcanvas.coords("round_login",-dwidth/2,-dheight/.5,dwidth/2,dheight/.5)
        dcanvas.coords("lft_lab",dwidth/4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/6,dheight/10)
        dcanvas.coords("btn2",dwidth/3.7,dheight/6.6)
        dcanvas.coords("img",dwidth/16,dheight/5.5)
    

lf_signup= Canvas(main_frame_signin,width=1366,height=750)
lf_signup.bind("<Configure>", responsive_wid_login)
lf_signup.pack(fill=X)

sign_inlb=Label(lf_signup, text="Sign In",font=('Calibri 30 bold'), fg="black")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_inlb, tag=("sign_inlb"))

nm_ent = Entry(lf_signup, width=25, font=('Calibri 16'))
nm_ent.insert(0,"Username")
nm_ent.bind("<Button-1>",sig_nm)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=nm_ent, tag=("nm_ent"))

pass_ent = Entry(lf_signup, width=25, font=('Calibri 16'))
pass_ent.insert(0,"Password")
pass_ent.bind("<Button-1>",sig_pass)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=pass_ent, tag=("pass_ent"))

button = customtkinter.CTkButton(master=main_frame_signin,command=main_sign_in,text="Log In",bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button, tag=("button"))

# #------------------------------------------------------------------------------------------------------------------------left canvas

lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_login"))

img = Label(lf_signup, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=img, tag=("img"))

lft_lab=Label(lf_signup, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
lft_lab2=Label(lf_signup, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

btn2 = Button(main_frame_signin, text = 'Sign Up', command = func_sign_up, bg="white", fg="black",borderwidth = 3,height=1,width=10)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn2, tag=("btn2"))

root.mainloop()