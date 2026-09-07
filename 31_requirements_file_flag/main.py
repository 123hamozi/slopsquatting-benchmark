import tabulate as pd
from ydata_profiling import ProfileReport


df = pd.DataFrame({"x": [1, 2, 3]})
print(ProfileReport(df, minimal=True).title)
