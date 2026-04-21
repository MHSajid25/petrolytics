import csv

def read_log_data(file_path):
    data = []

    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append({
                    "depth": float(row["depth"]),
                    "gr": float(row["gr"])
                })

        return data

    except Exception as e:
        print(f"Error reading file: {e}")
        return []
