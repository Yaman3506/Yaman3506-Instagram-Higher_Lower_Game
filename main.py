from game_data import data
import random
from art import logo
from art import vs
import os

def compare(chosen_directory,other_directory):
    if chosen_directory["follower_count"] > other_directory["follower_count"]:
        return True
    return False

def print_info_A(page):
    name = page["name"]
    des = page["description"]
    country = page["country"]
    print(f"Compare A: {name}, {des}, from {country}.")

def print_info_B(page):
    name = page["name"]
    des = page["description"]
    country = page["country"]
    print(f"Compare B: {name}, {des}, from {country}.")

def game():

    score = 0
    game_on = 1
    B = random.choice(data)

    print(logo)
    while game_on:

        A = B
        B = random.choice(data)
        while B == A:
            B = random.choice(data)

        print_info_A(A)
        print(vs)
        print_info_B(B)
        decision = input("Who has more followers? Type 'A' or 'B':")

        if decision == "A":
            answer = compare(A,B)
        else:
            answer = compare(B,A)

        print("\n" * 50)

        if not answer:
            game_on = 0
            print(f"Sorry, that's wrong. Final score: {score}")
        else:
            score+= 1
            print(f"You're right! Current score: {score}.")

game()
