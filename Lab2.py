print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    arraylist = []
    print("get_user_input")
    inputstr=input()
    numlist = inputstr.split(",")
    print(numlist)

    for eachnum in numlist:
        arraylist.append(float(eachnum))
    print(arraylist)
    return arraylist

def calc_average(arraylist):
    print("calc_average")
    total = sum(arraylist)
    average = total / len(arraylist)
    print("Average = ", f"{average: .2f}")
    return round(average, 2)

def find_min_max(arraylist):
    print("find_min_max")
    templist = sort_temperature(arraylist)
    min = templist[0]
    max = templist[-1]
    print("MIN = " +str(min) + " and MAX = " + str(max))
    return [min, max]

def sort_temperature(arraylist):
    print("sort_temperature")
    templist = arraylist.copy()
    templist.sort()
    print("Sorted Numbers = ", templist)
    return templist

def calc_median_temperature(numlist):
    print("calc_median_temperature")
    templist = sort_temperature(numlist)
    numcount = len(templist)
    if numcount % 2 ==1:
        median = templist[numcount//2]
    else:
        median = (templist[numcount//2-1] + templist[numcount//2])/2
    print("MEDIAN = ", median)
    return median

def main(): 
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu() 
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    calc_median_temperature(num_list)
    


if __name__ == "__main__":
    main() 