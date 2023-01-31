

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
            { 
                "title": "Terminator 3: Rise of the Machines", 
                "genre": "sci-fi"
            },
            { 
                "title": "Spiderman 2",
                "genre": "action"
            }
        ]
    }

    info_dict["movies"].append( { "title": "Split", "genre": "psychological" })

    print_student_info(info_dict)

    print_pizza_toppings(info_dict)
    add_pizza_topping(info_dict, ["cheese", "green peppers"])
    print_pizza_toppings(info_dict)

    print_movie_genres(info_dict)
    print_movie_titles(info_dict)
    
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
    print("\nMy favorite pizza toppings are: \n")

    for topping in dict["pizza_toppings"]:
        print("- {0}".format(topping))

def print_movie_genres(dict):
    movies = dict["movies"]
    genres = []

    for movie in movies:
        genres.append(movie["genre"])

    print("I like to watch ", end="")
    for i, g in enumerate(genres):
        if g == genres[-1]:
            print("and {0} movies.".format(g))
        else:
            print("{0}, ".format(g), end="")


def print_movie_titles(dict):
    movies = dict["movies"]
    titles = []

    for movie in movies:
        titles.append(movie["title"])

    print("\nSome of my favorite movies are ", end="")
    for i, t in enumerate(titles):
        if t == titles[-1]:
            print("and {0}!".format(t))
        else:
            print("{0}, ".format(t), end="")


if __name__ == "__main__":
    main()