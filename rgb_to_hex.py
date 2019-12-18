
rgb = [0,128, 64]
print(*rgb) # * before means unzip
def rgb2hex(r,g,b):
    return f'#{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}'

print(rgb2hex(*rgb))