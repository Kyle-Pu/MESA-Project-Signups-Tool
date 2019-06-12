import pandas as pd
signups = pd.read_excel("signups.xlsx", sheet_name = "Sheet1")

# Take care of missing values
print("\nThe following people need to be contacted because they didn't provide a complete response")
print(signups.apply(lambda x: print(signups[x.isnull()].Name.to_string(index=False))))

# Function to find all people that have signed up for the specific project.
# Note: This was possible because I'm now accessing each column using bracket notation instead of dot notation. Previously, when I used dot notation to access all columns, it wasn't possible to take in column names as a parameter. 
def findNames(col):
    return signups[signups[col] == 1].Name.to_string(index=False)

print("\nMESA Machine Signups:\n", findNames("Machine"), sep = "")
print("\nGlider Signups:\n", findNames("Glider"), sep = "")
print("\nTank Signups:\n", findNames("Tank"), sep = "")
print("\nBridge Signups:\n", findNames("Bridge"), sep = "")
print("\nArm Signups:\n", findNames("Arm"), sep = "")
print("\n\n\n")

signups.set_index('Name', inplace = True)

for row in signups.index:

    numProjects = 0

    for col in signups.columns:
        if signups.loc[row][col] in [1]:
            numProjects += 1

    print(row, "has", numProjects, "projects.")



