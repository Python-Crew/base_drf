


def delete_space_and_slash(aim_str):
    len_str = len(aim_str)
    condition = True
    while condition==True:
        aim_str = aim_str.strip("/").strip(" ")
        if len_str > len(aim_str):
            condition = True
            len_str = len(aim_str)
        else:
            condition = False
    return aim_str