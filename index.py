def read_patient_details():
    patient_count = int(input("Enter number of patients: "))
    patients = []

    for patient_number in range(1, patient_count + 1):
        print(f"\nEnter details for patient {patient_number}")
        name = input("Name: ")
        blood_group = input("Blood group: ")
        disease = input("Disease: ")

        patients.append(
            {
                "name": name,
                "blood_group": blood_group,
                "disease": disease,
            }
        )

    return patients


def display_patient_details(patients):
    print("\nHospital Patient Details")
    for index, patient in enumerate(patients, start=1):
        print(f"\nPatient {index}")
        print(f"Name: {patient['name']}")
        print(f"Blood Group: {patient['blood_group']}")
        print(f"Disease: {patient['disease']}")


patients = read_patient_details()
display_patient_details(patients)
