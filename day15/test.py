def get_surrounding(coord:complex,size:int):
    # Iterate through the y values (coord.imag-size -> coord.imag+size)
    # Iterate through the x values between the derrived points on the current y value (coord.real-l//2 -> coord.real+l//2)
    for y in range(int(coord.imag)-size, int(coord.imag)+size+1):
        d=abs(y-int(coord.imag))
        l=2*abs(size-d)+1
        start_x, end_x = int(coord.real)-l//2, int(coord.real)+l//2
        for x in range(start_x, end_x+1):
            yield complex(x,y)

def fancy(coords,size):
    real_size=size*2+1
    template=[[" "]*real_size]*real_size
    for i in coords:
        template[int(i.imag)+size][int(i.real)+size]="#"
    print("\n".join("".join(i for i in j) for j in template))

a=sorted(list(get_surrounding(0j,2)),key=lambda i:i.imag)
fancy(a,2)
