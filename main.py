import os
import time
import pyautogui
import pytesseract
import pyperclip
import dotenv


dotenv.load_dotenv()
user_code = os.getenv("USERCODE")
password = os.getenv("PASSWORD")
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/TesseractOCR/tesseract.exe"

delay = 3
print("Starting in " + str(delay) + " seconds")
time.sleep(delay)


def pos_loop():
    while True:
        x, y = pyautogui.position()
        print(x, y)
        time.sleep(1.5)


def copy_clipboard():
    pyperclip.copy("")
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(.01)
    return pyperclip.paste()


def click_at_with_delay(x_pos=0, y_pos=0, click_delay=0.5):
    pyautogui.moveTo(x_pos, y_pos)
    pyautogui.click()
    time.sleep(click_delay)


def login_logout_test():
    # click_at_with_delay(300, 450) # PC size
    click_at_with_delay(400, 335)
    pyautogui.write(user_code)
    time.sleep(0.5)

    # click_at_with_delay(300, 530) # PC size
    click_at_with_delay(400, 415)
    pyautogui.write(password)
    time.sleep(0.5)

    # click_at_with_delay(400, 670) # PC size
    click_at_with_delay(400, 555)
    # click_at_with_delay(350, 710) # PC size
    click_at_with_delay(220, 640)
    time.sleep(5)

    logged_screenshot = pyautogui.screenshot()
    # click_at_with_delay(1770, 100) # PC size
    click_at_with_delay(1240, 130)

    # click_at_with_delay(1800, 320, 3) # PC size
    click_at_with_delay(1260, 350, 3)

    pyautogui.press("F5")
    refresh_screenshot = pyautogui.screenshot()
    if list(logged_screenshot.getdata()) != list(refresh_screenshot.getdata()):
        print("Logout Test Successful")
    else:
        print("Logout Test Failed")
    time.sleep(2)


def secure_connection_test():
    # click_at_with_delay(160, 50) # PC size
    click_at_with_delay(194, 50)
    ssl_screenshot = pyautogui.screenshot("test.png", region=(150, 118, 156, 34))
    ssl_screenshot_string = pytesseract.image_to_string(ssl_screenshot)
    if "Connection is secure" in ssl_screenshot_string:
        print("Secure Connection Test Successful")
    else:
        print("Secure Connection Test Failed")
    time.sleep(2)


def password_field_test():
    # click_at_with_delay(300, 530) # PC password field
    # click_at_with_delay(400, 335) # Laptop usercode field
    click_at_with_delay(400, 415)   # Laptop password field
    pyautogui.write("123")
    time.sleep(0.5)

    # pyautogui.doubleClick((300, 530)) # PC password field
    # pyautogui.doubleClick((400, 335)) # Laptop usercode field
    pyautogui.doubleClick((400, 415))   # Laptop password field

    password_field_list = []
    var = copy_clipboard()
    password_field_list.append(var)
    if password_field_list[0] == '':
        print("Password Field Test Successful")
    else:
        print("Password Field Test Failed")
    time.sleep(2)


login_logout_test()
secure_connection_test()
password_field_test()
# pos_loop()
