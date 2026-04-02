def find_keyword_lines(file_path: str, keyword: str) -> list[int]:
    matches = []
    with open(file_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            if keyword in line:
                matches.append(idx)
    return matches


if __name__ == "__main__":
    lines = find_keyword_lines("score_file", "Phoneix")
    if lines:
        print(f"Keyword 'Phoneix' found at line(s): {lines}")
    else:
        print("Keyword 'Phoneix' not found in score_file")