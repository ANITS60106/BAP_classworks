def make(s):
    a = b = c = d = e = False
    total = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'A':
            a = True
            total += -1 if (b or c or d or e) else 1
        elif s[i] == 'B':
            b = True
            total += -10 if (c or d or e) else 10
        elif s[i] == 'C':
            c = True
            total += -100 if (d or e) else 100
        elif s[i] == 'D':
            d = True
            total += -1000 if e else 1000
        elif s[i] == 'E':
            e = True
            total += 10000

    return total


def main():
    t = int(input())

    for _ in range(t):
        s = list(input())
        indices = {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1}

        for i, char in enumerate(s):
            if indices[char] == -1:
                indices[char] = i

        res = make(s)

        for char, index in indices.items():
            if index != -1:
                for replacement in 'ABCDE':
                    if replacement != char:
                        s[index] = replacement
                        res = max(res, make(s))
                s[index] = char

        indices = {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1}

        for i in range(len(s) - 1, -1, -1):
            if indices[s[i]] == -1:
                indices[s[i]] = i

        for char, index in indices.items():
            if index != -1:
                for replacement in 'ABCDE':
                    if replacement != char:
                        s[index] = replacement
                        res = max(res, make(s))
                s[index] = char

        print(res)


if __name__ == "__main__":
    main()
