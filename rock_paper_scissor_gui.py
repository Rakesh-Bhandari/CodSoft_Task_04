import customtkinter as tk
import random

user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_message = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    result_label.configure(text=result_message)
    update_scoreboard()

def update_scoreboard():
    user_score_label.configure(text=f"User: {user_score}")
    computer_score_label.configure(text=f"Computer: {computer_score}")
    
def reset_score():
    result_message = f""
    result_label.configure(text=result_message)
    global user_score, computer_score
    user_score*=0
    computer_score*=0
    update_scoreboard()

window = tk.CTk()
window.title("Rock Paper Scissors")
window.geometry("600x400")
window.config(bg='#5c8ab6')
window.resizable(width='false',height='false')

Title=tk.CTkLabel(window,bg_color='#09112e',width=600,height=65,text='')
Title.place(x=0,y=0)

label = tk.CTkLabel(window, text="Choose Rock, Paper, or Scissors:",font=("Arial", 30,'bold'),text_color='#fff',bg_color='#09112e')
label.place(x=60,y=20)



rock_button = tk.CTkButton(window, text="Rock",font=("Arial", 15,"bold"), width=80, height=40,fg_color='#09112e', command=lambda: play_game('rock'),corner_radius=5,bg_color='#5c8ab6')
rock_button.place(x=80,y=85)

paper_button = tk.CTkButton(window, text="Paper",font=("Arial", 15,"bold"), width=80, height=40, fg_color='#09112e', command=lambda: play_game('paper'),corner_radius=5,bg_color='#5c8ab6')
paper_button.place(x=200,y=85)

scissors_button = tk.CTkButton(window, text="Scissors",font=("Arial", 15,"bold"), width=80, height=40, fg_color='#09112e', command=lambda: play_game('scissors'),corner_radius=5,bg_color='#5c8ab6')
scissors_button.place(x=320,y=85)

reset_button=tk.CTkButton(window,command=reset_score,font=("Arial", 15,"bold"),text='Reset',text_color='#fff',fg_color='#09112e',bg_color='#5c8ab6',corner_radius=5,width=80,height=40)
reset_button.place(x=440,y=85)

grid1=tk.CTkLabel(window,width=300,height=40,fg_color='#09112e',corner_radius=10,bg_color='#5c8ab6',text='')
grid1.place(x=160,y=145)

score_frame = tk.CTkLabel(window,width=300,height=50,text='',fg_color='#09112e')
score_frame.place(x=160,y=155)

user_score_label = tk.CTkLabel(score_frame, text="User: 0", font=("Arial", 18))
user_score_label.place(x=20,y=5)

computer_score_label = tk.CTkLabel(score_frame, text="Computer: 0", font=("Arial", 18))
computer_score_label.place(x=180,y=5)

grid2=tk.CTkLabel(window,width=300,height=40,fg_color='#fff',corner_radius=10,bg_color='#5c8ab6',text='')
grid2.place(x=160,y=345)

result_label = tk.CTkLabel(window, width=300,height=170,text="" ,font=("Times", 26,'bold'),fg_color='#fff',text_color='#000',bg_color='#fff')
result_label.place(x=160,y=195)

window.mainloop()