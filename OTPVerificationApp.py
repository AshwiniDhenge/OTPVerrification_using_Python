import tkinter as tk
from tkinter import messagebox
import random

class OTPVerificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OTP Verification")

        self.otp = self.generate_otp()
        print(self.otp)

        self.label = tk.Label(root, text="Enter OTP:")
        self.label.pack()

        self.otp_entry = tk.Entry(root)
        self.otp_entry.pack()

        self.verify_button = tk.Button(root, text="Verify", command=self.verify_otp)
        self.verify_button.pack()

    def generate_otp(self):
        # Generate a 4-digit OTP
        return str(random.randint(1000, 9999))

    def verify_otp(self):
        user_otp = self.otp_entry.get()

        if user_otp == self.otp:
            messagebox.showinfo("Success", "OTP Verified!")
        else:
            messagebox.showerror("Error", "Incorrect OTP. Please try again.")

def main():
    root = tk.Tk()
    app = OTPVerificationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()