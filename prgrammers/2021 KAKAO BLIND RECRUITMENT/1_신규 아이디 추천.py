import re


# def solution(new_id):
#     answer = ''

#     # 1단계
#     new_id = new_id.lower()

#     # 2단계
#     new_id = "".join(re.findall('\w*|[.]*|[-]*|[_]*', new_id))

#     # 3단계
#     new_id = re.sub('[.]{2,}', '.', new_id)

#     # 4단계
#     while new_id and new_id[0] == '.':
#         new_id = new_id[1:]

#     while new_id and new_id[-1] == '.':
#         new_id = new_id[:-1]

#     # 6단계
#     if len(new_id) >= 16:
#         new_id = new_id[:15]
#         while new_id and new_id[-1] == '.':
#             new_id = new_id[:-1]

#     # 5단계
#     if not new_id:
#         new_id += "a"

#     # 7단계
#     if len(new_id) <= 2:
#         new_id += (new_id[-1] * (3 - len(new_id)))

#     return new_id

def solution(new_id):
    st = new_id

    # 1단계
    st = st.lower()
    # 2단계
    st = re.sub('[^a-z0-9\-_.]', '', st)
    # 3단계
    st = re.sub('\.+', '.', st)
    # 4단계
    st = re.sub('^[.]|[.]$', '', st)
    # 5단계, 6단계
    st = 'a' if not st else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    # 7단계
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3 - len(st))])
    return st

new_id_1 = "...!@BaT#*..y.abcdefghijklm"
# 정답 : "bat.y.abcdefghi"
new_id_2 = "z-+.^."
# 정답 : "z--"
new_id_3 = "=.="
# 정답 : "aaa"
new_id_4 = "123_.def"
# 정답 : "123_.def"
new_id_5 = "abcdefghijklmn.p"
# 정답 : "abcdefghijklmn"
