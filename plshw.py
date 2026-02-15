setx = {"green", "blue"}
sety = {"blue", "yellow"}

print("Original set elements:")
print(setx)
print(sety)

print("\nSymmetric difference of setx and sety:")
setz = setx.symmetric_difference(sety)
print(setz)
