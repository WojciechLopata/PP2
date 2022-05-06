import os
import pandas as pd
print(*[filename.split(".")[0] for filename in os.listdir("./opinions")],sep="\n")
id=input("Podaj id produktu którego opinie chcesz sprawdzić ")
opinions=pd.read_json(f"opinions/{id}.json")
print(opinions)