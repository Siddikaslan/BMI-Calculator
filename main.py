import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)
FONT = ("spendthrift", 14)
window.config(pady=60)

height_label = tkinter.Label(text="Enter Your Height (cm)", font=(FONT))
height_label.pack(pady=3)
height_entry = tkinter.Entry(width=25)
height_entry.pack(pady=3)

weight_label = tkinter.Label(text="Enter Your Weight (kg)", font=(FONT))
weight_label.pack(pady=3)
weight_entry = tkinter.Entry(width=25)
weight_entry.pack(pady=3)


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def validate_entry(event):

    if not is_float(event.widget.get()):
        result_label.config(text="Enter a Valid Number!", font=(FONT))
    else:
        result_label.config(text="")


weight_entry.bind("<FocusOut>", validate_entry)
height_entry.bind("<FocusOut>", validate_entry)


def calculate_bmi():
    height_str = height_entry.get()
    weight_str = weight_entry.get()

    if not height_str or not weight_str:
        result_label.config(text="Enter both Height and Weight!", font=(FONT))
        return

    if not is_float(height_str) or not is_float(weight_str):
        result_label.config(text="Enter a Valid Number!", font=(FONT))
        return

    height_cm = float(height_str)
    height_m = height_cm / 100
    weight = float(weight_str)
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        bmi_state = "Underweight \n Biraz kilo alsan iyi olur :)"
    elif 18.5 <= bmi < 24.9:
        bmi_state = "Normal \n İdeal ölçü :)"
    elif 25 <= bmi < 29.9:
        bmi_state = "Overweight \n Biraz kilo vermelisin :)"
    elif 30 <= bmi < 34.9:
        bmi_state = "Obese \n Dostum sağlığın için kilo vermelisin!"
    elif 35 <= bmi <39.9:
        bmi_state = "Obese II \n Dostum sağlığın için kilo vermelisin!"
    else:
        bmi_state = "Extremely Obese \n OMGG Dostum buneee! :(("

    result_label.config(text=f"BMI: {bmi:.2f} \nCategory: {bmi_state}", font=(FONT))


first_button = tkinter.Button(text="Calculate", font=(FONT), command=calculate_bmi)
first_button.pack(pady=5)

result_label = tkinter.Label(text="", font=(FONT))
result_label.pack(pady=10)

window.mainloop()
