import os
import threading
import time
from collections import defaultdict

def search_keywords(file_paths, keywords, results, thread_id):
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                for keyword in keywords:
                    if keyword in content:
                        results[keyword].append(file_path)
        except Exception as e:
            print(f"Thread {thread_id}: Error reading {file_path}: {e}")

def main():
    directory = 'C:\My_repo\goit-cs-hw-04'

    keywords = ['keyword1', 'keyword2', 'keyword3']

    file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    num_threads = 4
    files_per_thread = len(file_paths) // num_threads
    threads = []
    results = defaultdict(list)

    start_time = time.time()

    for i in range(num_threads):
        start_index = i * files_per_thread
        end_index = (i + 1) * files_per_thread if i < num_threads - 1 else len(file_paths)
        thread_files = file_paths[start_index:end_index]
        thread = threading.Thread(target=search_keywords, args=(thread_files, keywords, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    for keyword, files in results.items():
        print(f"Keyword '{keyword}' found in files: {files}")

    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()