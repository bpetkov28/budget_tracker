import customtkinter
from tkcalendar import DateEntry
import data_methods


class LefSidebar(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.button0 = customtkinter.CTkButton(self, text="Home", command=self.show_home)
        self.button0.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button1 = customtkinter.CTkButton(self, text="Add new expense", command=self.show_add_expense)
        self.button1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button2 = customtkinter.CTkButton(self, text="Report", command=self.show_report)
        self.button2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

    def show_add_expense(self):
        self.master.show_frame("AddExpense")

    def show_report(self):
        self.master.show_frame("Report")

    def show_home(self):
        self.master.show_frame("Home")


class RightBarHome(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)

        self.label1 = customtkinter.CTkLabel(self, text="Total spent this month:")
        self.label1.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")

        self.label2 = customtkinter.CTkLabel(self, text="Money remaining this month:")
        self.label2.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="w")

        total_month = int(data_methods.view_total())
        money_remaining = 10000 - total_month

        self.label3 = customtkinter.CTkLabel(self, text=f"$ {total_month}")
        self.label3.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="w")

        self.label4 = customtkinter.CTkLabel(self, text=f"$ {money_remaining}")
        self.label4.grid(row=1, column=1, padx=10, pady=(5, 10), sticky="w")


class AddExpense(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid_columnconfigure((0, 1), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)

        self.date_label = customtkinter.CTkLabel(self, text="Date:")
        self.date_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
        self.date_picker = DateEntry(self, width=25, background='#1F6AA5', foreground='white', borderwidth=2)
        self.date_picker.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="w")
        self.date_picker.config(date_pattern='y-mm-dd')

        categories = ['Entertainment', 'Food', 'Groceries', 'Health', 'Rent', 'Shopping', 'Transport', 'Utilities']
        self.category_label = customtkinter.CTkLabel(self, text="Category:")
        self.category_label.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="w")
        self.category = customtkinter.CTkComboBox(self, values=categories, state="readonly")
        self.category.set("Pick category")
        self.category.grid(row=1, column=1, padx=10, pady=(5, 10), sticky="w")

        self.desc_label = customtkinter.CTkLabel(self, text="Description:")
        self.desc_label.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="w")
        self.desc = customtkinter.CTkTextbox(self, width=145, height=50)
        self.desc.grid(row=2, column=1, padx=10, pady=(5, 10), sticky="w")

        self.amount_label = customtkinter.CTkLabel(self, text="Amount:")
        self.amount_label.grid(row=3, column=0, padx=10, pady=(5, 10), sticky="w")
        self.amount = customtkinter.CTkEntry(self, placeholder_text="Amount")
        self.amount.grid(row=3, column=1, padx=10, pady=(5, 10), sticky="w")

        self.button = customtkinter.CTkButton(self, text="Add", command=self.get_expense,
                                              fg_color="#7a7a52", hover_color="#6b6b47")
        self.button.grid(row=4, column=1, padx=10, pady=(10, 5), sticky="w")

    def get_expense(self):
        selected_date = self.date_picker.get()
        selected_category = self.category.get()
        selected_desc = self.desc.get("1.0", customtkinter.END).strip()
        selected_amount = self.amount.get()
        input_data = [selected_date, selected_amount, selected_category, selected_desc]

        # Save the expense data
        data_methods.write_expense(input_data)

        # Show confirmation dialog
        self.show_confirmation_dialog()

    def show_confirmation_dialog(self):
        dialog = customtkinter.CTkToplevel(self)
        dialog.geometry("300x200")
        dialog.title("Confirmation")

        # Make sure the dialog is above the main window
        dialog.transient()  # Set to be on top of the main window
        dialog.grab_set()  # Make it modal (disables other windows)
        dialog.focus_set()  # Focus on the dialog

        label = customtkinter.CTkLabel(dialog, text="The expense has been added successfully!")
        label.pack(pady=20)

        close_screen_btn = customtkinter.CTkButton(dialog, text="OK", command=dialog.destroy)
        close_screen_btn.pack(pady=10)


