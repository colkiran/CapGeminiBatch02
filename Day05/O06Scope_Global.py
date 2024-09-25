
glbx = 500

def fun(x):             # x is a local variable
    global glbx         # do not assign any value in this line

    print(f"x :{x}")
    glbx = 1500
    print(f"inside glbx :{glbx}")


print(f"before glbx :{glbx}")

fun(50)

print(f"after glbx :{glbx}")
