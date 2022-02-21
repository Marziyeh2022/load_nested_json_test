import json

datalist = []
print("Started Reading JSON file which contains multiple JSON document")
with open('/content/sample_data/5143_2021-04-21_logs.json') as f:
    for jsonObj in f:
        log = json.loads(jsonObj)
        datalist.append(pd.json_normalize(log))

result_table =[]
for data in datalist:
  result_table.append(data[['tags.url', 'weboid' ]])

result_pd = pd.concat(result_table)
final_output = result_pd['tags.url'].value_counts().rename_axis('url').reset_index(name='hits')
final_output.to_csv('output.csv')