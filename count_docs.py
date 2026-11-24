import sys
from pathlib import Path

def collect_stats(folder):
    count = 0
    total = 0
    largest = []

    for file in folder.rglob("*.md"):
        size = file.stat().st_size
        count += 1
        total += size

        largest.append((size, file))
        largest.sort(key=lambda item: item[0], reverse=True)
        largest = largest[:3]

    return count, total, largest

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python count_docs.py FOLDER")
        sys.exit(1)

    folder = Path(sys.argv[1])
    count, total, largest = collect_stats(folder)

    print(f"count files: {count}")
    print(f"total size: {round(total / 1024, 2)} KB")

    for size, file_path in largest:
        print(f"{file_path.name} - {round(size / 1024, 2)} KB")