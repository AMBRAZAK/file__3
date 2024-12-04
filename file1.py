import os

def combine_files(output_file):
    files_data = []
    
    # Считываем файлы из текущей папки
    for filename in os.listdir():
        if filename.endswith('.txt') and filename != output_file:  # Учитываем только .txt файлы, кроме выходного
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                files_data.append((filename, len(lines), lines))
    
    # Сортируем по количеству строк
    files_data.sort(key=lambda x: x[1])
    
    # Записываем в итоговый файл
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for file_name, line_count, lines in files_data:
            result_file.write(f"{file_name}\n{line_count}\n")
            result_file.writelines(lines)
            result_file.write("\n")  # Добавляем пустую строку между файлами

# Пример использования
combine_files("итоговый_файл.txt")