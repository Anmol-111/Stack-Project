import Bussiness_Entities.EMP_Entities as Bent
import Bussiness_Access_Layer.EMP_Bal as Bal

obj_ent = Bent.Emp_Entities()
obj_bal = Bal.Emp_Bal()

option = "yes"
while option.lower() == "yes":
    print("\nCRUD OPERATIONS:")
    print("1. Insert Employee Data")
    print("2. Retrieve Employee Data")
    print("3. Update Employee Data")
    print("4. Delete Employee Data")
    choice = int(input("Enter the choice (1-4): "))

    if choice == 1:
        name = input("Enter the EMP_NAME: ")
        age = int(input("Enter the AGE: "))
        salary = float(input("Enter the SALARY: "))
        designation = input("Enter the DESIGNATION: ")

        id = obj_bal.auto_emp_id()
        obj_ent.set_emp_id(id)
        obj_ent.set_name(name)
        obj_ent.set_age(age)
        obj_ent.set_salary(salary)
        obj_ent.set_designation(designation)

        choice1 = input("Do you want to push the data in the main server?: ").lower()
        if choice1 == "yes":
            obj_bal.emp_insert_data(obj_ent)
            print("INSERTION OF DATA SUCCESSFULLY.")
        else:
            print("INSERTION OF DATA UNSUCCESSFULLY.")

    elif choice == 2:
        data = obj_bal.emp_retrieve_all_data()
        for counter in data:
            print(counter)

    elif choice == 3:
        emp_id = int(input("Enter EMP_ID to update: "))
        updated_name = input("Enter new name: ")
        updated_age = int(input("Enter new age: "))
        updated_salary = float(input("Enter new salary: "))
        updated_designation = input("Enter new designation: ")

        obj_ent.set_emp_id(emp_id)
        obj_ent.set_name(updated_name)
        obj_ent.set_age(updated_age)
        obj_ent.set_salary(updated_salary)
        obj_ent.set_designation(updated_designation)
    
        obj_bal.emp_update_data(obj_ent)

    elif choice == 4:
        emp_id = int(input("Enter EMP_ID to delete: "))
        result = obj_bal.emp_delete_id_data(emp_id)
        print(result)

    option = input("Do you want to perform another operation? (yes/no): ").lower()

