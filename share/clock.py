from datetime import *
from dothat import lcd, backlight, touch
from time import sleep
import signal
import sys

clock_on = 1    # Used to determine interupt status.
color_choice = 0

colors = [
  {'name' : 'Green', 'combo' : (0, 255, 0)},
  {'name' : 'Gold', 'combo' : (244, 217, 65)},
  {'name' : 'White', 'combo' : (255, 255, 255)},
  {'name' : 'Red', 'combo' : (255, 0, 0)},
  {'name' : 'Yellow', 'combo' : (255, 255, 0)},
  {'name' : 'Blue', 'combo' : (0, 0, 255)},
  {'name' : 'Magenta', 'combo' : (255, 0, 255)},
  {'name' : 'Aqua', 'combo' : (0, 255, 255)},
  {'name' : 'Purple', 'combo' : (131, 66, 244)},
  {'name' : 'Indiglo', 'combo' : (0, 66, 33)}
]

lcd.set_contrast(51)

lcd.create_char(0, [0,14,10,10,10,10,14,0])
lcd.create_char(1, [0,14,14,14,14,14,14,0])

months_abbr = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
trailing_zeros = [
  '00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
  '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
  '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
  '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
  '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
  '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
]

separator = [
  ':', ' ', ':', ' ', ':', ' ', ':', ' ', ':', ' ',
  ':', ' ', ':', ' ', ':', ' ', ':', ' ', ':', ' ',
  ':', ' ', ':', ' ', ':', ' ', ':', ' ', ':', ' ',
  ':', ' ', ':', ' ', ':', ' ', ':', ' ', ':', ' ',
  ':', ' ', ':', ' ', ':', ' ', ':', ' ', ':', ' ',
  ':', ' ', ':', ' ', ':', ' ', ':', ' ', ':', ' ',
]

hours = ["12", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]
tod = ['am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm']

def current_time():
  time = datetime.now()
  hour = time.hour
  minute = time.minute
  second = time.second
  year = time.year
  day = time.day
  month = time.month
  bin_clock_s = bin(second)
  bin_clock_s = bin_clock_s[2:]
  bin_clock_s = '000000' + bin_clock_s
  bin_clock_s = bin_clock_s[len(bin_clock_s)-6:len(bin_clock_s)]
  bin_clock_s = chr(int(bin_clock_s[0]))+chr(int(bin_clock_s[1]))+chr(int(bin_clock_s[2]))+chr(int(bin_clock_s[3]))+chr(int(bin_clock_s[4]))+chr(int(bin_clock_s[5]))
  return { 'tod' : tod[hour], 'hour' : hours[hour], 'minute' : trailing_zeros[minute], 'second' : trailing_zeros[second], 'month' : months_abbr[month], 'day' : trailing_zeros[day], 'year' : str(year), 'sep' : separator[second], 'bcs' : bin_clock_s }

@touch.on(touch.BUTTON)
def touch_button(channel, event):
  backlight.rgb(*colors[color_choice%len(colors)]['combo'])
  sleep(2)
  backlight.off()

@touch.on(touch.RIGHT)
def pick_color_p(channel, event):
  global color_choice
  color_choice += 1
  print "Selected combo: " + colors[color_choice%len(colors)]['name']

@touch.on(touch.LEFT)
def pick_color_m(channel, event):
  global color_choice
  color_choice -= 1
  print "Selected combo: " + colors[color_choice%len(colors)]['name']

def clean_up(signal, frame):
  global clock_on
  print "Stopping clock..."
  clock_on = 0
  lcd.set_display_mode(enable=False)
  lcd.clear()
  backlight.off()
  print "Goodbye!"

def info(signal, frame):
  print current_time()

signal.signal(signal.SIGINT, clean_up)
signal.signal(signal.SIGQUIT, clean_up)
signal.signal(signal.SIGTSTP, clean_up)
# signal.signal(signal.SIGSTOP, clean_up)
# signal.signal(signal.SIGINF, info)

print "Started LCD Clock by Joseph Geis."
print "Press Ctrl-C, Ctrl-\\ or Ctrl-Z to stop.\n"

while clock_on:
  time = current_time()
  lcd.set_cursor_position(4,0)
  lcd.write(time['hour'] + time['sep'] + time['minute'] + ' ' + time['tod'])
  lcd.set_cursor_position(5,1)
  lcd.write(time['bcs'])
  lcd.set_cursor_position(2,2)
  lcd.write(time['month'] + ' ' + time['day'] + ', ' + time['year'])