"""
This module contains everything related to the GUI.
"""

import wx


class DataGingerFrame(wx.Frame):
    """
    Main frame of the Data Ginger application.
    """

    def __init__(self, *args, **kwargs):
        super(DataGingerFrame, self).__init__(*args, **kwargs)

        main_panel = wx.Panel(self)

        text = wx.StaticText(main_panel, label="Hello World!", pos=(25, 25))
        font = text.GetFont()
        font.PointSize += 10
        font = font.Bold()
        text.SetFont(font)

        self.CreateStatusBar()
        self.SetStatusText("Welcome!")
