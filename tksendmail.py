from tkinter import *
import smtplib

class Email:
    def __init__(self, mail):
        self.mail = mail
        mail.title("Send Emails")
        mail.configure(bg="#1e1e1e")
        mail.geometry("573x600")
        #mail.resizable(width=False, height=False)

        
        self.heading = Label(mail, text="Send emails", fg="white", bg="#222222", font="none 24 bold")
        self.heading.grid(row=1, column=0, pady=5)
        
        #Sender's Email
        self.set = Label(mail, text="Your Email:", font="none 12 bold", fg="white", bg="#222222")
        self.set.grid(row=2, column=0, sticky=W, padx=10)
        self.se = Entry(mail, width=60, bg="white", borderwidth=5, font="none 12 bold")
        self.se.grid(row=3, column=0, sticky=W, padx=10)
        #Sender's Email password
        self.sept = Label(mail, text="Your Email password:", font="none 12 bold", fg="white", bg="#222222")
        self.sept.grid(row=4, column=0, sticky=W, padx=10)
        self.sep = Entry(mail, width=60, bg="white", borderwidth=5, font="none 12 bold")
        self.sep.grid(row=5, column=0, sticky=W, padx=10)
        #Reciever's Email 
        self.rept = Label(mail, text="Reciever's Email:", font="none 12 bold", fg="white", bg="#222222")
        self.rept.grid(row=6, column=0, sticky=W, padx=10)
        self.rep = Entry(mail, width=60, bg="white", borderwidth=5, font="none 12 bold")
        self.rep.grid(row=7, column=0, sticky=W, padx=10)
        #Subject
        self.subj = Label(mail, text="Subject:", font="none 12 bold", fg="white", bg="#222222")
        self.subj.grid(row=8, column=0, sticky=W, padx=10)
        self.sub = Entry(mail, width=60, bg="white", borderwidth=5, font="none 12 bold")
        self.sub.grid(row=9, column=0, sticky=W, padx=10)
        #Body
        self.text1 = Label(mail, text="Body:", font="none 12 bold", fg="white", bg="#222222")
        self.text1.grid(row=10, column=0, sticky=W, padx=10)
        self.text = Text(mail, width=60, height=10, wrap=WORD, background="white", borderwidth=5, font="none 12 bold") 
        self.text.grid(row=11, column=0, columnspan=2, sticky=W, padx=10)
        #Send Mail
        self.send_btn = Button(mail, text="Send Mail", command=self.send, font="none 12 bold", borderwidth=5) 
        self.send_btn.grid(row=12, column=0, pady=5, padx=10)
        #Exit
        self.send_btn = Button(mail, text="Exit Mail", command=self.end, font="none 12 bold", borderwidth=5) 
        self.send_btn.place(x=460, y=553)
        #Clear Contents
        self.send_btn = Button(mail, text="Clear Contents", command=self.clear, font="none 12 bold", borderwidth=5) 
        self.send_btn.place(x=220, y=553)

    def end(self):
        w.destroy()
    def clear(self):
        self.text.delete(0.0, END)
        self.sub.delete(0, 'end')

        self.se.delete(0, 'end')
        self.sep.delete(0, 'end')

        self.rep.delete(0, 'end')
    def send(self):
        #print(self.text.get('1.0', END))
        
        bmail = self.text.get('1.0', END)
        submail = self.sub.get()

        yemail = self.se.get()
        yemailp = self.sep.get()

        remail = self.rep.get()

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        
        s.login(yemail, yemailp)
        message = 'Subject: {}\n\n{}'.format(submail, bmail)
        s.sendmail(yemail, remail, message)
        #print("Email Sent")
        s.quit()
        
w = Tk()
x = Email(w)
w.mainloop()

