def get_menu_choice():
    def print_menu():       
        print(30 * "-", "Bird Migration", 30 * "-")
        print("1. Latitude and Longitude ")
        print("2. 2D Speed Vs Frequency ")
        print("3. Time and Date ")
        print("4. Daily Mean Speed ")
        print("5. Cartographic View ")
        print("6. Exit from the script ")
        print(73 * "-")

    loop = True
    int_choice = -1

    while loop:          
        print_menu()    
        choice = input("Enter your choice [1-6]: ")

        if choice == '1':
            exec(open('BirdMigrationLatLong.py').read())
            loop = True
        elif choice == '2':
            exec(open('BirdMigrationDateTime.py').read())
            loop = True

        elif choice == '3':
            exec(open('BirdMigration2DSpeed.py').read())
            loop = True

        elif choice == '4':
            exec(open('BirdMigrationDailyMeanSpeed.py').read())
            loop = True

        elif choice == '5':
            exec(open('BirdMigrationMapView.py').read())
            loop = True
            
        elif choice == '6':
            int_choice = -1
            print("Exiting..")
            loop = False  
        else:
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]


print(get_menu_choice())
