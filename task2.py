import os
import multiprocessing
import time
from collections import defaultdict

def search_keywords(file_paths, keywords, results, process_id):
    local_results = defaultdict(list)
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                for keyword in keywords:
                    if keyword in content:
                        local_results[keyword].append(file_path)
        except Exception as e:
            print(f"Process {process_id}: Error reading {file_path}: {e}")
    results.update(local_results)

def main():
    directory = 'C:\My_repo\goit-cs-hw-04'

    keywords = ['keyword1', 'keyword2', 'keyword3']

    file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    num_processes = 4
    files_per_process = len(file_paths) // num_processes
    processes = []
    manager = multiprocessing.Manager()
    results = manager.dict()

    start_time = time.time()

    for i in range(num_processes):
        start_index = i * files_per_process
        end_index = (i + 1) * files_per_process if i < num_processes - 1 else len(file_paths)
        process_files = file_paths[start_index:end_index]
        process = multiprocessing.Process(target=search_keywords, args=(process_files, keywords, results, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    for keyword, files in results.items():
        print(f"Keyword '{keyword}' found in files: {files}")

    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()