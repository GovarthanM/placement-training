x = 5
assert x > 0, "x should be positive"

print("x is positive.")

try:
    y = -3
    assert y > 0, "y should be positive"
except AssertionError as e:
    print("AssertionError:", e)

z = 10
assert z % 2 == 0, "z should be even"
print("z is even.")
