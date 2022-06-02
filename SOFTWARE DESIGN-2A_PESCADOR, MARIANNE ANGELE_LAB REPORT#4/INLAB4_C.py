def reverse_string(s):
    if len(s)<=0:

        return 0
    elif len(s)==1:

        return s
    else:

        return s[-1] + reverse_string(s[:-1])

if __name__=="__main__":
    s = input()
    print(reverse_string(s))