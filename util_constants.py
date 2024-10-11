version = 0.3

fname_input = "input first name: "
lname_input = "input last name: "
name_input = "input name: "

time_change_int_DEFAULT = 40
time_change_int = time_change_int_DEFAULT
devmode = False

def change_timeChangeInt(newvalue):
    time_change_int = newvalue or time_change_int_DEFAULT