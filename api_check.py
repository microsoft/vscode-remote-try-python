import requests

AUTH = 'AfasToken PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+OENDNjVGQUE3RjBGNEYwMkIxRjVFRDAyOTA5RDEyQzBCRDlBQUNCMTNEREM0MkNEODMxRTQyNzExQ0JGMzFCQzwvZGF0YT48L3Rva2VuPg=='
url = "https://83448.rest.afas.online/profitrestservices/connectors/ETL2_Dossier2_Verzuimverloop/"

headers = {
    'Authorization': AUTH
}

response = requests.get(url, headers=headers)

print(f"Status code: {response.status_code}")
print("Headers:", response.headers)
print("Response body:", response.text)