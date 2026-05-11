import heapq

def dijkstra(graph, start):

    distance = {}

    for node in graph:
        distance[node] = float('inf')

    distance[start] = 0

    heap = [(0, start)]

    while heap:

        current_distance, current_node = heapq.heappop(heap)

        for neighbor, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:

                distance[neighbor] = new_distance

                heapq.heappush(heap, (new_distance, neighbor))

    return distance


graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

result = dijkstra(graph, 'A')

print(result)



# Job Scheduling using Greedy Method

jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

# Step 1: Sort jobs by profit (high to low)
jobs.sort(key=lambda x: x[2], reverse=True)

print("Sorted Jobs:")
print(jobs)

# Step 2: Find maximum deadline
max_deadline = 0

for job in jobs:

    deadline = job[1]

    if deadline > max_deadline:
        max_deadline = deadline

print("Maximum Deadline:", max_deadline)

# Step 3: Create empty slots
slots = [-1] * max_deadline

print("Initial Slots:", slots)

# Step 4: Profit variable
total_profit = 0

# Step 5: Process each job
for job in jobs:


    job_id = job[0]
    deadline = job[1]
    profit = job[2]

    print("\nChecking Job:", job)

    # Check slots backward
    for i in range(deadline - 1, -1, -1):

        print("Checking slot:", i)

        # If slot empty
        if slots[i] == -1:

            # Place job
            slots[i] = job_id

            # Add profit
            total_profit = total_profit + profit

            print(job_id, "inserted at slot", i)

            # Stop checking more slots
            break

# Final Output
print("\nFinal Slots:", slots)
print("Total Profit:", total_profit)






processes = ['P1', 'P2', 'P3']
burst_time = [5, 3, 8]

waiting_time = [0] * len(processes)
turnaround_time = [0] * len(processes)

# Calculate waiting time
for i in range(1, len(processes)):
    waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

# Calculate turnaround time
for i in range(len(processes)):
    turnaround_time[i] = waiting_time[i] + burst_time[i]

# Display output
print("Process\tBT\tWT\tTAT")

for i in range(len(processes)):
    print(processes[i], "\t", burst_time[i], "\t",
          waiting_time[i], "\t", turnaround_time[i])