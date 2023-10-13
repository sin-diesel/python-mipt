#!env/bin/python3


def _main() -> None:
    npoints = int(input())
    masses_coord = list()
    for idx in range(npoints):
        data = input().split(' ')
        x, m = int(data[0]), int(data[1])
        masses_coord.append((m, x))
    masses_coord.sort(key=lambda entry: entry[0], reverse=True)
    print(*[str(entry[1]) for entry in masses_coord], sep="\n")


if __name__ == "__main__":
    _main()

