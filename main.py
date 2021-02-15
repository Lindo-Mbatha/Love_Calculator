print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
results1 = lower_case_name1.count("t")
results2 = lower_case_name1.count("r")
results3 = lower_case_name1.count("u")
results4 = lower_case_name1.count("e")

lower_case_name2 = name2.lower()
results5 = lower_case_name2.count("t")
results6 = lower_case_name2.count("r")
results7 = lower_case_name2.count("u")
results8 = lower_case_name2.count("e")

lower_case_name1 = name1.lower()
results9 = lower_case_name1.count("l")
results10 = lower_case_name1.count("o")
results11 = lower_case_name1.count("v")
results12 = lower_case_name1.count("e")

lower_case_name2 = name2.lower()
results13 = lower_case_name2.count("l")
results14 = lower_case_name2.count("o")
results15 = lower_case_name2.count("v")
results16 = lower_case_name2.count("e")

final_results_for_true = results1 + results2 + results3 + results4 + results5 + results6 + results7 + results8

final_results_for_love = results9 + results10 + results11 + results12 + results13 + results14 + results15 + results16

final_results = int(f"{final_results_for_true}{final_results_for_love}")

if final_results < 10 or final_results > 90:
  print(f"Your score is {final_results}, you go together like coke and mentos")
elif final_results >= 40 and final_results <= 50:
  print(f"Your score is {final_results}, you are alright together")
else:
  print(f"Your score is {final_results}%")