# Calculate ball bouncing height
def ballBounceHeight(times):
    totalHeight, bounceHeight = 100, 100
    while times > 0:
        bounceHeight /= 2
        totalHeight += 2 * bounceHeight
        times -= 1
    return totalHeight, bounceHeight

if __name__ == '__main__':
    times = 10
    totalHeight, reboundHeight = ballBounceHeight(10)
    print("totalHeight =", totalHeight, "\n"+str(times)+"th bounceHeight =", reboundHeight)
