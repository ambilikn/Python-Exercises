#School administration application - read input data
import csv

def write_into_csv(info_test):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() ==0:
            writer.writerow(['Name','Age','Contact_number','Email-ID'])

        writer.writerow(info_test)

if __name__ == '__main__':

    condition = True
    student_num = 1

    while condition:
        student_info = input("Enter student information for student number {} in the following format: (Name Age Contact_number E-mail_Id)".format(student_num))
        print("Entered infomration is " + student_info)

        student_info_list = student_info.split(' ')

        print("\nThe entered information is\n Name :{}\n Age: {}\n Contact_number: {}\n Email-ID: {}\n"
            .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        choice_check = input("Is the entered information correct? (yes/no)")

        if choice_check == "yes":
            write_into_csv(student_info_list)
            condition_check = input("Enter (yes/no) if you wish to enter details of more students: ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("Please re-enter the values!")
