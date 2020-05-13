from utils import SCORES_FILE_NAME

def add_score(diff):
    cur_s = 0
    try:
        f = open(SCORES_FILE_NAME,mode='r')
        cur_s = int(f.read())
        f.close()
    except:
        print ("Score read Error, if file exist then format is wrong !")
    new_s = cur_s + (diff * 3) + 5
    print ("old score is {old}, new score is now : {new}".format(old=cur_s,new=new_s))
    with open(SCORES_FILE_NAME, mode='w+') as f:
        f.write("{score}".format(score=new_s))
        f.close()
    return new_s
