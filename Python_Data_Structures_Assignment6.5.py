text = "X-DSPAM-Confidence:    0.8475"
zap1 = text.find("0")
zap2 = text.find("5")
zap3 = float(text[zap1:zap2+1])
print(zap3)
