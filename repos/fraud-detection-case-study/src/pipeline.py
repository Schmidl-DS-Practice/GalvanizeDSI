org_name_ratio = df.groupby('org_name')['fraud'].mean().rename(name_ratio).reset_index()

df2 = df2.merge(org_name_ratio)