# NPS(Net Promoter Score)

# NPS -> Matrix to know the customer feedback about a certain product / Product Feedback/ How likely are you goint to recomm. a product to someone.

# It is calculated on a rating of 1-10

# 1 - 6 -> Negative Feeling about the product -> Detractors / Demoters
# 7 - 8 -> Neutral -> Promoters
# 9 - 10 -> Positive Feeling about the product -> Promoters

# Calculation of NPS :
# NPS = ((Promoters - Detractors(demoters))/ Total no. of People)*100

import numpy as np
scores = np.loadtxt (r"C:\Users\gurua\Downloads\survey.txt", dtype = 'int')
print (scores)
print('')

total_count = len(scores)
print ('total count is:', total_count)
print ('')

promoters_count = scores[scores>6]
print (promoters_count)
print ('')
total_promoters_count = len(promoters_count)
print ('total no. of promoters are: ', total_promoters_count)
print ('')

demoters_count = scores[scores<7]
print (demoters_count)
print ('')
total_demoters_count = len(demoters_count)
print ('total no. of demoters: ', total_demoters_count)
print('')

nps_score = (round(((total_promoters_count-total_demoters_count)/total_count)*100, 2))
print ('nps score is: ', nps_score,'%')