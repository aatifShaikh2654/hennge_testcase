import sys

def main():
    input_lines = sys.stdin.read().splitlines()
    results = []

    i = 0
    N = int(input_lines[i])
    i += 1

    for _ in range(N):
        if i >= len(input_lines):  # Not enough lines for the next test case
            results.append("-1")
            break

        X = int(input_lines[i])
        i += 1

        if i >= len(input_lines):
            results.append("-1")
            break

        try:
            numbers = list(map(int, input_lines[i].split()))
        except ValueError:
            results.append("-1")
            i += 1
            continue

        i += 1

        if len(numbers) != X:
            results.append("-1")
        else:
            total = sum(num**4 for num in numbers if num <= 0)
            results.append(str(total))

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
