# from models import Job
#
# job = Job()
#
# job.row_number = 5
#
# job.retailer = "Target"
#
# job.comments.append("Identity matched")
#
# print(job)

from models import Candidate

candidate = Candidate()

candidate.identity_score = 96.5

candidate.discovered_by.append("Exact Search")

print(candidate)
