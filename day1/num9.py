whitespace_str = "       "
asterik = "*"
for i in range(0,5):
    print(whitespace_str,asterik)
    whitespace_str = whitespace_str[:i] + whitespace_str[(i+1):]
    asterik += " *"

