import csv
import sys
import re

def main():

    # Verify the number of arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit()
    # Assing names to each argument
    database = sys.argv[1]
    sequence = sys.argv[2]
    # Open the database
    with open(database, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        db = list(reader)
    # Open the sequence and remove new line at the end
    with open(sequence, 'r') as txtfile:
        sq = txtfile.readline().rstrip("\n")

    AGATC = count("AGATC", sq)
    TTTTTTCT = count("TTTTTTCT", sq)
    TCTAG = count("TCTAG", sq)
    AATG = count("AATG", sq)
    GATA = count("GATA", sq)
    TATC = count("TATC", sq)
    GAAA = count("GAAA", sq)
    TCTG = count("TCTG", sq)

    if database == "databases/small.csv":
        for i in range(len(db)):
            if all([db[i]["AGATC"] == str(AGATC), db[i]["AATG"] == str(AATG), db[i]["TATC"] == str(TATC)]):
                name = db[i]["name"]
                break
            else:
                name = "No match"
    else:
        for i in range(len(db)):
            if all([db[i]["AGATC"] == str(AGATC), db[i]["TTTTTTCT"] == str(TTTTTTCT), db[i]["TCTAG"] == str(TCTAG), db[i]["AATG"] == str(AATG),
                    db[i]["GATA"] == str(GATA), db[i]["TATC"] == str(TATC), db[i]["GAAA"] == str(GAAA), db[i]["TCTG"] == str(TCTG)]):
                name = db[i]["name"]
                break
            else:
                name = "No match"
    print(name)

# Count the number of STR
def count(c, s):
    p = rf'({c})\1*'
    pattern = re.compile(p)
    match = [match for match in pattern.finditer(s)]
    max = 0
    for i in range(len(match)):
        if match[i].group().count(c) > max:
            max = match[i].group().count(c)
    return max

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
