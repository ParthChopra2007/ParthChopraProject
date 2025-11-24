# ParthChopraProject
<br>
Author- Parth Chopra
Registration No.:25BSA10027

Overview of the Project

This project is a Python-based Water Quality Monitoring System that helps track and visualize the Total Dissolved Solids (TDS) levels in water blocks of a hostel.
The program allows users to:

Enter TDS values for each block

Classify water quality based on TDS levels

Update & delete entries

View stored data

Display a live animated bar graph of TDS levels using Matplotlib

The system acts as a simple decision-support tool to determine whether the water in each block is Excellent, Acceptable, or Poor, and whether purification measures are needed.

Features
1. Water Quality Classification

Based on TDS value, water is categorized into:

Poor

Excellent

Minerally Tasty

Acceptable

Very Poor

2. Menu-Driven Program

User-friendly menu options:

Check water quality for all blocks

Update TDS of a block

Remove an entry

Display complete list

Exit the program

Show LIVE graph

3. Live Animated Graph

Real-time graph refreshes every second

Bars are color-coded based on water quality

Quality label displayed above each bar

4. Dynamic Data Handling

Add, update, and delete TDS values

Automatically refresh graph based on list contents

Technologies / Tools Used
Programming Language

Python 3.x

Libraries

matplotlib.pyplot → for bar graph

matplotlib.animation → for live graph animation

IDE / Environment

Python IDLE, VS Code, Jupyter Notebook, or any Python environment

Steps to Install & Run the Project
1. Install Python

Download & install Python 3.x from python.org.

2. Install Required Library

Open terminal/command prompt and run:

pip install matplotlib

3. Save the Python file

Save the provided code as:

tds_monitor.py

4. Run the Program

Use terminal / cmd:

python tds_monitor.py

Instructions for Testing

Start the program → Enter number of hostel blocks

Choose from the menu:

Option 1 → Enter TDS values for all blocks

Option 2 → Update TDS of a specific block

Option 3 → Remove a block’s TDS entry

Option 4 → View all entries

Option 5 → Exit

Option 6 → See LIVE updating graph
