# Screenshot App

This is a Python-based Screenshot App that allows users to capture screenshots, preview them, save them as PDF files, and reset the captures. The app provides a user-friendly GUI built with Tkinter.

## Features

![image](https://github.com/MaxCar31/ScreenShotApp/assets/141116497/da9f0e7d-11b7-43e8-a686-25a6836b762d)


- **Take Screenshots:** Capture the current screen and preview the screenshot within the app.
- **Save to PDF:** Save all captured screenshots into a single PDF file.
- **Reset Captures:** Clear all captured screenshots and reset the app.
- **Scrollable Preview List:** View a list of previously taken screenshots.
- **Shortcut Key:** Use `Ctrl + C` to quickly take a screenshot.

## Installation

To run this project, you need to have Python and the necessary libraries installed. Follow the steps below to set up the environment:

### Prerequisites

1. **Python:** Make sure Python is installed on your system. You can download it from [Python's official website](https://www.python.org/).

2. **pip:** Ensure you have `pip` installed for managing Python packages.

### Required Libraries

Install the required Python libraries using `pip`:

```bash
pip install pyautogui Pillow tk
```

## Clone the Repository
#### Clone the project repository to your local machine:

```bash
git clone https://github.com/MaxCar31/ScreenShotApp.git
cd ScreenShotApp
```
### Run the Application
Navigate to the project directory and run the application:

```bash
python ScreenShotApp.py
```
Usage

Launch the App: Run the screenshot_app.py script to launch the Screenshot App.

- Take a Screenshot: Click the "Take Screenshot" button or press Ctrl + C to capture the current screen.
- Preview Screenshot: The captured screenshot will be displayed in the app. The screenshot will also be added to the scrollable preview list.
- Save to PDF: Click the "Save to PDF" button to save all captured screenshots into a single PDF file. Choose the location to save the PDF file when prompted.
- Reset Captures: Click the "Reset Captures" button to clear all captured screenshots and reset the app.

### Project Structure
The project has the following structure:

```bash
screenshot-app/
├── screenshots/         # Directory where screenshots are saved
├── screenshot_app.py    # Main script to run the application
└── README.md            # This README file
```

### Dependencies
The following pip libraries are required for this project:

- pyautogui
- Pillow
- tk
  
### Install them using:

```bash
pip install pyautogui Pillow tk
```

#### License
This project is licensed under the MIT License. See the LICENSE file for details.

#### Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

#### Acknowledgments
- Python
- Tkinter
- Pillow
- pyautogui
  
#### Contact

If you have any questions or feedback, feel free to reach out to the project maintainer at maxmateo.carrion@gmail.com

