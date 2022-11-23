
glbX = 100                              # global variable

def fun(n):                             # local variable
    global glbX
    glbX = 250
    print(n)
    # glbX = 250                          # local variable with glb_var name
    print(f"glbX inside :{glbX}")
    st = "hello world"                 # local variable
    print(st)

print(f"glbX before :{glbX}")

fun(500)

print(f"glbX after :{glbX}")
