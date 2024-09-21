import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# تعریف تصاویر و اسامی
images = {
    "آلبرت اینشتین": "1.png",
    "نیکولا تسلا": "2.png",
    "میر عماد میرمیرانی": "3.png",
    "مهاتما گاندی": "4.png",
    "گیدو ون روسوم": "5.png"
}

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("حدس بزن کیه؟")
root.geometry("400x500")

# متغیرهای جهانی
score = 0
current_person = None

# تابع نمایش تصویر جدید
def show_new_image():
    global current_person, photo
    current_person = random.choice(list(images.keys()))
    image = Image.open(images[current_person])
    image = image.resize((200, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    create_rectangles()
    var.set(None)

# تابع ایجاد مستطیل‌های سیاه
def create_rectangles():
    global rectangles, removed_count
    rectangles = []
    removed_count = 0
    for i in range(5):
        for j in range(5):
            x1 = i * 40
            y1 = j * 40
            x2 = x1 + 40
            y2 = y1 + 40
            rect = canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            rectangles.append(rect)
    canvas.bind("<Button-1>", remove_rectangle)

# تابع حذف مستطیل با کلیک
def remove_rectangle(event):
    global removed_count
    if removed_count < 3:
        for rect in rectangles:
            if canvas.coords(rect)[0] <= event.x <= canvas.coords(rect)[2] and canvas.coords(rect)[1] <= event.y <= canvas.coords(rect)[3]:
                canvas.delete(rect)
                rectangles.remove(rect)
                removed_count += 1
                break
    if removed_count == 3:
        canvas.unbind("<Button-1>")

# تابع بررسی پاسخ
def check_answer():
    global score
    if var.get() == current_person:
        score += 1
        messagebox.showinfo("درست!", f"آفرین! این {current_person} بود.")
    else:
        messagebox.showerror("اشتباه", f"متأسفم، این {current_person} بود.")
    score_label.config(text=f"امتیاز: {score}")
    show_new_image()

# ایجاد المان‌های گرافیکی
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack(pady=20)

var = tk.StringVar()
var.set(None)

for person in images.keys():
    tk.Radiobutton(root, text=person, variable=var, value=person).pack()

submit_button = tk.Button(root, text="ثبت پاسخ", command=check_answer)
submit_button.pack(pady=20)

score_label = tk.Label(root, text=f"امتیاز: {score}")
score_label.pack()

# شروع بازی
show_new_image()

# اجرای برنامه
root.mainloop()