from tkinter import *

window = Tk()
window.minsize(300,300)
window.title("BMI Calculater")

def calculateFun():
    bmiCal = float(entryx.get())/((float(entryy.get())/100) ** 2)
    result = round(bmiCal,2)
    print(result)
    if(result == 18.5):
        print(f"BMI calculate is {result} and under weight")
    elif(18.5 <= result <=24.9):
        print(f"BMI calculate is {result} and normal")
    elif(25<= result<= 29.9):
        print(f"BMI calculate is {result} and over weight")
    elif(30 <= result <= 34.9):
        print(f"BMI calculate is {result} and obesity class I")
    elif(35 <= result <= 39.9):
        print(f"BMI calculate is {result} and obesity class II")
    else:
        print(f"BMI calculate is {result} and extreme obesity")



#weight
labelw = Label()
labelw.config(bg="#fefefd", fg="black", text="Enter your weight (kg)")
labelw.place(x=100, y=50)
entryx = Entry()
entryx.place(x=100, y =80)

labelh = Label()
labelh.config(bg="#fefefd", fg="black", text="Enter your height (cm)")
labelh.place(x=100, y=130)
entryy = Entry()
entryy.place(x=100, y =160)

button = Button()
button.config(bg="#fefefd", fg="black", text="Calculate", command=calculateFun)
button.place(x=140, y= 200)


window.mainloop()
