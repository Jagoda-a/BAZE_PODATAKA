from student import Student
import csv
import json

def create_dummy_model():
    student_model = [
        Student("2019270487", "Predrag Radak"),
        Student("2019270000", "Nikola Nikolic"),
        Student("2019270111", "Ivan Ivic"),
        Student("2019270222", "Marko Maric"),
        Student("2019270333", "Janko Janic")
    ]
    return student_model


newdata = []

with open("student_data.csv", 'w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",", quotechar="'")
    # writer.writerow(create_dummy_model())
    for student in create_dummy_model():
        writer.writerow([student.broj_indeksa, student.ime_prezime])

with open("student_data.csv", 'r', newline="") as infile:
    reader = csv.reader(infile, delimiter=",", quotechar="'")
    for row in reader:
        newdata.append(row)
        print(row)

with open("student_metada.json", 'w') as metafile:
    metadata = {}
    metadata['columns_nums'] = ["Nroj indeksa", "Ime i prezime"]
    metadata['delimiter'] = ","
    json.dump(metadata, metafile)

with open("studen_metadata.json", 'r') as metafile:
    metadata = json.load(metafile)
    print(metadata['columns'])


newstudents = []

for s in newdata:
    print(s)
    newstudents.append(Student(s[0], s[1]))
    stud = Student("","")
    stud.__setattr__("broj_indeksa", s[0])
    stud.__setattr__("ime_prezime", s[1])
    print(stud.ime_prezime)
    