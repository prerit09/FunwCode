import pywhatkit
to = input("Send To : ")
msg = input("Enter Message : ")
hour = int(input("Enter Hour : "))
minute = int(input("Enter Min : "))
pywhatkit.sendwhatmsg(to, msg, hour, minute)