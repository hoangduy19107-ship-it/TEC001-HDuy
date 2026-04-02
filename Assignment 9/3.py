def average_score_from_file(path):
    total = 0.0
    count = 0

    with open(path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                raise ValueError(f"Bad format line {line_no}: {line}")
            name = parts[0].strip()
            score_str = parts[1].strip()
            try:
                score = float(score_str)
            except ValueError:
                raise ValueError(f"Invalid score line {line_no}: {score_str}")
            total += score
            count += 1

    if count == 0:
        raise ValueError("No records in file.")
    return total / count


if __name__ == "__main__":
    file_path = "score_file"
    avg = average_score_from_file(file_path)
    print(f"Average score from {file_path}: {avg:.2f}")