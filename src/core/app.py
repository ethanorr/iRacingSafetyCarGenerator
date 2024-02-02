import configparser
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Load settings from config file
        self.settings = configparser.ConfigParser()
        self.settings.read("settings.ini")

        # Set window properties
        self.title("iRacing Safety Car Generator")

        # Create widgets
        self._create_widgets()

    def _create_widgets(self):
        # Create a two column grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create and grid widgets for each setting
        self.min_sc_label = tk.Label(self, text="Minimum Safety Cars")
        self.min_sc_entry = tk.Entry(self)
        self.min_sc_entry.insert(
            0,
            self.settings["settings"]["min_safety_cars"]
        )
        self.min_sc_label.grid(row=0, column=0)
        self.min_sc_entry.grid(row=0, column=1)

        self.max_sc_label = tk.Label(self, text="Maximum Safety Cars")
        self.max_sc_entry = tk.Entry(self)
        self.max_sc_entry.insert(
            0,
            self.settings["settings"]["max_safety_cars"]
        )
        self.max_sc_label.grid(row=1, column=0, pady=(5, 0))
        self.max_sc_entry.grid(row=1, column=1, pady=(5, 0))

        self.start_minute_label = tk.Label(self, text="Start Minute")
        self.start_minute_entry = tk.Entry(self)
        self.start_minute_entry.insert(
            0,
            self.settings["settings"]["start_minute"]
        )
        self.start_minute_label.grid(row=2, column=0, pady=(5, 0))
        self.start_minute_entry.grid(row=2, column=1, pady=(5, 0))

        self.end_minute_label = tk.Label(self, text="End Minute")
        self.end_minute_entry = tk.Entry(self)
        self.end_minute_entry.insert(
            0,
            self.settings["settings"]["end_minute"]
        )
        self.end_minute_label.grid(row=3, column=0, pady=(5, 0))
        self.end_minute_entry.grid(row=3, column=1, pady=(5, 0))

        self.min_time_between_label = tk.Label(
            self,
            text="Minimum Minutes Between SC Events"
        )
        self.min_time_between_entry = tk.Entry(self)
        self.min_time_between_entry.insert(
            0,
            self.settings["settings"]["min_time_between"]
        )
        self.min_time_between_label.grid(row=4, column=0, pady=(5, 0))
        self.min_time_between_entry.grid(row=4, column=1, pady=(5, 0))

        self.laps_under_sc_label = tk.Label(self, text="Laps Under Safety Car")
        self.laps_under_sc_entry = tk.Entry(self)
        self.laps_under_sc_entry.insert(
            0,
            self.settings["settings"]["laps_under_sc"]
        )
        self.laps_under_sc_label.grid(row=5, column=0, pady=(5, 0))
        self.laps_under_sc_entry.grid(row=5, column=1, pady=(5, 0))

        # Create a save settings button
        self.save_button = tk.Button(
            self,
            text="Save Settings",
            command=self._save_settings
        )
        self.save_button.grid(row=6, column=0, columnspan=2, pady=(5, 0))

        # Create a button to generate safety car events
        self.generate_button = tk.Button(
            self,
            text="Generate Safety Car Events",
            command=self.generate
        )
        self.generate_button.grid(row=7, column=0, columnspan=2, pady=(5, 0))

        # Create a disabled text box to display the generated safety car events
        self.sc_text = tk.Text(self, height=10, width=50, state="disabled")
        self.sc_text.grid(row=8, column=0, columnspan=2, pady=(5, 0))

    def _save_settings(self):
        # Get settings from the entry widgets
        min_sc_entry = self.min_sc_entry.get()
        max_sc_entry = self.max_sc_entry.get()
        start_minute_entry = self.start_minute_entry.get()
        end_minute_entry = self.end_minute_entry.get()
        min_time_between_entry = self.min_time_between_entry.get()
        laps_under_sc_entry = self.laps_under_sc_entry.get()

        # Save the settings to the config file
        self.settings["settings"]["min_safety_cars"] = min_sc_entry
        self.settings["settings"]["max_safety_cars"] = max_sc_entry
        self.settings["settings"]["start_minute"] = start_minute_entry
        self.settings["settings"]["end_minute"] = end_minute_entry
        self.settings["settings"]["min_time_between"] = min_time_between_entry
        self.settings["settings"]["laps_under_sc"] = laps_under_sc_entry

        with open("settings.ini", "w") as configfile:
            self.settings.write(configfile)

    def generate(self):
        pass