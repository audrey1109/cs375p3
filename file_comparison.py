'''
Audrey Palmer
Desmond Frimpong
Samuel Offei

file_comparison.py
'''

from edit_distance import bottom_up_edit_distance, top_down_recursive

def get_lines(f1, f2) :
    '''
    breaks files down into groups of strings
    '''

    f1_content, f1_lines = open(f1, "r"), []
    f2_content, f2_lines = open(f2, "r"), []

    for line in f1_content : f1_lines.append(line)
    for line in f2_content : f2_lines.append(line)

    return f1_lines, f2_lines

def fc_strings(string_1, string_2):
    """
    Computes the edit distance between string_1 and string_2.
    Uses the edit distance to determine the edits needed to
    convert string_1 into string_2.
    """
    instructions = []
    chache = bottom_up_edit_distance(string_1, string_2)

    while len(string_1) > 0 and len(string_2) > 0:
        if string_1[-1] == string_2[-1]:
            instructions.append(f"--------\nKEEP -> char {string_1[-1]} as {string_1}\n")
            string_1 = string_1[:-1]
            string_2 = string_2[:-1]
        else:
            if chache[len(string_1)][len(string_2)] == chache[len(string_1) - 1][len(string_2) - 1] + 3:
                instructions.append(f"--------\nREPLACE -> char {string_1[-1]} with {string_2[-1]}\n")
                string_1 = string_1[:-1]
                string_2 = string_2[:-1]
            elif chache[len(string_1)][len(string_2)] == chache[len(string_1) - 1][len(string_2)] + 2:
                instructions.append(f"--------\nDELETE -> char {string_1[-1]} from string 1 {string_1}\n")
                string_1 = string_1[:-1]
            else:
                instructions.append(f"--------\nINSERT -> {string_2[-1]}\n")
                string_2 = string_2[:-1]
    return instructions


def compare_files() :

    lines1, lines2 = get_lines("comparison_files/fib1.py", "comparison_files/fib2.py")
    output, processing = [], True
    i = 0

    while processing :

        if i >= len(lines1) and i >= len(lines2) :
            processing = False
            break

        elif i >= len(lines2) :
            while i < len(lines1) :
                output.append(f"#####\nDELETING\n{lines1[i]}\n")
                i += 1
            processing = False
            break

        elif i >= len(lines1) :
            while i < len(lines2) :
                output.append(f"#####\nINSERTING\n{lines2[i]}\n")
                i += 1
            processing = False
            break

        instructions = fc_strings(lines1[i], lines2[i])

        instruction_flags = []

        for line in instructions : 

            if "REPLACE" in line : instruction_flags.append("replace")
            elif "DELETE" in line : instruction_flags.append("delete")
            elif "KEEP" in line   : instruction_flags.append("keep")
            else                  : instruction_flags.append("insert")

        # now decide based on flags
        if all(flag == "delete" for flag in instruction_flags) :
            output.append(f"########\nLINE DELETION : {lines1[i]} deleted\n")
            i += 1
            continue

        if all(flag == "insert" for flag in instruction_flags) :
            output.append(f"########\nLINE INSERTION : {lines2[i]} inserted\n")
            i += 1
            continue

        if all(flag == "keep" for flag in instruction_flags) :
            output.append(f"########\nLINE KEPT : {lines1[i]} maintained\n")
            i += 1
            continue

        else :
            output.append(f"########\nLINE REPLACEMENT : {lines1[i]} edited into {lines2[i]}\n")
            i += 1
            continue

    return output


if __name__ == "__main__" :

    output = compare_files()

    for line in output :
        print(line)






