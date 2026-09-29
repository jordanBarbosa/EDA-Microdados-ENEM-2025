# %%
import pandas as pd
df = pd.read_csv("dados/DADOS/ITENS_PROVA_2025.csv", sep=";", encoding="iso-8859-1")
df.head()

# %%
df.info()

# %%
df_amarela = df[(df["TX_COR"] == "AMARELA") & (df["CO_PROVA"] == 1550)]
df_amarela.head()

# %%
df_amarela[["SG_AREA", "TP_LINGUA", "CO_ITEM"]].groupby(by=["SG_AREA", "TP_LINGUA"]).nunique()

# %%

df[["SG_AREA", "TP_LINGUA"]].groupby("SG_AREA").count()
# %%
df[(df["IN_ITEM_ABAN"] == 1)]
# %%
df[(df["CO_ITEM"] == 44935)].sort_values(by="CO_PROVA")
# %%

df_teste = (df[["CO_PROVA", "CO_ITEM"]].groupby(by=["CO_PROVA", "CO_ITEM"]).value_counts().reset_index())
df_teste[(df_teste["count"] > 1)]

# %%
set(df["TX_GABARITO"])
# %%
df[(df["IN_ITEM_ABAN"] == 1)]
# %%
df[["TX_MOTIVO_ABAN", "IN_ITEM_ABAN"]].groupby(by="IN_ITEM_ABAN").value_counts().reset_index()
# %%
