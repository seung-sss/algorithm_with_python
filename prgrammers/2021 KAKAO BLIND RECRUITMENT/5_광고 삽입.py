# 시간 초 단위로 변경
def make_sec(time):  # t : 'hh:mm:ss'
    # tmp = t.split(':')
    # return (int(tmp[0]) * 3600) + (int(tmp[1]) * 60) + int(tmp[2])
    return sum([int(x) * y for x, y in zip(time.split(':'), [3600, 60, 1])])


# 원래 상태로 변경
def make_origin(seconds):  # t : int(sec)
    #     h = t // 3600
    #     m = (t % 3600) // 60
    #     s = (t % 3600) % 60

    #     res = ''

    #     if h < 10:
    #         res += '0' + str(h) + ':'
    #     else:
    #         res += str(h) + ':'

    #     if m < 10:
    #         res += '0' + str(m) + ':'
    #     else:
    #         res += str(m) + ':'

    #     if s < 10:
    #         res += '0' + str(s)
    #     else:
    #         res += str(s)

    #     return res
    h, m = divmod(seconds, 3600)
    m, s = divmod(m, 60)
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


def get_accumulated_time(play_list):
    for i in range(1, len(play_list)):
        play_list[i] += play_list[i - 1]

    for i in range(1, len(play_list)):
        play_list[i] += play_list[i - 1]

    return play_list


def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    spt = make_sec(play_time)
    sat = make_sec(adv_time)

    arr = [0] * (spt + 1)

    for log in logs:
        s, e = log.split("-")
        arr[make_sec(s)] += 1
        arr[make_sec(e)] -= 1

    arr = get_accumulated_time(arr)

    # logs 초로 만들어서 arr에 올리기
    #     for t in logs:
    #         tmp = t.split('-')
    #         start = make_sec(tmp[0])
    #         end = make_sec(tmp[1])

    #         for i in range(start + 1, end + 1):
    #             arr[i] += 1

    #     sum_value = 0
    #     prefix_sum = [0]

    #     # 누적 합 만들기
    #     for val in arr:
    #         sum_value += val
    #         prefix_sum.append(sum_value)

    # 탐색
    max_viewer = 0
    answer = 0

    # for i in range(1, spt - sat + 1):
    #     if max_val < prefix_sum[i + sat] - prefix_sum[i]:
    #         max_val = prefix_sum[i + sat] - prefix_sum[i]
    #         max_start = i - 1

    for i in range(sat, spt + 1):
        if max_viewer < arr[i] - arr[i - sat]:
            max_viewer = arr[i] - arr[i - sat]
            answer = i - sat + 1

    if max_viewer <= arr[sat - 1]:  # ~ adv_time-1 까지의 구간이 최대면
        answer = 0  # answer은 0초

    return make_origin(answer)