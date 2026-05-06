
#D00290718 - Samuel Delaney
#Y1 System Testing & CI Final Practical

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time, pytest, os
from selenium.webdriver.common.by import By

url = "http://127.0.0.1:5000/"
filename = "timetable.txt"

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService('chromedriver.exe'))
    driver.get("http://127.0.0.1:5000/")
    time.sleep(1) #Wait for the web page to load fully.
    return driver


#Part 1 – Basics 5 marks

#PART A:

def test_page_title(driver):
    #a. Page title – Student Timetable
    title = driver.title
    assert title == "Student Timetable"

#PART B:

def test_header_text(driver):
    #b. Header text – Student Timetable Viewer
    header = driver.find_element(By.XPATH, '//*[@id="title1"]')
    header = header.text
    assert header == "Student Timetable Viewer"

#PART C:

def test_label_text(driver):
    #c. Label text - Enter timetable filename (e.g., timetable.txt):
    label = driver.find_element(By.XPATH, '//*[@id="label1"]')
    label = label.text
    assert label == "Enter timetable filename (e.g., timetable.txt):"

#PART D:

def test_footer_copyright(driver):
    #d. Footer copyright
    footer = driver.find_element(By.XPATH, '//*[@id="copy"]')
    footer = footer.text
    assert footer == "© Peter Gosling 2026 Student Timetable Viewer. All rights reserved."

#PART E:

def test_logo_alt(driver):
    #e. Logo ALT text
    logo_alt = driver.find_element(By.ID, 'logo')
    logo_alt = logo_alt.get_attribute("alt")
    assert logo_alt == "DkIT current Logo"


#Part 2 – Advance 10 marks

#PART F: AND PART G:

def test_load_timetable(driver):
    #f. Load the timetable.txt file
    #AND
    #g. Table exists
    type_intoBox = driver.find_element(By.ID, "filename")
    type_intoBox.send_keys("timetable.txt")
    click_next = driver.find_element(By.ID, "submit-btn")
    click_next.click()
    time.sleep(1) #wait for the web page to load after submitting the text file to be read.
    assert driver.find_element(By.TAG_NAME, "table")


#PART H:

def test_table_head_and_colour(driver):
    #h. Table head text and colour

    #Load TXT data into the web page first obviously.

    type_intoBox = driver.find_element(By.ID, "filename")
    type_intoBox.send_keys("timetable.txt")
    click_next = driver.find_element(By.ID, "submit-btn")
    click_next.click()
    time.sleep(1) #wait for the web page to load after submitting the text file to be read.

    #Next:

    wanted_output = ["rgba(144, 144, 144, 1)", "Subject", "Time", "Room"]
    new_output = []
    #step 1
    bg_colour = driver.find_element(By.XPATH, '//*[@id="container"]/main/table/thead/tr')
    bg_colour = bg_colour.value_of_css_property("background-color")
    new_output.append(bg_colour)
    #step 2
    col1 = driver.find_element(By.XPATH, '//*[@id="container"]/main/table/thead/tr/th[1]')
    col1 = col1.text
    new_output.append(col1)
    #step 3
    col2 = driver.find_element(By.XPATH, '//*[@id="container"]/main/table/thead/tr/th[2]')
    col2 = col2.text
    new_output.append(col2)
    #step 4
    col3 = driver.find_element(By.XPATH, '//*[@id="container"]/main/table/thead/tr/th[3]')
    col3 = col3.text
    new_output.append(col3)
    #now check if matches
    #print(wanted_output)
    #print("\n\n")
    #print(new_output)
    assert wanted_output == new_output


#PART I :



#PART J:



