"""
Take the block of text provided and strip off the whitespace at both ends. Split the text by newline (\n).

Loop through the lines, for each line:

strip off any leading spaces,
check if the first character is lowercase,
if so, split the line into words and get the last word,
strip off BOTH the trailing dot (.) and exclamation mark (!) from this last word,
and finally add it to the results list.
Return the results list.
"""


def first_is_lower(text):
    """ Check if the first character is lowercase """
    return text[0].islower()

def slice_and_dice(text):
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []
    split_text = text.split('\n')
    split_text = [line.strip() for line in split_text]
    split_text = [line for line in split_text if len(line) > 0]
    split_text = [line for line in split_text if line[0].islower()]


    for line in split_text:
        line = line.split(' ')
        lastword = line[-1]
        lastword = lastword.strip("!").strip('.')
        results.append(lastword)

    return(results)



    