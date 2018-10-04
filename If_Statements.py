
is_Male = False
is_Tall = True

if is_Male and is_Tall:
    print("You are a tall male.")
elif is_Male and not(is_Tall):
        print("You are a short male")
elif not(is_Male) and is_Tall:
        print("You are not a male but are tall")

else:
    print("You are either not male nor not tall ")