def judge_solution(standard_solution, team_output):
    """
    Judges a team's output based on the standard solution.
    Args:
    standard_solution (list[str]): The lines of the standard solution.
    team_output (list[str]): The lines of the team's output.
    Returns:
    str: One of "Accepted", "Presentation Error", or "Wrong Answer".
    """
    if len(standard_solution) != len(team_output):
        return "Wrong Answer"

    for i in range(len(standard_solution)):
        std_line = standard_solution[i]
        out_line = team_output[i]

        # Check if the lines match exactly
        if std_line == out_line:
            continue

        # Check if the lines have the same numeric characters in the same order
        std_nums = ''.join(c for c in std_line if c.isdigit())
        out_nums = ''.join(c for c in out_line if c.isdigit())
        if std_nums == out_nums:
            return "Presentation Error"

    # If all lines match exactly, it's accepted
    return "Accepted"

def main():
    run_number = 1
    while True:
        # Read the standard solution
        n = int(input())
        if n == 0:
            break
        standard_solution = [input() for _ in range(n)]

        # Read the team output
        m = int(input())
        team_output = [input() for _ in range(m)]

        # Judge the solution
        result = judge_solution(standard_solution, team_output)
        print(f"Run #{run_number}: {result}")
        run_number += 1

if __name__ == "__main__":
    main()
