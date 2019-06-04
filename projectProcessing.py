import pandas as pd
signups = pd.read_excel("signups.xlsx", sheet_name = "Sheet1")

# Take care of missing values
print("\nThe following people need to be contacted because they didn't provide a complete response")
print(signups.apply(lambda x: print(signups[x.isnull()].Name.to_string(index=False))))

print("\nMESA Machine Signups: ")
print(signups[signups.Machine == 1].Name.to_string(index=False))

print("\nGlider Signups:")
print(signups[signups.Glider == 1].Name.to_string(index=False))

print("\nTank Signups:")
print(signups[signups.Tank == 1].Name.to_string(index=False))

print("\nBridge Signups:")
print(signups[signups.Bridge == 1].Name.to_string(index=False))

print("\nArm Signups:")
print(signups[signups.Arm == 1].Name.to_string(index=False))
