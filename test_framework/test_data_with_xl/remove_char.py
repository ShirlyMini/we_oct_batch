str1="₹ 15,000"
srt2="15000"

srt3 = str1.replace("₹ ", "").replace(",", "")
print(float(srt3))