import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    scores = []

    for item in sys.argv[1:]:
        try:
            scores.append(int(item))
        except:
            print(f"Invalid parameter: '{item}'")
    
    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        total = sum(scores)
        count = len(scores)
        average = total / count
        high = max(scores)
        low = min(scores)
        score_range = high - low

        print("Scores processed:", scores)
        print("Total players:", count)
        print("Total score:", total)
        print("Average score:", average)
        print("High score:", high)
        print("Low score:", low)
        print("Score range:", score_range)
    
