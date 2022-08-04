MAX = 219


# Function to return the minimum number of halls required Logic is based on dynamic programing algorithm with
# tabulation approach rather than calculating all possible meeting rooms we are counting the active meetings. At any
# end of point if there are more than one active meetings that means we need more rooms. Cumulative result is
# considered to remove the redundant meeting room asked for multiple meetings of intersecting timings.
def min_conf_rooms(lectures, n):
    # Array to store the number of
    # lectures ongoing at time t
    prefix_sum = [0] * MAX

    # For every lecture increment start
    # point s decrement (end point + 1)
    for i in range(n):
        prefix_sum[lectures[i][0]] += 1
        prefix_sum[lectures[i][1] + 1] -= 1

    ans = prefix_sum[0]

    # Perform prefix sum and update
    # the ans to maximum
    for i in range(1, MAX):
        prefix_sum[i] += prefix_sum[i - 1]
        ans = max(ans, prefix_sum[i])

    return ans


# Driver code
if __name__ == "__main__":
    # Test case 1
    A = [[0, 30],
         [5, 10],
         [15, 20]
         ]

    size = len(A)

    print(min_conf_rooms(A, size))

    # Test case 2
    A = [[1, 18],
         [18, 23],
         [15, 29],
         [4, 15],
         [2, 11],
         [5, 13]
         ]

    size = len(A)

    print(min_conf_rooms(A, size))
