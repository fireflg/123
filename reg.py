import re
text = 'вфывфы 81.11.2.31 ыфвфыв'
print(re.search(r"([0-9]{1,3}[\.]){3}[0-9]{1,3}", text))
