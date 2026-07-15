from models import MatchResult

result = MatchResult()

result.score = 96.4

result.matched = True

result.method = "Identity + Variant"

result.notes.append("Identity matched")

print(result)