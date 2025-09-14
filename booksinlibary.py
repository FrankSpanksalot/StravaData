import os
import csv

def list_books_to_csv(root_path, output_csv):
    # Dictionary to hold books by "basename"
    books = {}

    for dirpath, _, files in os.walk(root_path):
        for file in files:
            if file.lower().endswith((".mobi", ".epub")):
                full_path = os.path.join(dirpath, file)
                basename, ext = os.path.splitext(file)

                # If the base name is already recorded, skip duplicates (.mobi/.epub pair)
                if basename not in books:
                    books[basename] = full_path
                else:
                    # If one already exists, keep the first one found (skip duplicates)
                    continue

    # Write results to CSV
    with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Book Name", "File Path"])  # header
        for basename, path in sorted(books.items()):
            writer.writerow([basename, path])

    print(f"CSV file created: {output_csv}")


if __name__ == "__main__":
    # Replace with your UNC path and desired output location
   # unc_path = r"\\millervillenas\ebooks\Adult"
    unc_path = r"\\millervillenas\ebooks\Calibre Library"
    output_file = r"calibre_library_books_list.csv"

    list_books_to_csv(unc_path, output_file)
