def main():
    info_dict = {
        "full_name": "Carter Tomlenovich",
        "student_id": 123456,
        "pizza_toppings": [
            "BLACK_OLIVES",
            "PEPPERONI",
            "BACON"
        ],
        "movies": [
            { "title": "Terminator 3: Rise of the Machines", "genre": "sci-fi"},
            { "title": "Spiderman 2", "genre": "action"}
        ]
    }

    info_dict["movies"].append( { "title": "Interstellar", "genre": "sci-fi" })

    print_pizza_toppings(info_dict)
    add_pizza_topping(info_dict, ["cheese", "green peppers"])
    print_pizza_toppings(info_dict)

    print(info_dict)
    
    return


def print_student_info(dict):
    full_name = dict["full_name"]
    first_name = full_name.split()[0]
    student_id = dict["student_id"]

    print("My name is {0}, but you can call me Sir {1}. \nMy student ID is {2}.".format(full_name, first_name, student_id))

def add_pizza_topping(dict, new_toppings):

    for topping in new_toppings:
        dict["pizza_toppings"].append(topping.lower())

    for i, topping in enumerate(dict["pizza_toppings"]):
        dict["pizza_toppings"][i] = topping.lower()

    dict["pizza_toppings"].sort()


def print_pizza_toppings(dict):
    print("My favorite pizza toppings are: \n")

    for topping in dict["pizza_toppings"]:
        print("- {0}".format(topping))

if __name__ == "__main__":
    main()