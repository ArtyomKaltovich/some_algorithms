from operator import itemgetter
import bisect


def dots_lie_on_lines(lines, dots):
    xs = sorted(line[0] for line in lines)
    ys = sorted(line[1] for line in lines)
    result = []
    for dot in dots:
        started = bisect.bisect_right(xs, dot)
        finished = bisect.bisect_left(ys, dot)
        result.append(started - finished)
    return result


if __name__ == '__main__':
    n_lines, n_dots = list(map(int, input().split()))
    lines = []
    for _ in range(n_lines):
        lines.append(list(map(int, input().split())))
    dots = list(map(int, input().split()))
    print(*dots_lie_on_lines(lines, dots))
