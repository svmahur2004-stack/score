import sys

if len(sys.argv) > 1:
    script_name = sys.argv[0]
    scores = [float(score) for score in sys.argv[1:]]
    print("User provided input values:")
    print("Script name:", script_name)
    print("Scores:", scores)
    print("Sum:", sum(scores))
    print("Average:", sum(scores) / len(scores))
    print("Max:", max(scores))
    print("Min:", min(scores))
else:
    script_name = sys.argv[0]
    scores = [90, 80, 70, 60, 50]
    print("No input given:")
    print("Script name:", script_name)
    print("Scores:", scores)
    print("Sum:", sum(scores))
    print("Average:", sum(scores) / len(scores))
    print("Max:", max(scores))
    print("Min:", min(scores))