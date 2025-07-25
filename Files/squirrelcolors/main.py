import pandas

# TODO: Read CSV File
squirrel_data = pandas.read_csv("./squirrel_data.csv")

# TODO: Get the Primary Fur Color column
fur_color_column = squirrel_data["Primary Fur Color"]

# TODO: Rows in the column where the Primary Fur Color == Gray, Cinnamon, Black
# this does not return the data, it returns True or False for each row
grey = fur_color_column == "Gray"# does the row contain gray in the Primary Fur Color the column
red = fur_color_column == "Cinnamon"
black = fur_color_column == "Black"
# print(grey)
# TODO: Get all the rows that contain gray, red, cinnamon squirrels
# this returns the actual data, treated like a list
grey_squirrels_data = squirrel_data[grey]# returns the rows where gray equals TRUE
red_squirrels_data = squirrel_data[red]
black_squirrels_data = squirrel_data[black]
# print(grey_squirrels_data)

# TODO: Get count of squirrels for each color
grey_squirrels_count = len(grey_squirrels_data)
red_squirrels_count = len(red_squirrels_data)
black_squirrels_count = len(black_squirrels_data)
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)


# # TODO: Create a Dictionary
squirrel_colors_count = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
# # TODO: Create a Data Frame
fur_color_count_data = pandas.DataFrame(squirrel_colors_count)
print(fur_color_count_data)
#
# # TODO: Convert Data to CSV File
# fur_color_count_data.to_csv("squirrel_count.csv")

#read csv
fur_color_data = pandas.read_csv("./squirrel_count.csv")
print(fur_color_data)


# #My Solution*************************************************************************
# # TODO: Read CSV File
# squirrel_data = pandas.read_csv("./squirrel_data.csv")
# # TODO: Get the Primary Fur Color column
# fur_color_column = squirrel_data["Primary Fur Color"]

# # TODO: Convert Series to a list
# squirrel_color_list = fur_color_column.to_list()


# grey_list = []
# cinnamon_list = []
# black_list = []
# # TODO:Loop through the list and add each color to its color list
# for color in squirrel_color_list:
#     if color == "Gray":
#         grey_list.append(color)
#     if color == "Cinnamon":
#         cinnamon_list.append(color)
#     if color == "Black":
#         black_list.append(color)

# # TODO:Remove duplicates from the List
# colors_list = list(dict.fromkeys(squirrel_color_list))

# colors_list.pop(0)# remove nan from the list
# colors_list[0] = "Grey"# replace Gray with Grey
# print(f"Colors List:  {colors_list}")

# # TODO: Count the number of items in each colors list
# grey_count = len(grey_list)
# cinnamon_count = len(cinnamon_list)
# black_count = len(black_list)

# # TODO: Create a list from the color counts
# colors_count = [grey_count, cinnamon_count, black_count]

# # print(f"Colors Count {colors_count}")


# # TODO: Create a Dictionary
# squirrel_colors_count = {
#     "Fur Color": colors_list,
#     "Count": colors_count
# }
# # TODO: Create a Data Frame
# fur_color_count_data = pandas.DataFrame(squirrel_colors_count)
# # print(fur_color_count_data)

# # TODO: Convert Data to CSV File
# # fur_color_count_data.to_csv("squirrel_count2.csv")

# #read csv
# fur_color_data = pandas.read_csv("./squirrel_count2.csv")
# print(fur_color_data)

