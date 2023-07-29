def len_last(s):
    s = s.strip()  # quita los espacios al inicio y al final
    cont = 0
    for l in s:
        if l == ' ':
            cont = 0  # reseta el cont mientras que no sea la ultima palabra
        else:
            cont += 1

    print(cont)

len_last("   fly me   to   the moon   ")