class Report(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=0)

        total = int(data_methods.view_total())

        self.label1 = customtkinter.CTkLabel(self, text="Total expenses:")
        self.label1.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")

        self.label1x2 = customtkinter.CTkLabel(self, text=f"$ {total}")
        self.label1x2.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="w")

        self.label2 = customtkinter.CTkLabel(self, text="By month:")
        self.label2.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="w")

        self.button2 = customtkinter.CTkButton(self, text="Show", fg_color="#7a7a52",
                                               hover_color="#6b6b47", command=self.show_date_on_click)
        self.button2.grid(row=1, column=1, padx=10, pady=(5, 10), sticky="w")

    def show_date_on_click(self):
        self.show_by_month()

    def show_by_month(self):
        dialog = customtkinter.CTkToplevel(self)
        dialog.geometry("650x300")
        dialog.title("Monthly expenses by date")
        dialog.grid_columnconfigure((0, 1), weight=0)
        dialog.grid_columnconfigure(2, weight=1)
        dialog.grid_rowconfigure((0, 1, 2), weight=0)

        # Make sure the dialog is above the main window
        dialog.transient()  # Set to be on top of the main window
        dialog.grab_set()  # Make it modal (disables other windows)
        dialog.focus_set()  # Focus on the dialog

        frame1 = customtkinter.CTkFrame(dialog)
        frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        dropdown1 = customtkinter.CTkComboBox(master=frame1, values=['January', 'February', 'March',
                                                                     'April', 'May', 'June',
                                                                     'July', 'August', 'September',
                                                                     'October', 'November', 'December'],
                                              state="readonly")
        dropdown1.grid(row=0, column=0, padx=10, pady=10, sticky='nsw')
        dropdown1.set("Pick month")

        dropdown2 = customtkinter.CTkComboBox(master=frame1, values=[str(x) for x in range(2024, 2019, -1)],
                                              state="readonly")
        dropdown2.grid(row=1, column=0, padx=10, pady=10, sticky='nsw')
        dropdown2.set("Pick year")

        def on_button_click():
            selected_month = dropdown1.get()
            selected_year = dropdown2.get()
            report_response = data_methods.view_by_date(selected_month, selected_year)
            report_response2 = data_methods.view_by_categ(selected_month, selected_year)

            label2.configure(text=report_response)
            label3.configure(text=report_response2)

        button = customtkinter.CTkButton(master=frame1, text="Show", fg_color="#7a7a52", hover_color="#6b6b47",
                                         command=on_button_click)
        button.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="w")

        frame2 = customtkinter.CTkScrollableFrame(dialog)
        frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsw")

        label2 = customtkinter.CTkLabel(frame2, text="", anchor="w", justify="left")
        label2.grid(padx=10, pady=10, sticky="nsw")

        frame3 = customtkinter.CTkScrollableFrame(dialog)
        frame3.grid(row=0, column=2, padx=10, pady=10, sticky="nsw")

        label3 = customtkinter.CTkLabel(frame3, text="", anchor="w", justify="left")
        label3.grid(padx=10, pady=10, sticky="nsw")


class MainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Budget expense tracker")
        self.geometry("500x260")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=0)

        # Create and place the sidebar
        self.left_sidebar = LefSidebar(self)
        self.left_sidebar.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        # Create frames for each screen
        self.home_frame = RightBarHome(self)
        self.add_expense_frame = AddExpense(self)
        self.report_frame = Report(self)

        # Grid frames into the main window
        self.home_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.add_expense_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.report_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Show home screen by default
        self.show_frame("Home")

    def show_frame(self, frame_name):
        self.home_frame.grid_forget()
        self.add_expense_frame.grid_forget()
        self.report_frame.grid_forget()

        if frame_name == "Home":
            self.home_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        elif frame_name == "AddExpense":
            self.add_expense_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        elif frame_name == "Report":
            self.report_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
