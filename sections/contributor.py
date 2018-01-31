from tkinter import Entry, W, E, StringVar, END

from apa_widgets import *


class ContributorSection(Section):
    def __init__(self, master, **options):
        Section.__init__(self, master, **options)

        self.contributor_first_name = StringVar()
        self.contributor_middle_name = StringVar()
        self.contributor_last_name = StringVar()

        contributors_frame = Section(self.master)
        PrimaryLabel(contributors_frame, text='Contributors:', font=('', 11, 'bold')).grid(row=0, columnspan=3,
                                                                                           sticky=W)
        # first name
        PrimaryLabel(contributors_frame, text='First Name').grid(row=1, sticky=W)
        self.contributor_first_name_entry = Entry(contributors_frame, width=20,
                                                  textvariable=self.contributor_first_name)
        self.contributor_first_name_entry.grid(row=2, column=0, sticky=W)
        # middle name
        PrimaryLabel(contributors_frame, text='MI').grid(row=1, column=1, sticky=W)
        Entry(contributors_frame, width=5, textvariable=self.contributor_middle_name).grid(row=2, column=1, sticky=W)
        # last name
        PrimaryLabel(contributors_frame, text='Last Name').grid(row=1, column=2, sticky=W)
        Entry(contributors_frame, width=20, textvariable=self.contributor_last_name).grid(row=2, column=2, sticky=W)
        contributors_frame.pack(anchor=W)

        # Add Contributor Button
        add_contributor_btn = Section(self.master)
        PrimaryButton(add_contributor_btn, text='+ Add another contributor',
                      # command=self.add_contributor
                      ).pack(anchor=E)
        add_contributor_btn.pack(anchor=E)
