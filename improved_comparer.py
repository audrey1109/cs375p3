'''
Audrey Palmer
Desmond Frimpong
Samuel Offei

improved_comparer.py
'''

from edit_distance import bottom_up_edit_distance
from file_comparison import fc_strings


def get_lines(f1, f2) :
    '''
    breaks files down into groups of strings
    '''

    f1_content, f1_lines = open(f1, "r"), []
    f2_content, f2_lines = open(f2, "r"), []

    for line in f1_content : f1_lines.append(line)
    for line in f2_content : f2_lines.append(line)

    return f1_lines, f2_lines


def improved_comparer(lines1, lines2) :
    ''' a comparer optimized for .py files '''

    output, processing = [], True
    i, j = 0, 0

    while processing :

        # if there are no lines left in either...
        if i >= len(lines1) and j >= len(lines2) :
            processing = False
            break

        # if there are still lines in 1 but none in 2 
        elif j >= len(lines2) :
            while i < len(lines1) :
                output.append(f"#####\nDELETING\n{lines1[i]}\n")
                i += 1
            processing = False
            break

        # if there are still lines in 2 but none in 1
        elif i >= len(lines1) :
            while j < len(lines2) :
                output.append(f"#####\nINSERTING\n{lines2[j]}\n")
                j += 1
            processing = False
            break

        else :

            line1, line2 = lines1[i], lines2[j]

            if "#" in line2 :
                output.append(f"#####\nINSERTING\n{line2}\n")
                j += 1
                continue

            elif "'''" in line2 :
                output.append(f"#####\nINSERTING\n{line2}\n")
                j += 1
                while j < len(lines2) and "'''" not in lines2[j] :
                    output.append(f"#####\nINSERTING\n{lines2[j]}\n")
                    j += 1
                if j < len(lines2) :
                    output.append(f"#####\nINSERTING\n{lines2[j]}\n")
                    j += 1
                continue

            elif '"""' in line2 :
                output.append(f"#####\nINSERTING\n{line2}\n")
                j += 1
                while j < len(lines2) and '"""' not in lines2[j] :
                    output.append(f"#####\nINSERTING\n{lines2[j]}\n")
                    j += 1
                if j < len(lines2) :
                    output.append(f"#####\nINSERTING\n{lines2[j]}\n")
                    j += 1
                continue

            else :
                instructions = fc_strings(line1, line2)
                flags = []

                for ins in instructions :
                    if "REPLACE" in ins : flags.append("replace")
                    elif "DELETE" in ins : flags.append("delete")
                    elif "KEEP" in ins : flags.append("keep")
                    else : flags.append("insert")

                if all(f == "delete" for f in flags) :
                    output.append(f"########\nLINE DELETION :\n{line1}\nhas been deleted\n")
                    i += 1
                    continue

                if all(f == "insert" for f in flags) :
                    output.append(f"########\nLINE INSERTION :\n{line2}\nhas been inserted\n")
                    j += 1
                    continue

                if all(f == "keep" for f in flags) :
                    output.append(f"########\nLINE KEPT :\n{line1}\nhas been maintained\n")
                    i += 1
                    j += 1
                    continue

                else :
                    output.append(f"########\nLINE EDIT :\n{line1}\nhas been edited into {line2}\n")
                    i += 1
                    j += 1
                    continue

    return output



if __name__ == "__main__" :

    lines1, lines2 = get_lines("comparison_files/fib1.py", "comparison_files/fib2.py")
    output = improved_comparer(lines1, lines2)

    for line in output : print(line)
