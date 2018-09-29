if __name__ == "__main__":
    import wx
    import gui

    app = wx.App()
    frame = gui.DataGingerFrame(None, title="Hello World!")
    frame.Show()
    app.MainLoop()
