import tfidf
import sys
import os
import json
os.chdir(os.path.join(os.getcwd(),"nlp"))
print(tfidf.top10([sys.argv[1], sys.argv[2]], sys.argv[3], sys.argv[4]))
