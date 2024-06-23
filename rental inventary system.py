from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime
import sqlite3


class rental_inventory:
    def __init__(self,root):
        self.root=root
        self.root.title("Rental Inventory System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background="skyblue")


        #===============================frame=========================================

        mainframe=Frame(self.root, bd=20, width=1350, height=700, bg="light green", relief=RIDGE)
        mainframe.grid()


        leftframe=Frame(mainframe, bd=10, width=750, height=600, bg="lightgreen", relief=RIDGE)
        leftframe.pack(side=LEFT)

        rightframe=Frame(mainframe,bd=10,width=560,height=600,bg="lightgreen",relief=RIDGE)
        rightframe.pack(side=RIGHT)


        #==============================div_frame====================================

        leftframe0=Frame(leftframe, bd=9, width=712, height=143, padx=5, bg="skyblue", relief=RIDGE)
        leftframe0.grid(row=0,column=0)
        leftframe1=Frame(leftframe, bd=5, width=712, height=170,padx=5, bg="skyblue", relief=RIDGE)
        leftframe1.grid(row=1,column=0)
        leftframe2=Frame(leftframe, bd=5, width=712, height=168,padx=5, bg="skyblue", relief=RIDGE)
        leftframe2.grid(row=2,column=0)
        leftframe3=Frame(leftframe, bd=5, width=712, height=95,padx=5, bg="skyblue", relief=RIDGE)
        leftframe3.grid(row=3,column=0)

        rightframe0=Frame(rightframe, bd=5, width=522, height=200,padx=5, bg="skyblue", relief=RIDGE)
        rightframe0.grid(row=0,column=0,sticky=W)
        rightframe1=Frame(rightframe, bd=5, width=522, height=280,padx=5, bg="skyblue", relief=RIDGE)
        rightframe1.grid(row=1,column=0,sticky=W)
        rightframe2=Frame(rightframe, bd=5, width=522, height=95,padx=5, bg="skyblue", relief=RIDGE)
        rightframe2.grid(row=2,column=0,sticky=W)

        #=========================variables==================================

        fullname=StringVar()
        acctopen=StringVar()
        appdate=StringVar()
        nextcreditreview=StringVar()
        lastcreditreview=StringVar()
        daterev=StringVar()
        prodcode=StringVar()
        prodtype=StringVar()
        nodays=StringVar()
        costpday=StringVar()
        crelimit=StringVar()
        crecheck=StringVar()
        settdueday=StringVar()
        paymentd=StringVar()
        discount=StringVar()
        deposit=StringVar()
        paydueday=StringVar()
        paymentm=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        tax=StringVar()
        subtotal=StringVar()
        total=StringVar()
        receipt_ref=StringVar()



        def database():
            tax1=tax.get()
            subtotal1=subtotal.get()
            total1=total.get()
            name1=fullname.get()
            prod=prodtype.get()
            conn=sqlite3.connect('amount.db')
            with conn:
                cursor=conn.cursor()
            
            cursor.execute('create table if not exists rental(fullname text,prodtype text,tax text,subtotal text,total text)')
            cursor.execute('insert into rental(fullname,prodtype,tax,subtotal,total) values(?,?,?,?,?)',(name1,prod,tax1,subtotal1,total1))
            conn.commit()

            

        def iexit():
            iexit = tkinter.messagebox.askyesno("Inventory Rental System","confirm if you want to exit")
            if iexit > 0:
                root.destroy()
                return

        def Reset():
            self.txtinfo0.delete("1.0",END)
            self.txtinfo1.delete("1.0",END)
            self.txtinfo2.delete("1.0",END)
            self.txtinfo3.delete("1.0",END)
            self.txtreceipt.delete("1.0",END)

            acctopen.set("")
            appdate.set("")
            nextcreditreview.set("")
            lastcreditreview.set("")
            daterev.set("")
            prodcode.set("")
            prodtype.set("")
            nodays.set("")
            costpday.set("")
            crelimit.set("")
            crecheck.set("")
            settdueday.set("")
            paymentd.set("")
            discount.set("")
            deposit.set("")
            paydueday.set("")
            paymentm.set("")
            fullname.set("")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            tax.set("")
            subtotal.set("")
            total.set("")
            return

        def checkcredit():
            if (var1.get()==1):
                self.txtinfo0.insert(END,"Customer's Check Credit Approved")
            elif (var1.get()==0):
                self.txtinfo0.delete('1.0',END)

        def termagreed():
            if (var2.get()==1):
                self.txtinfo1.insert(END,"Term Agreed")
            elif (var2.get()==0):
                self.txtinfo1.delete('1.0',END)

        def acctonhold():
            if (var3.get()==1):
                self.txtinfo2.insert(END,"Account On Hold")
            elif (var3.get()==0):
                self.txtinfo2.delete('1.0',END)

        def restrictedmails():
            if (var4.get()==1):
                self.txtinfo3.insert(END,"Restricted Mail For Customer")
            elif (var4.get()==0):
                self.txtinfo3.delete('1.0',END)

        def Product(evt):
            values=str(self.cboprodtype.get())
            pType=values
            if pType=='Car':
                prodcode.set('CAR452')
                costpday.set('Rs50')
                crecheck.set('No')
                settdueday.set('50')
                paymentd.set('No')
                deposit.set('No')
                paymentm.set('master card')

                n=float(lastcreditreview.get())
                s=float(settdueday.get())
                price=(n*s)
                tc='Rs',str('%.2f'%(price))
                paydueday.set(tc)

            elif pType=='Van':
                    prodcode.set('VAN775')
                    costpday.set('Rs35')
                    crecheck.set('No')
                    settdueday.set('35')
                    paymentd.set('No')
                    deposit.set('No')
                    paymentm.set('cash')

                    n=float(lastcreditreview.get())
                    s=float(settdueday.get())
                    price=(n*s)
                    tc='Rs',str('%.2f'%(price))
                    paydueday.set(tc)

            elif pType=='Bike':
                  prodcode.set('BIKE007')
                  costpday.set('Rs20')
                  crecheck.set('No')
                  settdueday.set('20')
                  paymentd.set('No')
                  deposit.set('No')
                  paydueday.set('20')
                  paymentm.set('cash')

                  n=float(lastcreditreview.get())
                  s=float(settdueday.get())
                  price=(n*s)
                  tc='Rs',str('%.2f'%(price))
                  paydueday.set(tc)

            elif pType=='Truck':
                    prodcode.set('TRK7483')
                    costpday.set('Rs75')
                    crecheck.set('No')
                    settdueday.set('75')
                    paymentd.set('No')
                    deposit.set('No')
                    paydueday.set('75')
                    paymentm.set('visa card')

                    n=float(lastcreditreview.get())
                    s=float(settdueday.get())
                    price=(n*s)
                    tc='Rs',str('%.2f'%(price))
                    paydueday.set(tc)

        def idates(evt):
            values=str(self.cbonodays.get())
            ndays=values
            if ndays=='1-30':
                d1=datetime.date.today()
                d2=datetime.timedelta(days=30)
                d3=(d1+d2)
                appdate.set(d1)
                nextcreditreview.set(d3)
                lastcreditreview.set(30)
                daterev.set(d3)

                crelimit.set('Rs500')
                discount.set('0.05')
                acctopen.set('Yes')

            elif ndays=='1-90':
                d1=datetime.date.today()
                d2=datetime.timedelta(days=90)
                d3=(d1+d2)
                appdate.set(d1)
                nextcreditreview.set(d3)
                lastcreditreview.set(90)
                daterev.set(d3)

                crelimit.set('Rs750')
                discount.set('0.10')
                acctopen.set('Yes')

            elif ndays=='1-270':
                d1=datetime.date.today()
                d2=datetime.timedelta(days=270)
                d3=(d1+d2)
                appdate.set(d1)
                nextcreditreview.set(d3)
                lastcreditreview.set(270)
                daterev.set(d3)

                crelimit.set('Rs875')
                discount.set('0.15')
                acctopen.set('Yes')

            elif ndays=='1-365':
                d1=datetime.date.today()
                d2=datetime.timedelta(days=365)
                d3=(d1+d2)
                appdate.set(d1)
                nextcreditreview.set(d3)
                lastcreditreview.set(365)
                daterev.set(d3)

                crelimit.set('Rs1000')
                discount.set('0.20')
                acctopen.set('Yes')

            elif (ndays=='0'):
                messagebox.showinfo('zero selected','you choose zero?')
                Reset()

        def totalcost():
            n=float(lastcreditreview.get())
            s=float(settdueday.get())
            price=(n*s)
            da=price-(price*float(discount.get()))
            st='Rs',str('%.2f'%(da))
            itax='Rs',str('%.2f'%((price)*0.18))
            tax.set(itax)
            subtotal.set(st)
            tc='Rs',str('%.2f'%(((price)*0.18)+da))
            total.set(tc)


            self.txtreceipt.delete('1.0',END)
            x=random.randint(10908,500876)
            randomref=str(x)
            receipt_ref.set('BILL'+randomref)


            self.txtreceipt.insert(END,'Receipt Ref:\t\t\t\t'+receipt_ref.get()+'\t\t\t'+appdate.get()+'\n')
            self.txtreceipt.insert(END,'Product Type\t\t\t\t'+prodtype.get()+'\n')
            self.txtreceipt.insert(END,'Product Code:\t\t\t\t'+prodcode.get()+'\n')
            self.txtreceipt.insert(END,'No Of Days:\t\t\t\t'+nodays.get()+'\n')
            self.txtreceipt.insert(END,'Account Open:\t\t\t\t'+acctopen.get()+'\n')
            self.txtreceipt.insert(END,'Next Credit Review\t\t\t\t'+nextcreditreview.get()+'\n')
            self.txtreceipt.insert(END,'Last Credit Review:\t\t\t\t'+lastcreditreview.get()+'\n')
            self.txtreceipt.insert(END,'\nTAX:\t\t\t\t'+tax.get()+'\n')
            self.txtreceipt.insert(END,'\nSubtotal:\t\t\t\t'+str(subtotal.get())+'\n')
            self.txtreceipt.insert(END,'\nTotal Cost:\t\t\t\t'+str(total.get()))

        #==============================rightframe0============================

        self.lblacctopen=Label(rightframe0,font=('arial',18,'bold'),text='ACCOUNT OPENED:',padx=2,pady=6,bg='skyblue')
        self.lblacctopen.grid(row=0,column=0,sticky=W)

        self.cboacctopen=ttk.Combobox(rightframe0,textvariable=acctopen,state='readonly',
                                      font=('arial',18,'bold'),width=19)
        self.cboacctopen['value']=('','select an option','Yes','No')
        self.cboacctopen.current(0)
        self.cboacctopen.grid(row=0,column=1,pady=6)
        
        self.lblappdate=Label(rightframe0,font=('arial',18,'bold'),text='APPLICATION DATE:',padx=2,pady=6,bg='skyblue')
        self.lblappdate.grid(row=1,column=0,sticky=W)

        self.cboappdate=ttk.Combobox(rightframe0,textvariable=appdate,state='readonly',
                                      font=('arial',18,'bold'),width=19)
        self.cboappdate['value']=('','select an option','Yes','No')
        self.cboappdate.current(0)
        self.cboappdate.grid(row=1,column=1,pady=6)

        self.lblncrer=Label(rightframe0,font=('arial',18,'bold'),text='NEXT CREDIT REVIEW:',padx=2,pady=6,bg='skyblue')
        self.lblncrer.grid(row=2,column=0,sticky=W)

        self.cboncrer=ttk.Combobox(rightframe0,textvariable=nextcreditreview,state='readonly',
                                      font=('arial',18,'bold'),width=19)
        self.cboncrer['value']=('','select an option','Yes','No')
        self.cboncrer.current(0)
        self.cboncrer.grid(row=2,column=1,pady=6)

        self.lbllcrer=Label(rightframe0,font=('arial',18,'bold'),text='LAST CREDIT REVIEW:',padx=2,pady=6,bg='skyblue')
        self.lbllcrer.grid(row=3,column=0,sticky=W)

        self.cbolcrer=ttk.Combobox(rightframe0,textvariable=lastcreditreview,state='readonly',
                                      font=('arial',18,'bold'),width=19)
        self.cbolcrer['value']=('','select an option','Yes','No')
        self.cbolcrer.current(0)
        self.cbolcrer.grid(row=3,column=1,pady=6)

        self.lbldaterev=Label(rightframe0,font=('arial',18,'bold'),text='DATE REVIEW:',padx=2,pady=6,bg='skyblue')
        self.lbldaterev.grid(row=4,column=0,sticky=W)

        self.cbodaterev=ttk.Combobox(rightframe0,textvariable=daterev,state='readonly',
                                      font=('arial',18,'bold'),width=19)
        self.cbodaterev['value']=('','select an option','Yes','No')
        self.cbodaterev.current(0)
        self.cbodaterev.grid(row=4,column=1,pady=6)

        #================================rightframe1===============================
        self.txtreceipt=Text(rightframe1,pady=6,height=14,width=71,font=('arial',10,'bold'))
        self.txtreceipt.grid(row=0,column=0,pady=6)
        
        #================================rightframe2===============================
        self.lbltax=Label(rightframe2,font=('arial',18,'bold'),text="TAX",padx=4,pady=1,fg='black',bg='skyblue')
        self.lbltax.grid(row=0,column=0,sticky=W)
        self.txttax=Entry(rightframe2,textvariable=tax,font=('arial',17,'bold'),bd=8,
                          fg='black',width=30,justify=LEFT).grid(row=0,column=1,pady=1,padx=4)

        self.lblsubtotal=Label(rightframe2,font=('arial',18,'bold'),text="SUB TOTAL",padx=4,pady=1,fg='black',bg='skyblue')
        self.lblsubtotal.grid(row=1,column=0,sticky=W)
        self.txtsubtotal=Entry(rightframe2,textvariable=subtotal,font=('arial',17,'bold'),bd=8,
                          fg='black',width=30,justify=LEFT).grid(row=1,column=1,pady=1,padx=4)

        self.lbltotal=Label(rightframe2,font=('arial',18,'bold'),text="TOTAL",padx=4,pady=1,fg='black',bg='skyblue')
        self.lbltotal.grid(row=2,column=0,sticky=W)
        self.txtsubtotal=Entry(rightframe2,textvariable=total,font=('arial',17,'bold'),bd=8,
                          fg='black',width=30,justify=LEFT).grid(row=2,column=1,pady=1,padx=4)
        
        #================================leftframe0========================================
        self.lblprodtype=Label(leftframe0,font=('arial',18,'bold'),text='PRODUCT TYPE:',padx=2,pady=16,bg='skyblue')
        self.lblprodtype.grid(row=0,column=0,sticky=W)

        self.cboprodtype=ttk.Combobox(leftframe0,textvariable=prodtype,state='readonly',
                                      font=('arial',18,'bold'),width=12)

        self.cboprodtype.bind('<<ComboboxSelected>>',Product)
        self.cboprodtype['value']=('','Car','Van','Bike','Truck')
        self.cboprodtype.current(0)
        self.cboprodtype.grid(row=0,column=1)

        self.lblnodays=Label(leftframe0,font=('arial',18,'bold'),text='NO OF DAYS:',padx=2,pady=2,bg='skyblue')
        self.lblnodays.grid(row=0,column=2,sticky=W)

        self.cbonodays=ttk.Combobox(leftframe0,textvariable=nodays,state='readonly',
                                      font=('arial',18,'bold'),width=12)
        self.cbonodays.bind('<<ComboboxSelected>>',idates)
        self.cbonodays['value']=('0','1-30','1-90','1-270','1-365')
        self.cbonodays.current(0)
        self.cbonodays.grid(row=0,column=3)
        
        self.lblprodcode=Label(leftframe0,font=('arial',16,'bold'),text='PRODUCT CODE:',padx=1,pady=16,bg='skyblue')
        self.lblprodcode.grid(row=1,column=0,sticky=W)

        self.txtprodcode=Entry(leftframe0,textvariable=prodcode,font=('arial',16,'bold'),bd=8,
                               fg='black',width=14,justify=LEFT).grid(row=1,column=1)

        self.lblcostpday=Label(leftframe0,font=('arial',16,'bold'),text='COST PER DAY:',padx=1,pady=2,bg='skyblue')
        self.lblcostpday.grid(row=1,column=2,sticky=W)

        self.txtcostpday=Entry(leftframe0,textvariable=costpday,font=('arial',16,'bold'),bd=8,
                               fg='black',width=14,justify=LEFT).grid(row=1,column=3)

        self.fullname=Label(leftframe0,font=('arial',16,'bold'),text='FULLNAME',padx=1,pady=16,bg='skyblue')
        self.fullname.grid(row=3,column=0,sticky=W)

        self.entryfullname=Entry(leftframe0,textvar=fullname,font=('arial',16,'bold'),bd=8,fg='black',width=14,justify=LEFT)
        self.entryfullname.grid(row=3,column=1,sticky=W)



        #================================leftframe1=========================================
        self.lblcrelimit=Label(leftframe1,font=('arial',18,'bold'),text='CREDIT LIMIT:',padx=2,pady=2,bg='skyblue')
        self.lblcrelimit.grid(row=0,column=0,sticky=W)

        self.cbocrelimit=ttk.Combobox(leftframe1,textvariable=crelimit,state='readonly',
                                      font=('arial',18,'bold'),width=12)
        self.cbocrelimit['value']=('','select an option','Rs500','Rs750','Rs875','Rs1000')
        self.cbocrelimit.current(0)
        self.cbocrelimit.grid(row=0,column=1,pady=2)

        self.lblcrecheck=Label(leftframe1,font=('arial',18,'bold'),text='CREDIT CHECK:',padx=2,pady=2,bg='skyblue')
        self.lblcrecheck.grid(row=0,column=2,sticky=W)

        self.cbocrecheck=ttk.Combobox(leftframe1,textvariable=crecheck,state='readonly',
                                      font=('arial',18,'bold'),width=10)
        self.cbocrecheck['value']=('','select an option','Yes','No')
        self.cbocrecheck.current(0)
        self.cbocrecheck.grid(row=0,column=3,pady=2)
        
        self.lblsettdueday=Label(leftframe1,font=('arial',18,'bold'),text='SET DUE DAY:',padx=2,pady=2,bg='skyblue')
        self.lblsettdueday.grid(row=1,column=0,sticky=W)

        self.txtsettdueday=Entry(leftframe1,textvariable=settdueday,font=('arial',16,'bold'),bd=2,
                               fg='black',width=14,justify=LEFT).grid(row=1,column=1)

        self.lblpaymentd=Label(leftframe1,font=('arial',18,'bold'),text='PAYMENT OVERDUE:',padx=1,pady=2,bg='skyblue')
        self.lblpaymentd.grid(row=1,column=2,sticky=W)

        self.cbopaymentd=ttk.Combobox(leftframe1,textvariable=paymentd,state='readonly',
                                      font=('arial',18,'bold'),width=10)
        self.cbopaymentd['value']=('','select an option','Yes','No')
        self.cbopaymentd.current(0)
        self.cbopaymentd.grid(row=1,column=3,pady=2)

        self.lbldiscount=Label(leftframe1,font=('arial',18,'bold'),text='DISCOUNT:',padx=1,pady=2,bg='skyblue')
        self.lbldiscount.grid(row=2,column=0,sticky=W)

        self.cbodiscount=ttk.Combobox(leftframe1,textvariable=discount,state='readonly',
                                      font=('arial',18,'bold'),width=12)
        self.cbodiscount['value']=('0','5%','10%','15%','20%')
        self.cbodiscount.current(0)
        self.cbodiscount.grid(row=2,column=1,pady=2)

        self.lbldeposit=Label(leftframe1,font=('arial',18,'bold'),text='DEPOSIT:',padx=1,pady=2,bg='skyblue')
        self.lbldeposit.grid(row=2,column=2,sticky=W)

        self.cbodeposit=ttk.Combobox(leftframe1,textvariable=deposit,state='readonly',
                                      font=('arial',18,'bold'),width=10)
        self.cbodeposit['value']=('','select an option','Yes','No')
        self.cbodeposit.current(0)
        self.cbodeposit.grid(row=2,column=3,pady=2)

        self.lblpaydueday=Label(leftframe1,font=('arial',18,'bold'),text='PAY DAY DUE:',padx=1,pady=2,bg='skyblue')
        self.lblpaydueday.grid(row=3,column=0,sticky=W)

        self.txtpaydueday=Entry(leftframe1,textvariable=paydueday,font=('arial',16,'bold'),bd=2,
                               fg='black',width=14,justify=LEFT).grid(row=3,column=1)

        self.lblpaymentm=Label(leftframe1,font=('arial',18,'bold'),text='PAYMENT METHOD:',padx=0,pady=4,bg='skyblue')
        self.lblpaymentm.grid(row=3,column=2,sticky=W)

        self.cbopaymentm=ttk.Combobox(leftframe1,textvariable=paymentm,state='readonly',
                                      font=('arial',18,'bold'),width=10)
        self.cbopaymentm['value']=('','select an option','Cash','Visa Card','Master Card')
        self.cbopaymentm.current(0)
        self.cbopaymentm.grid(row=3,column=3,pady=2)

        #================================leftframe2========================================
        
        leftframe2LL=Frame(leftframe2,bd=5,width=300,height=160,padx=5,bg="skyblue",relief=RIDGE)
        leftframe2LL.grid(row=0,column=0)
        leftframe2LR=Frame(leftframe2,bd=5,width=300,height=160,padx=5,bg='black',relief=RIDGE)
        leftframe2LR.grid(row=0,column=1)

        #====================================leftframe2LL=====================================

        self.chkcheckcredit=Checkbutton(leftframe2LL,text='CHECK CREDIT',variable=var1,onvalue=1,offvalue=0,
                                        font=('arial',19,'bold'),bg='skyblue',command=checkcredit).grid(row=0,sticky=W)

        self.chktermagreed=Checkbutton(leftframe2LL,text='TERM AGREED',variable=var2,onvalue=1,offvalue=0,
                                        font=('arial',19,'bold'),bg='skyblue',command=termagreed).grid(row=1,sticky=W)
        
        self.chkaccountonhold=Checkbutton(leftframe2LL,text='ACCOUNT ON HOLD',variable=var3,onvalue=1,offvalue=0,
                                        font=('arial',19,'bold'),bg='skyblue',command=acctonhold).grid(row=2,sticky=W)
        
        self.chkrestrictmailing=Checkbutton(leftframe2LL,text='RESTRICT MAILING',variable=var4,onvalue=1,offvalue=0,
                                        font=('arial',19,'bold'),bg='skyblue',command=restrictedmails).grid(row=3,sticky=W)

        #=======================================leftframe2LR==========================================

        self.txtinfo0=Text(leftframe2LR,height=2.1,width=63,font=('arial',10,'bold'))
        self.txtinfo0.grid(row=0,column=0,pady=2)

        self.txtinfo1=Text(leftframe2LR,height=2.1,width=63,font=('arial',10,'bold'))
        self.txtinfo1.grid(row=1,column=0,pady=2)

        self.txtinfo2=Text(leftframe2LR,height=2.1,width=63,font=('arial',10,'bold'))
        self.txtinfo2.grid(row=2,column=0,pady=2)

        self.txtinfo3=Text(leftframe2LR,height=2.1,width=63,font=('arial',10,'bold'))
        self.txtinfo3.grid(row=3,column=0,pady=2)

        #================================leftframe3==========================================

        self.btntotal=Button(leftframe3,padx=33,pady=2,bd=4,fg="black",font=('arial',20,'bold'),width=6,height=2,
                             bg="skyblue",text="Total",command=totalcost).grid(row=0,column=0)
        
        self.btnreset=Button(leftframe3,padx=33,pady=2,bd=4,fg="black",font=('arial',20,'bold'),width=6,height=2,
                             bg="skyblue",text="Reset",command=Reset).grid(row=0,column=1)
                             
        self.btnexit=Button(leftframe3,padx=34,pady=2,bd=4,fg="black",font=('arial',20,'bold'),width=6,height=2,
                            bg="skyblue",text='Exit',command=iexit).grid(row=0,column=3)

        self.btnsave=Button(leftframe3,padx=34,pady=2,bd=4,fg="black",font=('arial',20,'bold'),width=6,height=2,
                            bg="skyblue",text='Save',command=database).grid(row=0,column=2)
        
                             




if __name__=="__main__":
    root=Tk()
    application=rental_inventory(root)
    root.mainloop()
