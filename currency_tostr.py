def cur_to_str(e):
    e=e[1:].replace(',','')
    return e

def str_to_cur(e):
    return "${:,.2f}".format(float(e))