Schaltjahr = int(input("Zu Überprüfendes Jahr: "))

if Schaltjahr % 4 or Schaltjahr % 400 == 0:
    print("Schaltjahr")
else:
    print("kein Schaltjahr")
