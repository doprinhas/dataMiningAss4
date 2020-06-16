from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class View:

    def __init__(self, master, controller):
        self.controller = controller
        self.master = master
        master.title("K-Means Clustering")
        master.minsize(1280, 800)

        vcmd = master.register(self.validate)

        self.browse_ent = Entry(master, text="Open File")
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
        self.browse_ent.delete(0, END)
        self.browse_ent.insert(0, self.filename)

    def pre_process(self):
        try:
            self.controller.pre_process(self.filename)
        except:
            return

    def cluster(self):
        if self.num_of_clusters_ent.get() == '' or self.num_of_iterations_ent.get() == '':
            return
        clusters_num = int(self.num_of_clusters_ent.get())
        iterations_num = int(self.num_of_iterations_ent.get())
        self.controller.cluster(clusters_num, iterations_num)

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, controller):
        self.__controller = controller
