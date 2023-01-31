def seven_segment_to_string(segment_string):
    segments = segment_string.strip().split("\n")
    digit_mapping = {
    " _ | ||_|": "0",
    "     |  |": "1",
    " _  _||_ ": "2",
    " _  _| _|": "3",
    "   |_|  |": "4",
    " _ |_  _|": "5",
    " _ |_ |_|": "6",
    " _   |  |": "7",
    " _ |_||_|": "8",
    " _ |_| _|": "9"
    }

    result = ""
    for i in range(0, len(segments[0]), 3):
        segment = segments[0][i:i+3] + segments[1][i:i+3] + segments[2][i:i+3]
        print(segments[0][i:i+3] + "\n" + segments[1][i:i+3] + "\n" + segments[2][i:i+3])
        result += digit_mapping.get(segment, "?")
    return result

# Test the example provided
# segment_string = """
#    _  _     _  _  _  _  _  _   
#  | _| _||_||_ |_   ||_||_|| |
#  ||_  _|  | _||_|  ||_| _||_|
# """
# print(seven_segment_to_string(segment_string)) # Output: "1234567890"
