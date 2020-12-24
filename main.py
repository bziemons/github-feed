import sys


def main(github_username):
    pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], " <GitHub username>")
    else:
        main(sys.argv[1])
