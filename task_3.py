import sys
import os
from typing import List, Dict, Callable


def parse_log_line(line: str) -> Dict[str, str]:
    # Розбирає рядок логу на компоненти.
    parts = line.split(maxsplit=3)
    if len(parts) < 4:
        return {}
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2].upper(),
        'message': parts[3].strip()
    }


def load_logs(file_path: str) -> List[Dict[str, str]]:
    # Завантажує логи з файлу та повертає список розібраних рядків.
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Відбулася помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    # Фільтрує логи за вказаним рівнем (використання filter).
    return list(filter(lambda log: log['level'] == level.upper(), logs))


def count_logs_by_level(logs: List[Dict]) -> Dict[str, int]:
    # Підраховує кількість записів для кожного рівня логування.
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: Dict[str, int]):
    # Виводить таблицю зі статистикою рівнів логування.
    print(f"{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 18 + "|" + "-" * 11)
    for level, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{level:<17} | {count:<10}")


def main():
    # Головна функція виконання скрипту.
    if len(sys.argv) < 2:
        print("Використання: python task_3.py <path_to_log_file> [log_level]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if len(sys.argv) > 2:
        level_to_filter = sys.argv[2].upper()
        filtered = filter_logs_by_level(logs, level_to_filter)

        if filtered:
            print(f"\nДеталі логів для рівня '{level_to_filter}':")
            for log in filtered:
                print(f"{log['date']} {log['time']} - {log['message']}")
        elif level_to_filter not in counts:
            print(f"\nЗаписів для рівня '{level_to_filter}' не знайдено.")


if __name__ == "__main__":
    main()