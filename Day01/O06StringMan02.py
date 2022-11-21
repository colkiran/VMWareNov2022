
# maketrans, translate
st = "hello world"
print(f"st :{st}")
a = "helowrd"
b = 'HELOWRD'
# the length of a and b should be the same

resTbl = st.maketrans(a, b)
print(resTbl)

res = st.translate(resTbl)
print(f"res :{res}")

print("split".center(40, "-"))

st1 = "the quick brown fox jumps over the lazy dog"
print(f"st1 :{st1}")

res= st1.split()            # by default the delimiter is a space
print(f"res :{res}")

res1 = " ".join(res)
print(f"res1 :{res1}")

print("strip".center(40, "-"))
st = "********hello********"
print(f"st :{st}")

res = st.lstrip("*")
print(f"res :{res}")

res = st.rstrip("*")
print(f"res :{res}")

res = st.strip("*")
print(f"res :{res}")
