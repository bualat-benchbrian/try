import os

class BenchInfo:
    def __init__ (self, name, overview, goal, traits, crush):
        self.name = name
        self.overview = overview
        self.goal = goal
        self.traits = traits
        self.crush = crush

    def show_name(self):
        os.system('cls')
        print(f"Name: {self.name}")

    def show_overview(self):
        os.system('cls')
        print(f"Overview: {self.overview}")

    def show_goal(self):
        os.system('cls')
        print(f"Goal: {self.goal}")

    def show_traits(self):
        os.system('cls')
        print("Traits:")
        for trait in self.traits:
            print(f"- {trait}")

    def show_crush(self):
        os.system('cls')
        print(f"Crush: {self.crush}")

    def menu(self):
        CHOICE_SHOW_NAME = '1'
        CHOICE_SHOW_OVERVIEW = '2'
        CHOICE_SHOW_GOAL = '3'
        CHOICE_SHOW_TRAITS = '4'
        CHOICE_SHOW_CRUSH = '5'
        CHOICE_EXIT = '6'
        
        while True:
            os.system('cls')
            print(f"Menu for {self.name}:")
            print("1. Name")
            print("2. Overview")
            print("3. Goal")
            print("4. Traits")
            print("5. Crush")
            print("6. Exit")

            user_choice = input("Please enter your choice: ")
            
            if user_choice == CHOICE_EXIT:
                print("Exiting the menu. Goodbye!")
                break
            elif user_choice == CHOICE_SHOW_NAME:
                self.show_name()
            elif user_choice == CHOICE_SHOW_OVERVIEW:
                self.show_overview()
            elif user_choice == CHOICE_SHOW_GOAL:
                self.show_goal()
            elif user_choice == CHOICE_SHOW_TRAITS:
                self.show_traits()
            elif user_choice == CHOICE_SHOW_CRUSH:
                self.show_crush()
            else:
                print("Invalid choice, please try again.")

            input("\nPress Enter to continue...")

bench = BenchInfo(
    name = "Bench Brian Bualat",
    overview = (
        "I like to play online games and watch movies. "
        "I don't have a girlfriend in my entire life. " 
        "But I have a family and friends who love and support me. " 
        "I am a simple person who enjoys the little things in life."
    ),
    goal = (
        "To be rich, but also to be happy and content with what I have."
        "Provide everything for my family and friends."
    ),
    traits = ["Cruel", "Chaotic", "Friendly", "Loyal", "Simple"],
    crush = "Nini <3"
)

bench.menu()