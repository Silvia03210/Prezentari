A = [3, 2, 1]
B = []
C = []


def move(n, sursa, tinta, intermediar):
    if n > 0:
        # Mutăm n - 1 discuri de la sursa la intermediar, so they are out of the way
        move(n - 1, sursa, intermediar, tinta)

        # Move the nth disk from source to target
        tinta.append(sursa.pop())

        # Display our progress
        print(A, B, C, '-----------------', sep='\n')

        # Move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, intermediar, tinta, sursa)

# Initiate call from source A to target C with auxiliary B
move(3, A, C, B)