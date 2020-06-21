from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk


class View:

    def __init__(self, master, controller):
        """ Constructor for View Class """

        self.controller = controller
        self.master = master
        self.filename = ''
        master.title("K-Means Clustering")
        master.minsize(300, 200)

        vcmd = master.register(self.validate)

        self.browse_ent = Entry(master, text="Open File")
        self.browse_ent.config(state=DISABLED)
        self.browse_btn = Button(master, text="Browse", command=self.file_dialog)

        self.num_of_clusters_ent = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.num_of_clusters_lbl = Label(master, text="Number Of Clusters: ")

        self.num_of_iterations_ent = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.num_of_iterations_lbl = Label(master, text="Number Of Iterations: ")

        self.pre_process_btn = Button(master, text="Pre-process", command=self.pre_process)
        self.cluster_btn = Button(master, text="Cluster", command=self.cluster)

        # self.num_of_clusters = Entry()
        # self.total = 0
        # self.entered_number = 0
        #
        # self.total_label_text = IntVar()
        # self.total_label_text.set(self.total)
        # self.total_label = Label(master, textvariable=self.total_label_text)
        #
        # self.label = Label(master, text="Total:")
        #
        # vcmd = master.register(self.validate) # we have to wrap the command
        # self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        #
        # self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        # self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        # self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.browse_btn.grid(column=2, row=2, padx=5, pady=5)
        self.browse_ent.grid(column=3, row=2, padx=5, pady=5)

        self.num_of_clusters_ent.grid(column=3, row=3, padx=5, pady=5)
        self.num_of_clusters_lbl.grid(column=2, row=3, padx=5, pady=5)

        self.num_of_iterations_ent.grid(column=3, row=4, padx=5, pady=5)
        self.num_of_iterations_lbl.grid(column=2, row=4, padx=5, pady=5)

        self.pre_process_btn.grid(column=3, row=5, padx=5, pady=5)
        self.cluster_btn.grid(column=4, row=5, padx=5, pady=5)


    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else:  # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

    def file_dialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype= \
            [("Excel file", "*.xlsx")])
        self.browse_ent.config(state=NORMAL)
        self.browse_ent.delete(0, END)
        self.browse_ent.insert(0, self.filename)
        self.browse_ent.config(state=DISABLED)

    def pre_process(self):
        try:
            if self.filename == '':
                messagebox.showerror("Error", "Path to data is invalid")
                return

            self.controller.pre_process(self.filename)
            messagebox.showinfo("Finished!", "Preprocessing completed successfully! ")
        except ValueError as err:
            messagebox.showerror('Error!', str(err))
            return
        except Exception as err:
            print(err)
            return

    def cluster(self):
        try:
            if self.controller.proc_data is None:
                messagebox.showerror("Error!", "Data is not processed")
                return
            if self.num_of_clusters_ent.get() == '' or self.num_of_iterations_ent.get() == '':
                messagebox.showerror('Error!', 'You must fill all of the fields')
                return
            clusters_num = int(self.num_of_clusters_ent.get())
            iterations_num = int(self.num_of_iterations_ent.get())
            if clusters_num < 2 or clusters_num > len(self.controller.proc_data.index):
                messagebox.showerror('Error!', 'The number of clusters is not valid')
                return
            if iterations_num < 1 or iterations_num > 100:
                messagebox.showerror('Error!', 'The number of iterations is not valid')

            graphs = self.controller.cluster(clusters_num, iterations_num)

            self.master.geometry("1280x700")

            graph1 = ImageTk.PhotoImage(Image.open(graphs[0]))
            graph2 = ImageTk.PhotoImage(Image.open(graphs[1]))
            graph_lbl1 = Label(self.master, image=graph1)
            graph_lbl2 = Label(self.master, image=graph2)
            graph_lbl1.place(relx=0.0, rely=1.0, anchor='sw')
            graph_lbl2.place(relx=1.0, rely=1.0, anchor='se')

            messagebox.showinfo("Finished!", "Clustering finished successfully")

        except Exception as err:
            print(err)
            return

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, controller):
        self.__controller = controller
