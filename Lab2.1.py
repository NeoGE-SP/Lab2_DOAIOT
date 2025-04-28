import math

def display_main_menu():
    print("Enter a list of numbers, separated by a comma to represent the temperatures: ")

def get_user_input(temp_list):
    values = temp_list.split(',')
    for i in range(len(values)):
        values[i] = float(values[i])
        print("Temperature ", i+1, ": ", values[i])
    return values

def calc_average(temps):
    total = 0.0
    for i in range(len(temps)):
        total += temps[i]
    average = total/len(temps)
    return average

def find_min_max(temps):
    min = 10000000000000
    max = 0
    for i in range(len(temps)):
        if temps[i] < min:
            min = temps[i]
        elif temps[i] > max:
            max = temps[i]
    print("The Maximum Temperature is:", max, "\nThe Minimum Temperature is:", min)


def sort_temperature(temps):
    temps.sort()        
    return temps


def cal_median_temp(temps):
    pos = (len(temps)-1)/2
    median = 0
    if pos%2 == 0:
        median = temps[int(pos)]
    else:
        median = (temps[int(pos)] + temps[int(pos)+1])/2
    
    return median








def main():
    display_main_menu()
    temp_list = input("")
    temps = get_user_input(temp_list)
    print("The average temperature is:", calc_average(temps))
    find_min_max(temps)
    print("The sorted list of temperatures is:", sort_temperature(temps))
    print("The median is:", cal_median_temp(temps))
    




if __name__ == "__main__":
    main()