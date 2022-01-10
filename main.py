"""
This project can be used freely in any type of use as long as the credits are maintained.
If you want to use this project for commercial use. QT has a license for that also. Please visit "qt.io" for more information.
"""

# Import Dependencies
import os
import sys
import datetime
import webbrowser as wb
from Interface.UI import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


# Main Window
def show_about():
    about_msg_box = QtWidgets.QMessageBox()
    about_msg_box.setText("""This is a simple text editor, but more lightweight, customizable, robust and easy to use.
    As this is a beta release we will provide a website link for all other user guides.
    """)
    about_msg_box.setWindowTitle("Pustak")
    about_msg_box.setWindowIcon(QtGui.QIcon("Interface/Icons/main_icon.ico"))
    about_msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    about_msg_box.exec_()


def show_help():
    help_msg_box = QtWidgets.QMessageBox()
    help_msg_box.setText("""
    As this is beta release for testing, help and about is currently not available in this version.
    """)
    help_msg_box.setWindowTitle("Pustak")
    help_msg_box.setWindowIcon(QtGui.QIcon("Interface/Icons/main_icon.ico"))
    help_msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    help_msg_box.exec_()


class App_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(App_Window, self).__init__()

        # Interface
        self.user_interface = Ui_MainWindow()
        self.user_interface.setupUi(self)

        # Window Properties
        # Set default window title to "Untitled".
        self.windowTitle = "Untitled"
        self.setWindowTitle(self.windowTitle)  # Set window title.
        self.setWindowIcon(
            QtGui.QIcon("Interface/Icons/main_icon.ico"))  # Set up default window icon located in "Interface/Icons".
        self.change_to_light_theme()  # Set light theme as default theme

        # Get the cursor in QTextEdit (editor).
        self.editor_cursor = self.user_interface.editor.textCursor()

        # Set shortcuts
        """
        File menu shortcuts.
        """
        self.user_interface.actionNew.setShortcut("Ctrl+N")
        self.user_interface.actionOpen.setShortcut("Ctrl+O")
        self.user_interface.actionSave.setShortcut("Ctrl+S")
        self.user_interface.actionSave_As.setShortcut("Ctrl+Shift+S")
        self.user_interface.actionPrint.setShortcut("Ctrl+P")
        self.user_interface.actionExit.setShortcut("Alt+F4")

        """
        Format menu shortcuts
        """
        self.user_interface.actionSelect_All.setShortcut("Ctrl+A")
        self.user_interface.actionDay.setShortcut("Ctrl+D")
        self.user_interface.actionDate_And_Time.setShortcut("Ctrl+Shift+D")
        self.user_interface.actionPrint.setShortcut("Ctrl+P")
        self.user_interface.actionInsert_Images.setShortcut("Ctrl+I")

        """
        View menu, Zoom shortcuts
        """
        self.user_interface.actionZoom_In.setShortcut("Ctrl+-")
        self.user_interface.actionZoom_Out.setShortcut("Ctrl++")

        # Connect actions to functions
        self.user_interface.actionNew.triggered.connect(self.new_file)
        self.user_interface.actionOpen.triggered.connect(self.open_file)
        self.user_interface.actionSave.triggered.connect(self.save_files)
        self.user_interface.actionSave_As.triggered.connect(self.save_as_file)
        self.user_interface.actionPrint.triggered.connect(
            self.print_preview_dialog)
        self.user_interface.actionExit.triggered.connect(self.closeEvent)
        self.user_interface.actionZoom_Out.triggered.connect(self.zoom_In)
        self.user_interface.actionZoom_In.triggered.connect(self.zoom_Out)
        self.user_interface.actionDate_And_Time.triggered.connect(
            self.date_and_time_in_editor)
        self.user_interface.actionDay.triggered.connect(self.day_in_editor)
        self.user_interface.actionSelect_All.triggered.connect(
            self.user_interface.editor.selectAll)
        self.user_interface.actionDark.triggered.connect(
            self.change_to_dark_theme)
        self.user_interface.actionLight_Defualt.triggered.connect(
            self.change_to_light_theme)
        self.user_interface.actionAbout.triggered.connect(self.show_about)
        self.user_interface.actionMore.triggered.connect(self.show_help_on_web)

    """
    Show error
    Shows message box when an error occurs.
    Args: Error
    """

    def show_error(self, error):
        # Show message box when error occurs. Default button is ok.
        error_msg_box = QtWidgets.QMessageBox.question(self, self.windowTitle, str(error),
                                                       QtWidgets.QMessageBox.StandardButton.Ok, icon=QtGui.QIcon.Warning)

        # If Ok is clicked in the message box then do nothing just close the message box.
        if error_msg_box == QtWidgets.QMessageBox.StandardButton.Ok:
            pass

    """
    Open files for pustak.
    Args: Nothing
    """

    def open_file(self):
        # Open file dialog to get the file path.
        self.open_file_dialog = QtWidgets.QFileDialog.getOpenFileName(self, "Open", ".",
                                                                      "Text Document (*.txt);;All Files (*.*)")
        # If nothing is in the file dialog index [0], where the actual file path is, it will do nothing.
        if self.open_file_dialog[0] == "":
            pass

        # If file dialog index [0] has some value, then it will try to open that file.
        elif self.open_file_dialog[0] != "":
            # Get the file path by getting the index [0] of open_file_dialog.
            self.valid_file_path = self.open_file_dialog[0]
            try:
                # Try to open that file in read mode.
                with open(self.valid_file_path, 'r') as read_file:
                    file_data = read_file.read()  # Read file
                    # When the file is opened and read successfully then set editor text to the text present in file.
                    self.user_interface.editor.setPlainText(file_data)
                    # Move the cursor at end once any file is opened.
                    self.user_interface.editor.moveCursor(
                        QtGui.QTextCursor.MoveOperation.End)
                    # Close the file that was opened earlier.
                    read_file.close()
                    # Get filename from the file path.
                    file_name = os.path.split(self.valid_file_path)
                    # Set windowTitle to filename.
                    self.windowTitle = str(file_name[1])
                    # Set window title to filename.
                    self.setWindowTitle(self.windowTitle)

            # Except Errors
            except Exception as e:
                self.show_error(e)

    """
    Save files
    Args: Nothing
    """

    def save_files(self):
        # If windowTitle is equal to "Untitled" this means that this file is not saved locally. Then, if this action is triggered then open save dialog.
        if self.windowTitle == "Untitled":
            # Open save dialog.
            self.save_file_dialog = QtWidgets.QFileDialog.getSaveFileName(self, "Save",
                                                                          ".", "Text Document (*.txt);;All Files(*.*)")

            # If the value of [0] index of save file dialog is not empty. Then, open file in write mode or create that file.
            if self.save_file_dialog[0] != "":
                try:
                    # Open path in write mode.
                    with open(self.save_file_dialog[0], 'w') as write_file:
                        # Write editor text to file.
                        write_file.write(
                            self.user_interface.editor.toPlainText())
                        write_file.close()  # Close the file.

                # Except errors
                except Exception as e:
                    self.show_error(e)

        # If windowTitle is not equal to "Untitled", this means that file is present locally on the machine.
        elif self.windowTitle != "Untitled":
            try:
                # Open file in both read and write mode.
                with open(self.valid_file_path, 'r+') as write_file2:
                    # Get the text in editor.
                    editor_text = self.user_interface.editor.toPlainText()
                    write_file2.truncate(0)  # Clear up the file.
                    # Write text present in the editor to file.
                    write_file2.write(editor_text)
                    write_file2.close()  # Close the file.

            # Except errors
            except Exception as e:
                self.show_error(e)

    """
    New file
    Args: Nothing
    """

    def new_file(self):
        # If the windowTitle is equal to "Untitled" and something is their in the editor.
        if self.windowTitle == "Untitled" and self.user_interface.editor.toPlainText() != "":
            # Show message box. Standard buttons are Save, Discard and Cancel.
            new_msg_box = QtWidgets.QMessageBox.question(self, str(self.windowTitle),
                                                         "Do you want to make changes in {}".format(
                                                             self.windowTitle),
                                                         QtWidgets.QMessageBox.StandardButton.Save | QtWidgets.QMessageBox.StandardButton.Discard | QtWidgets.QMessageBox.StandardButton.Close)
            # If save is clicked then it will call save method.
            if new_msg_box == QtWidgets.QMessageBox.StandardButton.Save:
                self.save_files()

            # If Discard is clicked then it will clear up the editor and set window title to default.
            elif new_msg_box == QtWidgets.QMessageBox.StandardButton.Discard:
                self.user_interface.editor.clear()  # Clear text in editor.
                self.windowTitle = "Untitled"  # Set windowTitle to Untitled.
                # Set window title to default.
                self.setWindowTitle(self.windowTitle)

            # If cancel is clicked then it will do nothing.
            elif new_msg_box == QtWidgets.QMessageBox.StandardButton.Cancel:
                pass

        # If windowTitle is not Untitled this means that file is present locally on the machine.
        elif self.windowTitle != "Untitled":
            try:
                # Open the file both read and write mode.
                with open(self.valid_file_path, 'r+') as read_and_write_file:
                    # Get the text in the editor.
                    text_in_editor = self.user_interface.editor.toPlainText()
                    text_in_file = read_and_write_file.read()  # Read the file.
                    # If the text in editor is not equal to the text in the file. Then, it will ask user opinion.
                    if text_in_file != text_in_editor:
                        # Show message box. Standard buttons are Save, Discard and Cancel.
                        new_save_msg_box = QtWidgets.QMessageBox.question(self, str(self.windowTitle),
                                                                          "Do you want to make change to {}".format(
                                                                              str(self.windowTitle)),
                                                                          QtWidgets.QMessageBox.StandardButton.Save | QtWidgets.QMessageBox.StandardButton.Discard | QtWidgets.QMessageBox.StandardButton.Cancel)

                        # If save is clicked then it will call save file method.
                        if new_save_msg_box == QtWidgets.QMessageBox.StandardButton.Save:
                            self.save_files()  # Call method.
                            # Clear text in the editor.
                            self.user_interface.editor.clear()
                            # Set windowTitle to "Untitled".
                            self.windowTitle = "Untitled"
                            # Set window title to default
                            self.setWindowTitle(self.windowTitle)

                        # If discard is clicked it will set all things to default.
                        elif new_save_msg_box == QtWidgets.QMessageBox.StandardButton.Discard:
                            # Clear the text in the editor.
                            self.user_interface.editor.clear()
                            # Set windowTitle to "Untitled".
                            self.windowTitle = "Untitled"
                            # Set window title to default
                            self.setWindowTitle(self.windowTitle)

                        # If cancel is clicked then it will do nothing.
                        elif new_save_msg_box == QtWidgets.QMessageBox.StandardButton.Cancel:
                            pass

                    elif text_in_file == text_in_editor:
                        # Set windowTitle to default.
                        self.windowTitle = "Untitled"
                        # Clear text in editor.
                        self.user_interface.editor.clear()
                        # Set window title to default.
                        self.setWindowTitle(self.windowTitle)

            # Except errors
            except Exception as e:
                self.show_error(e)

    """
    Save As files
    """

    def save_as_file(self):
        # Open save file dialog.
        save_as_file_dialog = QtWidgets.QFileDialog.getSaveFileName(self, "Save As", ".",
                                                                    "Text Documents (*.txt);;All Files (*.*)")

        # If filepath is not empty then create and write files.
        if save_as_file_dialog[0] != "":
            try:
                # Create/open file in write mode.
                with open(save_as_file_dialog[0], "w") as save_as_file:
                    # Write text in the file present in the editor.
                    save_as_file.write(
                        self.user_interface.editor.toPlainText())
                    save_as_file.close()  # Close file

            # Except errors
            except Exception as e:
                self.show_error(e)

    """
    These are method to make a print dialog.
    """

    def print_file(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.user_interface.editor.print_(printer)

    def print_preview_dialog(self):

        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec_()

    def print_preview(self, printer):
        self.user_interface.editor.print_(printer)

    """
    Close App
    Check for file status before closing.
    Args: Nothing
    """

    def closeEvent(self, event):
        # If windowTitle is equal to "Untitled" and editor is not empty. Then it will open a message box asking for user choice.
        if self.windowTitle == "Untitled" and self.user_interface.editor.toPlainText() != "":
            # Open message box. Standard buttons are Save, Discard and Cancel.
            close_app_msg_box = QtWidgets.QMessageBox.question(self, str(self.windowTitle),
                                                               "Do you want to make changes in {}".format(
                                                                   self.windowTitle),
                                                               QtWidgets.QMessageBox.StandardButton.Save | QtWidgets.QMessageBox.StandardButton.Discard | QtWidgets.QMessageBox.StandardButton.Cancel)

            # If save is clicked then it will call save method and then close the app.
            if close_app_msg_box == QtWidgets.QMessageBox.StandardButton.Save:
                self.save_files()
                event.accept()

            # If discard is clicked then it will close the app.
            elif close_app_msg_box == QtWidgets.QMessageBox.StandardButton.Discard:
                self.close()

            # If cancel is clicked then it will do nothing.
            elif close_app_msg_box == QtWidgets.QMessageBox.StandardButton.Cancel:
                event.ignore()

        # If it is safe to close then it will ask for user opinion.
        else:
            try:
                # Open message box.
                exit_msg_box = QtWidgets.QMessageBox.question(self, "Pustak", "Do you really want to exit",
                                                              QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

                # If yes is clicked then it will close the app.
                if exit_msg_box == QtWidgets.QMessageBox.StandardButton.Yes:
                    self.close()

                # If any other button is clicked then it will do nothing.
                else:
                    pass

            # Except errors
            except Exception as e:
                self.show_error(e)

    """
    Put Date
    Args: Nothing
    """

    def date_and_time_in_editor(self):
        current_date_and_time = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S")  # Get date/month/year and hours:minutes:seconds
        # Get the current position of the cursor.
        current_cursor_pos = self.user_interface.editor.textCursor()
        # Insert date and time at the current position of the cursor.
        current_cursor_pos.insertText(str(current_date_and_time))

    """
    Day
    Args: Nothing
    """

    def day_in_editor(self):
        current_day = datetime.datetime.now()  # Setup module.
        current_day2 = current_day.strftime("%A")  # Get the current day name.
        # Get the current cursor position.
        editor_cursor = self.user_interface.editor.textCursor()
        try:
            # Insert day name at the current cursor position.
            editor_cursor.insertText(str(current_day2))

        # Except errors
        except Exception as e:
            self.show_error(e)

    """
    Change Themes
    """

    def change_to_dark_theme(self):
        try:
            # Open dark stylesheet located in "Interface/Themes" in read mode.
            with open("Interface/Themes/Dark.qss", 'r') as dark_stylesheet:
                # Read the stylesheet.
                self.dark_stylesheet_for_app = dark_stylesheet.read()
                dark_stylesheet.close()  # Close the file.
                # Set stylesheet.
                self.setStyleSheet(self.dark_stylesheet_for_app)
                self.current_theme = "Dark"

        # Except errors
        except Exception as e:
            self.show_error(e)

    def change_to_light_theme(self):
        try:
            # Open light stylesheet located in "Interface/Themes" in read mode.
            with open("Interface/Themes/Light.qss") as light_stylesheet:
                # Read the stylesheet.
                self.light_style = light_stylesheet.read()
                light_stylesheet.close()  # Close the file.
                self.setStyleSheet(self.light_style)  # Set stylesheet.
                self.current_theme = "Light"

        # Except errors
        except Exception as e:
            self.show_error(e)

    """
    Zoom Out And Zoom In
    Zooms text when Ctrl + Plus is clicked. Zooms in when Ctrl + Minus.
    Args: Nothing
    """

    def zoom_Out(self):
        # Zoom - 1
        self.user_interface.editor.zoomOut(1)

    def zoom_In(self):
        # Zoom in + 1
        self.user_interface.editor.zoomIn(1)

    """
    User Guides
    """
    def show_help_on_web(self):
        wb.open("https://github.com/Raghav67816/Pustak")

    def show_about(self):
        wb.open("https://github.com/Raghav67816/Pustak")


# Run app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Create QApplication instance
    GUI = App_Window()  # Define main user interface.
    GUI.show()  # Show the interface.
    sys.exit(app.exec())  # Execute the instance.
