class Person:
    def __init__(self, name, age, gender, phone, id_number, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.id_number = id_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Phone: {self.phone}, national ID: {self.id_number}, Email: {self.email}"

    def get_Specifications(self):
        return f"name: {self.name} age: {self.age} gender: {self.gender}"

    def update_phone(self, new_phone):
        self.phone = new_phone

    def update_email(self, new_email):
        self.email = new_email

    def contact_info(self):
        return f"phone: {self.phone} id number: {self.id_number} email: {self.email}"


class Doctor(Person):
    def __init__(self, name, age, gender, phone, id_number, email, employee_id, specialization, department):
        super().__init__(name, age, gender, phone, id_number, email)
        self.employee_id = employee_id
        self.specialization = specialization
        self.department = department
        self.patients = []

    def __str__(self):
        return f"[{super().__str__()},Employee Id: {self.employee_id} ,Specialization: {self.specialization}, Department: {self.department}]"

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)

    def get_patients(self):
        return f"your patients: {self.patients}"


class Nurse(Person):
    def __init__(self, name, age, gender, phone, id_number, email, employee_id, department, shift):
        super().__init__(name, age, gender, phone, id_number, email)
        self.employee_id = employee_id
        self.department = department
        self.shift = shift
        self.patients = []

    def __str__(self):
        return f"[{super().__str__()}, Employee Id: {self.employee_id}, Department: {self.department}, Shift: {self.shift}]"

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)

    def get_patients(self):
        return f"your patients: {self.patients}"

    def update_shift(self, new_shift):
        self.shift = new_shift

    def display_shift(self):
        return f"your shift time: {self.shift}"


class Patient(Person):
    def __init__(self, name, age, gender, phone, id_number, email, patient_id, disease, doctor, room):
        super().__init__(name, age, gender, phone, id_number, email)
        self.patient_id = patient_id
        self.disease = disease
        self.doctor = doctor
        self.room = room
        self.treatments = []

    def __str__(self):
        return f"[{super().__str__()}, patient_id: {self.patient_id}, Disease: {self.disease}, Doctor: {self.doctor}, Room: {self.room}]"

    def add_treatment(self, treatment):
        self.treatments.append(treatment)

    def remove_treatment(self, treatment):
        if treatment in self.treatments:
            self.treatments.remove(treatment)

    def get_treatments(self):
        return f"treatment is {self.treatments}"

    def update_room(self, new_room):
        self.room = new_room

    def get_room_info(self):
        return f"room number is: {self.room}"


class Department:
    def __init__(self, department_name, department_id, head_doctor, number_of_rooms):
        self.department_name = department_name
        self.department_id = department_id
        self.head_doctor = head_doctor
        self.number_of_rooms = number_of_rooms
        self.staffs = []

    def __str__(self):
        return f"[Department name: {self.department_name}, Department ID: {self.department_id}, Head Doctor: {self.head_doctor},number of Rooms: {self.number_of_rooms}]"

    def add_staff(self, staff):
        self.staffs.append(staff)

    def remove_staff(self, staff):
        if staff in self.staffs:
            self.staffs.remove(staff)

    def display_staff(self):
        return f"staff: {self.staffs}"

    def update_head_doctor(self, new_head_doctor):
        self.head_doctor = new_head_doctor


class Room:
    def __init__(self, room_number, capacity, equipment, status):
        self.room_number = room_number
        self.capacity = capacity
        self.equipment = equipment
        self.status = status

    def __str__(self):
        return f"[Room Number: {self.room_number}, Capacity: {self.capacity}, Equipment: {self.equipment}, Status: {self.status}]"

    def patient_room(self, patient):
        if self.status == "available":
            self.status = "full"
            return f"Patient {patient.name} assigned to room {self.room_number}"
        else:
            return "Room is not available"

    def update_equipment(self, new_equipment):
        self.equipment = new_equipment

    def get_room_info(self):
        return f"Room {self.room_number}, Capacity: {self.capacity}, Equipment: {self.equipment}, Status: {self.status}"


doctor_list = []
nurse_list = []
patient_list = []
department_list = []
room_list = []


