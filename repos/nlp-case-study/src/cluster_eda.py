import k_m


if __name__ == "__main__":
    df = k_m.get_pipe_clustered(n_clusters=2)
    df[['city', 'state']] = df['location'].str.split(", ", expand = True)
    cluster_1 = df[df['Kmean_label'] == 0]
    cluster_2 = df[df['Kmean_label'] == 1]
    # print(df[df['Kmean_label'] == 0]['text'])
    # print(df[df['Kmean_label'] == 1]['text'])
    for index,row in cluster_1.iterrows():
        print(row['text'])