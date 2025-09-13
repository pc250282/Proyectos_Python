excercises = []

def add_excersice():
    excersice = {'name':'',
                 'sets_number':0,
                 'reps_number':0,
                 'weight':0.0
                 }
    
    while True:
        try:
            name = str(input('Enter excercise name: ').strip())
            if any(ex['name'].lower() == name.lower() for ex in excercises):
                print('that exercise already exists')
                continue
            excersice['name'] = name.capitalize()
            excersice['sets_number'] = int(input('Enter number of sets: '))
            excersice['reps_number'] = int(input('Enter number of reps: '))
            excersice['weight'] = float(input("Enter weight in kg: "))
            break
        except ValueError as e:
            print('error in the data. retry')
    
    return excersice
        
            

def log_workout():
    for excercise in excercises:
        print('---------------------------------')
        print(f"Excercise: {excercise['name']}")
        print(f"Sets: {excercise['sets_number']}")
        print(f"Repets: {excercise['reps_number']}")
        print(f"Weight: {excercise['weight']} Kg")
        print('---------------------------------')
    
def main_menu():
    while True:
        print("🏋️‍♂️ Gym Tracker 🏋️‍♂️")
        print("\t1- Add Exercise")
        print("\t2- Log workout")
        print("\t3- View Progress")
        print("\t4- Exit")
        option = input("Choose an option \n")
        match option:
            case "1":
                excercises.append(add_excersice())
                print('Excersise created')
            case "2":
                log_workout()
            case "3":
                pass
            case "4":
                break
            case _:
                continue   
if __name__ == "__main__":
    main_menu()