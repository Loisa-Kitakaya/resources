# command for "Edit database"
		def create_window():

			# defining properties for a child window
			Child_GUI = Toplevel(master)

			# setting the window name
			Child_GUI.title("Edit DB")

			# setting the window icon
			icon = Image("photo", file="icon.png")
			Child_GUI.tk.call('wm','iconphoto',Child_GUI._w, icon)

			# label
			l = Label(Child_GUI, text="This is window")
			# display label
			l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

		# creating buttons
		button_2 = Button(frame01, text = "Edit DB", relief = RAISED, command = create_window)

		# displaying the buttons
		button_2.pack(side = RIGHT, padx = 5)