
def Handle_Selection(selection):
    File = open('LocalDATA\\OptionSelected_Availability.txt', 'w')
    File.write(selection+"\n")