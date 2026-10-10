import csv
from pathlib import Path
from statistics import mean

import yaml


def main():
    # Find the project folder
    project_dir = Path(__file__).resolve().parent.parent

    # Read experiment configuration
    with open(project_dir / "configs/config.yaml", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    # Read the sample dataset
    data_path = project_dir / config["data"]["input_file"]

    with open(data_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        records = list(reader)

    if not records:
        raise ValueError("The dataset is empty.")

    print("AI Programming Research Benchmark")
    print("Data type:", config["project"]["data_type"])
    print("-" * 45)

    # Compare the three research groups
    for group in config["experiment"]["groups"]:
        students = [row for row in records if row["group"] == group]

        if not students:
            print(f"{group}: No data available")
            continue

        scores = [
            int(row["passed_tests"]) / int(row["total_tests"]) * 100
            for row in students
        ]

        times = [float(row["completion_time_min"]) for row in students]
        concepts = [float(row["concept_score"]) for row in students]
        errors = [int(row["programming_errors"]) for row in students]

        print(f"\nGroup: {group}")
        print(f"Number of students: {len(students)}")
        print(f"Average task score: {mean(scores):.2f}%")
        print(f"Average completion time: {mean(times):.2f} minutes")
        print(f"Average concept score: {mean(concepts):.2f}%")
        print(f"Average programming errors: {mean(errors):.2f}")

    print("\nBenchmark completed successfully.")
    print("Note: Synthetic data, not real research results.")


if __name__ == "__main__":
    main()
