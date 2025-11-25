# grade_manager.py
# Developer: Palak
# Date: 25 Nov 2025
# Title: Student Grade Manager CLI Tool

import csv
import statistics as stats

def banner():
    print("\n" + "-"*50)
    print("         STUDENT GRADE MANAGER – CLI TOOL")
    print("-"*50)
    print("Import marks, compute stats, assign grades & generate reports.\n")

def main_menu():
    print("OPTIONS:")
    print("1) Enter data manually")
    print("2) Load data from CSV file")
    print("3) Exit\n")

def manual_data():
    records = {}
    print("Enter student details manually (type 'done' to finish):")
    
    while True:
        name = input("Name: ").strip()
        if name.lower() == "done":
            break
        try:
            score = float(input(f"Marks for {name}: "))
            if not 0 <= score <= 100:
                print("Marks must be between 0–100.")
                continue
            records[name] = score
        except:
            print("Invalid marks! Please enter a number.")
    
    return records

def load_csv():
    records = {}
    filename = input("CSV file name: ").strip()

    try:
        with open(filename, "r") as f:
            for row in csv.reader(f):
                if len(row) >= 2:
                    name = row[0].strip()
                    try:
                        marks = float(row[1])
                        records[name] = marks
                    except:
                        print(f"Invalid marks for: {name} — skipped")
        print(f"Imported {len(records)} entries from {filename}")
    except Exception as e:
        print(f"Error: {e}")

    return records

# ---------- ANALYTICS ----------

def average(m):
    return stats.mean(m.values()) if m else 0

def median(m):
    return stats.median(m.values()) if m else 0

def topper(m):
    if not m:
        return None, None
    t = max(m, key=m.get)
    return t, m[t]

def lowest(m):
    if not m:
        return None, None
    l = min(m, key=m.get)
    return l, m[l]

def grading(m):
    g = {}
    for name, score in m.items():
        if score >= 90:
            g[name] = "A"
        elif score >= 80:
            g[name] = "B"
        elif score >= 70:
            g[name] = "C"
        elif score >= 60:
            g[name] = "D"
        else:
            g[name] = "F"
    return g

def distribution(grades):
    bucket = {x: 0 for x in ["A", "B", "C", "D", "F"]}

    for g in grades.values():
        bucket[g] += 1

    return bucket

def pass_fail(m):
    passed = [n for n, s in m.items() if s >= 40]
    failed = [n for n, s in m.items() if s < 40]
    return passed, failed

# ---------- REPORTING ----------

def show_report(m, grades, avg, med, top_info, low_info, dist, passed, failed):
    tname, tscore = top_info
    lname, lscore = low_info

    print("\n" + "-"*50)
    print("                   REPORT SUMMARY")
    print("-"*50)

    print(f"{'Student':<18}{'Marks':>8}{'Grade':>10}")
    print("-"*40)
    
    for name in m:
        print(f"{name:<18}{m[name]:>8.2f}{grades[name]:>10}")
    
    print("-"*40)
    print(f"{'Average':<18}{avg:>8.2f}")
    print(f"{'Median':<18}{med:>8.2f}")
    print(f"Top Performer: {tname} ({tscore})")
    print(f"Lowest Score: {lname} ({lscore})")

    print("\nGrade Distribution:")
    for g in dist:
        print(f"  {g}: {dist[g]} student(s)")

    print(f"\nPassed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
    print(f"Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")
    print("-"*50 + "\n")

def export_csv(m, grades):
    ans = input("Export results to CSV? (y/n): ").strip().lower()
    if ans != "y":
        return

    fname = input("File name: ").strip()

    try:
        with open(fname, "w", newline='') as f:
            w = csv.writer(f)
            w.writerow(["Name", "Marks", "Grade"])
            for n in m:
                w.writerow([n, m[n], grades[n]])
        print(f"Saved to {fname}")
    except Exception as e:
        print(f"Error saving file: {e}")

# ---------- MAIN CONTROLLER ----------

def main():
    banner()

    while True:
        main_menu()
        option = input("Select option: ").strip()

        if option == "1":
            marks = manual_data()
        elif option == "2":
            marks = load_csv()
        elif option == "3":
            print("Exiting… Thank you!")
            break
        else:
            print("Invalid selection.")
            continue

        if not marks:
            print("No records found. Try again.\n")
            continue

        avg = average(marks)
        med = median(marks)
        top = topper(marks)
        low = lowest(marks)
        grades = grading(marks)
        dist = distribution(grades)
        passed, failed = pass_fail(marks)

        show_report(marks, grades, avg, med, top, low, dist, passed, failed)
        export_csv(marks, grades)

        again = input("Analyze another dataset? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
