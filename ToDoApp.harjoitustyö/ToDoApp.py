#Tekijä: Hamza Alshaheen 
#Kurssi: Ohjelmoinnin perusteet TT00CD77-3008
#Harjoitustyön nimi: To do list app  
#Päivämäärä: 10.12.2024

#________lyhyt kuvaus tehtävästä__________#

# To-Do-sovellus auttaa käyttäjää luomaan tehtäviä, tallentamaan niiden luomisajan ja hallitsemaan niitä helposti.
# Sovelluksen avulla voi lisätä, poistaa ja muokata olemassa olevia tehtäviä. Lisäksi käyttäjä voi etsiä tehtäviä tai merkitä niitä tehdyiksi.
# Sovellus on yksinkertainen, mutta sen avulla käyttäjä voi kätevästi luoda oman To-Do-listansa.

#Aika module 
from datetime import datetime 
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#addTask funktio kysy käyttäjältä uusia tehtäviä mitkä haluaa tallentaa
def addTask(tasks: list[str]) -> None:
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task ¨{task}¨ has been added to the list at {timestamp}.")

#deleteTask funktio poista tehtäviä
def deleteTask(tasks: list[str]) -> None:
    if not tasks:
        print("There are no tasks to delete.")
    else:
        listTasks(tasks)
        try:
            taskToDelete = int(input("Enter the number of the task to delete: "))
            if 1 <= taskToDelete <= len(tasks):
                removed_task = tasks.pop(taskToDelete - 1)
                print(f"Task ¨{removed_task}¨ has been removed.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#listTasks funktio listaa kaikki tallennetut tehtävät
def listTasks(tasks: list[str]) -> None:
    if not tasks:
        print("Currently, there are no tasks.")
    else:
        print("Your current tasks are:")
        for index, task in enumerate(tasks, start=1):
            print(f"Task.{index} {task} was add at ({timestamp})")

#ModifyTask funktio muokkaa olemassa olevia tehtäviä
def modifyTask(current_tasks: list[str])-> None:
    #if not koodi > tarkistaa jos listalla on tehtäviä.
    if not current_tasks:
        print("There are no current tasks.")
    else:
        listTasks(current_tasks)
        #Try except koodi varmistaa että käyttäjä antaa oikea syöte
        try:
            modify_task_num =int(input("what number of task do you want to modify?: "))
            if 1 <= modify_task_num <= len(current_tasks):
                new_modify_task = input("Enter the new task: ")
                current_tasks[modify_task_num -1]= new_modify_task
                print("Task was seccessfully modified.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#SearchTask funktion hakee tehtäviä, jonka käyttäjä haluaa tulosta.
def searchTasks(tasks: list[str])-> None:
    if not tasks:
        print("There are no tasks to search")
        return
   #Käyttäjän antama haku sana ilman välilyönti ja myös muokattu pienillä kirjäimillä strip ja lowerin avulla
    search = input("Serch tasks by name: ").strip().lower()
    found_tasks = [task for task in tasks if search in task.lower()] #Tämä koodi tarkistaa onko käyttäjän antama sana on listassa/tehtävissä
    if found_tasks:
        print("Matching found")
        for index, task in enumerate(found_tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No matches were found.")

    #funktio markAsCompleted merkkaa tehtävä tehdyksi 
def markAsCompleted(unmarkedTasks: list[str], completedTasks: list[str])-> None:
    if not unmarkedTasks:
        print("There are no tasks right now.")
    else:
        listTasks(unmarkedTasks)
        try:
            taskToMark = int(input("What task do you want to mark as completed?: "))
            
            #Tarkistaa ensin käyttäjän syöte
            if 1 <= taskToMark <= len(unmarkedTasks):
                #Poista vanhan tehtävän ja Siirtää Completed tehtävä uuden listan. 
                task = unmarkedTasks.pop(taskToMark - 1)
                completedTasks.append(task)
                print(f"Task '{task}' has been marked as completed.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("You entered an invalid value. Please try again.")


#main funktiolla suoritetaan koodi
def main():
    #Tervetuloa appille
    print("Welcome to the to-do list app!\n")
    tasks = []
    completedTasks = []
    #Silmukka kysyy käyttäjältä valitsemaan vaihtoehdoista yhden vaihtoehto
    
    while True:
        print(
            """Please select one of the following options:
---------------------
1. Add a new task
2. Delete a task
3. List tasks
4. Modify tasks
5. search task
6. Mark tasks as completed
7. Quit"""
        )
        #Käyttäjän valinta
        choice = input("Enter your choice: ")
        #Jos valinta olisi 1 kutsu addTask funktio
        if choice == "1":
            addTask(tasks)
        #Tai valine olisi 2 kutsu deleteTask funktio
        elif choice == "2":
            deleteTask(tasks)
        #Tai valine olisi 3 kutsu listTask funktio   
        elif choice == "3":
            listTasks(tasks)
        #Tai valine olisi 4 kutsu modifyTask funktio 
        elif choice == "4":
            modifyTask(tasks)
        #Tai valine olisi 5 kutsu searchTask funktio 
        elif choice == "5":
            searchTasks(tasks)
        elif choice == "6":
            markAsCompleted(tasks, completedTasks)
        #Ja jos valinta olisi 6 niin ohjelma päättyy break silmukka 
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            #Jos syöte ei ole kelvollinen ohjelma printtaa tämä.
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
