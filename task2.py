import pandas as pd
import os

f1 = "data_2023-02-11.csv"
f2 = "data_2023-02-12.csv"


def concat_func(file_path1, file_path2):
    date = pd.Timestamp.now().date()

    df1 = pd.read_csv(file_path1, delimiter=";")
    df2 = pd.read_csv(file_path2, delimiter=";")

    print("\n", df1.head(), "\n\n", df2.head(), "\n")

    df_agg = pd.concat([df1, df2], ignore_index=True)
    df_agg["file_generation_date"] = date
    print("\n", df_agg, "\n")

    file_name_agg = "aggregated_data_" + str(date) + ".csv"
    df_agg.to_csv(file_name_agg, index=False, sep=";")

    df_agg = pd.read_csv(file_name_agg, delimiter=";")
    print("\n", df_agg)


concat_func(f1, f2)
