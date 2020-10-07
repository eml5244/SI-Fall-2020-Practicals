import arrays
import random
import turtle

"""
File Reading

You have been given a file called "pokemon.csv". Your job is to use the file to print the name of the Pokemon of the given type that has the highest stat of the given stat type.
For example, find_highest_stat("Fire", "HP") should print "The Fire pokemon with the most HP is Emboar".
"""
def find_highest_stat(a_type, stat):
    return None

"""
Arrays

Write a function that, given an array, creates another array called "squares" that holds the values of the original array, squared.
Then return the equivalent of the original array concatenated with squares. (Hint: you will need to create another array to do this!)
"""
def square_elements(an_array):
    return None

"""
Lists

Write a function that, given a filename and a letter, prints out the elements that start with the given letter. You must use a list at some point in your function!
If no element is found, print "No element starts with the letter <letter>"
"""
def find_elements(filename, letter):
    return None

"""
Recursion

First, write a function that draws a square given a length.
Next, write a function that recrusively draws smaller squares in each corner of the square given a length and a depth.
"""
def draw_square(length):
    return None

def draw_squares_rec(length, depth):
    return None

"""
Sorting

You will be implementing a new sorting algorithm called tri_merge_sort, a 3-array version of merge sort. You must use lists to do this.
You have been provided two functions, merge and merge_helper, to assist you. It is your job to implement a splitting function and the tri_merge_sort function.
"""
def merge_helper(result_list, list1, list2, list3):
    if len(list1) == 0:
        while len(list2) != 0 and len(list3) != 0:
            if list2[0] < list3[0]:
                result_list.append(list2[0])
                list2.pop(0)
            else:
                result_list.append(list3[0])
                list3.pop(0)

def merge(list1, list2, list3):
    result_list = [] 
    list_of_lists = [[list1, list2, list3], [list2, list1, list3], [list3, list1, list2]]
    while len(list1) != 0 and len(list2) != 0 and len(list3) != 0:
        if list1[0] < list2[0] and list1[0] < list3[0]:
            result_list.append(list1[0])
            list1.pop(0)
        elif list2[0] < list1[0] and list2[0] < list3[0]:
            result_list.append(list2[0])
            list2.pop(0)
        else:
            result_list.append(list3[0])
            list3.pop(0)
    for a_list in list_of_lists:
        merge_helper(result_list, a_list[0], a_list[1], a_list[2])
    for a_list in list_of_lists:
        if len(a_list[0]) != 0:
            result_list += a_list[0]
    return result_list   

def split_3(a_list):
    return None

def tri_merge_sort(a_list):
    return None