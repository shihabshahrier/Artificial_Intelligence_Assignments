import random as rand


def alphaBetaPruning(
    curr_depth,
    max_depth,
    curr_branch,
    max_branch,
    isMax,
    alpha,
    beta,
    terminals,
    visited_terminals,
):
    if curr_depth == max_depth:
        visited_terminals.append(curr_branch)
        return terminals[curr_branch]
    if isMax:
        best_score = float("-inf")
        for i in range(max_branch):
            value = alphaBetaPruning(
                curr_depth + 1,
                max_depth,
                curr_branch * max_branch + i,
                max_branch,
                False,
                alpha,
                beta,
                terminals,
                visited_terminals,
            )
            best_score = max(best_score, value)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float("inf")
        for i in range(max_branch):
            value = alphaBetaPruning(
                curr_depth + 1,
                max_depth,
                curr_branch * max_branch + i,
                max_branch,
                True,
                alpha,
                beta,
                terminals,
                visited_terminals,
            )
            best_score = min(best_score, value)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        student_id = file.readline().strip()
        minimum_hp, maximum_hp = map(int, file.readline().split())

    attackers_number_of_turns = int(student_id[0])
    defenders_initial_lifeline = int(student_id[7:5:-1])
    number_of_bullets = int(student_id[2])

    maximum_possible_turns = 2 * attackers_number_of_turns
    number_of_terminal = number_of_bullets**maximum_possible_turns

    terminals = [
        rand.randint(minimum_hp, maximum_hp) for _ in range(number_of_terminal)
    ]
    # terminals = [19, 22, 9, 2, 26, 16, 16, 27, 16]
    # terminals = [18, 13, 5, 12, 10, 5, 13, 7, 17, 8, 6, 8, 5, 11, 13, 18]
    visited_terminals = []
    attackers_best_score = alphaBetaPruning(
        0,
        maximum_possible_turns,
        0,
        number_of_bullets,
        True,
        float("-inf"),
        float("inf"),
        terminals,
        visited_terminals,
    )

    print(f"Depth and Branches ratio is {maximum_possible_turns}:{number_of_bullets}")

    print("Terminal States (leaf node values) are", *terminals)
    print(
        f"Left life(HP) of the defender after maximum damage caused by the attacker is {defenders_initial_lifeline - attackers_best_score}"
    )
    print(f"After Alpha-Beta Pruning Leaf Node Comparisons {len(visited_terminals)}")
