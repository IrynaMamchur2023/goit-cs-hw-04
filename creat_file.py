import os

directory = "path/to/text/files"

if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(10): 
    file_path = os.path.join(directory, f"file_{i}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Це тестовий файл номер {i}\n")
        file.write("Це деякий текст для тестування.\n")
        if i % 2 == 0:
            file.write("example keyword\n")
        if i % 3 == 0:
            file.write("test keyword\n")
        if i % 5 == 0:
            file.write("keyword\n")