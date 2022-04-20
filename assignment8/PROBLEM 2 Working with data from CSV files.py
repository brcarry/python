import csv

def BMI_calculator(min_age, max_age):
    with open('patient_data.csv', 'r') as f:
        lines = csv.reader(f)
        next(lines) # 跳过表头
        cnt = 0
        sum_BMI = 0
        for line in lines:
            if min_age <= int(line[2]) <= max_age:
                cnt += 1
                sum_BMI += int(line[4])/(int(line[3])*int(line[3]))*703
        return sum_BMI/cnt

while True:
    try:
        min_age = int(input("Please input min age: "))
        max_age = int(input("Please input max age: "))
        print(BMI_calculator(min_age, max_age))
    except:
        print("You enter an age younger than or older than those on the patient list.")
        print("Please input another age range")
    else:
        break
