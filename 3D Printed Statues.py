from collections import deque

def min_days(n):
    # Initial state is (number of printers, number of statues, number of days)
    initial_state = (1, 0, 0)

    # Create a queue and add the initial state
    queue = deque([initial_state])

    # Create a set to store visited states
    visited = set()

    while queue:
        printers, statues, days = queue.popleft()

        # If we have printed enough statues, return the number of days
        if statues >= n:
            return days

        # Generate new states and add them to the queue
        new_states = [(printers, statues + printers, days + 1), (printers * 2, statues, days + 1)]

        for new_state in new_states:
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)


print(min_days(int(input())))