def main_menu():
    while True:
        print("Main Menu")
        print("1) Doctor")
        print("2) Nurse")
        print("3) Patient")
        print("4) Department")
        print("5) Room")
        print("0) Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:

            print("1. Add Doctor")
            print("2. Remove Doctor")

            choice2 = int(input("Enter Your Choice: "))

            if choice2 == 1:
                name = input("Enter doctor name: ")
                age = int(input("Enter doctor age: "))
                gender = input("Gender => male/female: ")
                phone = input("Enter doctor phone: ")
                id_number = input("Enter doctor national ID number: ")
                email = input("Enter doctor email: ")

                employee_id_doctor = input("Enter doctor employee ID: ")
                specialization = input("Enter doctor specialization: ")
                department_doctor = input("Enter doctor department: ")

                doctor = Doctor(name, age, gender, phone, id_number, email,
                                employee_id_doctor, specialization, department_doctor)
                doctor_list.append(doctor)
                print("Doctor added successfully!\n")

                print("\nDoctors List:")
                for doctor1 in doctor_list:
                    print(doctor1)
                # این کد رو در قسمت پایین هم استفاده کنم
                print(f"(Current number of doctors: {len(doctor_list)})")

                continue

            elif choice2 == 2:
            
                employee_id = input("Enter doctor employee ID to remove: ")
                doctor_to_remove = None
                for doctor in doctor_list:
                    if doctor.employee_id == employee_id:
                        doctor_to_remove = doctor
                        break

                if doctor_to_remove:
                    doctor_list.remove(doctor_to_remove)
                    print(f"Doctor with employee ID {employee_id} removed successfully!\n")
                else:
                    print(f"No doctor found with employee ID {employee_id}\n")

                print("\nUpdated Doctors List:")
                for doctor1 in doctor_list:
                    print(doctor1)

                    continue
            else:
                print("Invalid choice, please try again.\n")

                continue


        elif choice == 2:

            print("1. Add Nurse")
            print("2. Remove Nurse")

            choice2 = int(input("Enter Your Choise: "))

            if choice2 == 1:

                name = input("Enter nurse name: ")
                age = int(input("Enter nurse age: "))
                gender = input("Gender => male/female: ")
                phone = input("Enter nurse phone: ")
                id_number = input("Enter nurse national ID number: ")
                email = input("Enter nurse email: ")

                employee_id_nurse = input("Enter nurse employee ID: ")
                department_nurse = input("Enter nurse department: ")
                shift = input("Enter nurse shift: ")

                nurse = Nurse(name, age, gender, phone, id_number,
                            email, employee_id_nurse, department_nurse, shift)
                nurse_list.append(nurse)
                print("Nurse added successfully!\n")

                print("\nNurses List:")
                for nurse1 in nurse_list:
                    print(nurse1)

                print(f"(current number of nurse: {len(nurse_list)})")

                continue

            elif choice2 == 2:

                employee_id = input("Enter nurse employee ID to remove: ")
                nurse_to_remove = None
                for nurse in nurse_list:
                    if nurse.employee_id == employee_id:
                        nurse_to_remove = nurse
                        break

                if nurse_to_remove:
                    nurse_list.remove(nurse_to_remove)
                    print(f"Nurse with employee ID {employee_id} removed successfully!\n")
                else:
                    print(f"No nurse found with employee ID {employee_id}\n")

                print("\nUpdated Nurses List:")
                for nurse1 in nurse_list:
                    print(nurse1)

                continue

            else:
                print("Invalid choice, please try again.\n")


        elif choice == 3:

            print("1. Add Patient")
            print("2. Remove Patient")

            choice2 = int(input("Enter Your Choise: "))

            if choice2 == 1:

                name = input("Enter patient name: ")
                age = int(input("Enter patient age: "))
                gender = input("Gender => male/female: ")
                phone = input("Enter patient phone: ")
                id_number = input("Enter patient national ID number: ")
                email = input("Enter patient email: ")

                patient_id = input("Enter patient ID: ")
                disease = input("Enter patient disease: ")
                doctor = input("Enter patient doctor's name: ")
                room = input("Enter patient room number: ")

                patient = Patient(name, age, gender, phone, id_number,
                                email, patient_id, disease, doctor, room)
                patient_list.append(patient)
                print("Patient added successfully!\n")

                print("\nPatients List:")
                for patient1 in patient_list:
                    print(patient1)

                print(f"(current number of patient: {len(patient_list)})")

                continue

            elif choice2 == 2:

                patient_id = input("Enter patient ID to remove: ")
                patient_to_remove = None
                for patient in patient_list:
                    if patient.patient_id == patient_id:
                        patient_to_remove = patient
                        break

                if patient_to_remove:
                    patient_list.remove(patient_to_remove)
                    print(f"Patient with ID {patient_id} removed successfully!\n")
                else:
                    print(f"No patient found with ID {patient_id}\n")

                print("\nUpdated Patients List:")
                for patient1 in patient_list:
                    print(patient1)

                continue

            else:
                print("Invalid choice, please try again.\n")


        elif choice == 4:

            print("1. Add Department")
            print("2. Remove Department")
            
            choice2 = int(input("Enter Your Choice: "))

            if choice2 == 1:

                department_name = input("Enter department name: ")
                department_id = input("Enter department ID: ")
                head_doctor = input("Enter head doctor's name: ")
                number_of_rooms = int(input("Enter number of rooms: "))

                department = Department(
                    department_name, department_id, head_doctor, number_of_rooms)
                department_list.append(department)
                print("Department created successfully!\n")

                print("\nDepartments List:")
                for department1 in department_list:
                    print(department1)
                
                print(f"(current number of department {len(department_list)})")

                continue

            elif choice2 == 2:

                department_id = input("Enter department ID to remove: ")
                department_to_remove = None
                for department in department_list:
                    if department.department_id == department_id:
                        department_to_remove = department
                        break

                if department_to_remove:
                    department_list.remove(department_to_remove)
                    print(f"Department with ID {department_id} removed successfully!\n")
                else:
                    print(f"No department found with ID {department_id}\n")

                print("\nUpdated Departments List:")
                for department1 in department_list:
                    print(department1)

                continue

        elif choice == 5:
            room_number = input("Enter room number: ")
            capacity = int(input("Enter capacity: "))
            equipment = input("Enter equipment: ")
            status = input("Enter status (available/full): ")

            room = Room(room_number, capacity, equipment, status)
            room_list.append(room)
            print("Room created successfully!\n")

            print("\nRooms List:")
            for room1 in room_list:
                print(room1)

            print(f"(current number of room {len(room_list)})")

            continue


        elif choice == 0:
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.\n")


main_menu()